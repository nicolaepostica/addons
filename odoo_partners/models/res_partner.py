# -*- coding: utf-8 -*-
import base64

import requests
from bs4 import BeautifulSoup

from odoo import api, models

BASE_URL = 'https://www.odoo.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
}


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def update_partners_list(self):
        def fix_country_name(country_name: str) -> str:
            if country_name == 'Slovak Republic':
                return 'Slovakia'
            else:
                return country_name

        page = 1
        while True:
            response = requests.get(f'{BASE_URL}/partners/page/{page}?country_all=True', headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            partners_list = soup.select('#ref_content div.media.mt-3 div.o_partner_body > a')

            for _ in partners_list:
                name = _.find('span').text
                if self.env['res.partner'].search([('name', '=', name)]):
                    continue
                href = _.attrs["href"]
                partner_content = requests.get(f'{BASE_URL}{href}', headers=headers).content
                soup_partner = BeautifulSoup(partner_content, 'html.parser')

                level = soup_partner.select_one('#wrap h3 span').text
                try:
                    address = soup_partner.find('span', {"itemprop": "streetAddress"}).contents
                    street = ' '.join(address[:-1:2])
                    country = self.env['res.country'].search([('name', '=', fix_country_name(address[-1]))])[0].id
                except:
                    street = ''
                    country = False
                try:
                    phone = soup_partner.find('span', {"itemprop": "telephone"}).text
                except:
                    phone = ''
                try:
                    website = soup_partner.find('span', {"itemprop": "website"}).text
                except:
                    website = ''
                try:
                    email = soup_partner.find('span', {"itemprop": "email"}).text
                except:
                    email = ''
                avatar_url = f"https:{soup_partner.select_one('img.img.img-fluid.d-block').attrs['src']}"
                description = soup_partner.select_one('div.col-lg-8.mt32 > div').encode_contents().decode("utf-8")
                avatar = base64.b64encode(requests.get(avatar_url, headers=headers).content).decode("utf-8")

                categories = self.env['res.partner.category'].search(
                    ['|', ('name', '=', level), ('name', '=', 'NewPartner')]).ids
                self.env['res.partner'].create({
                    'name': name,
                    'display_name': name,
                    'website': website,
                    'email': email,
                    'phone': phone,
                    'street': street,
                    'country_id': country,
                    'comment': description,
                    'image_1920': avatar,
                    'category_id': categories,
                })

            if soup.select_one('li.page-item.disabled'):
                if soup.select_one('li.page-item.disabled').text.strip() == 'Next':
                    break
            page += 1
