import asyncio
import requests
import json
from lxml import html as lxml_html

class fetcher:
    
    async def fetch(session, url, return_type):
        async with session.get(url) as response:
            if return_type == 'text':
                return await response.text()
            elif return_type == 'json':
                return await response.json()
    async def find_items(session,url,return_type='text'):
        global not_found, item_list
        not_found =0
        item_list = []
        i = 0
        while not_found == 0:
            i = i + 1
            url = f'{url}?p={i}' 
            html_content = await fetcher.fetch(session,url,return_type='text')
            if len(html_content)<10:
                return
            tree = lxml_html.fromstring(html_content)
            for attempt in range(3):
                products_in_frame = tree.xpath('//a[@class="card"]/@href')
                if products_in_frame:
                    item_list.extend(products_in_frame)
                    break
                else:
                    not_found=1
                    break

    async def process_item(session, item):
        html_content = await fetch(session, item, return_type='text')
        if len(html_content) < 10:
            return

        tree = lxml_html.fromstring(html_content)
        categories, varetekst, sku_id, ean_number, price, dropship, store, stock_total, brand = [], None, None, None, None, None, None, None, None

        for attempt in range(3):
            if not sku_id:
                script_content = tree.xpath('//script[@id="ng-state"]/text()')
                if script_content:
                    json_data = json.loads(script_content[0])
                    first_key = list(json_data.keys())[0]
                    data = json_data.get(first_key, {}).get("b", {}).get("data", [])
                    if data:
                        sku_id = data[0].get("id")
                        break  # Exit the loop if we successfully retrieve the ID

        return sku_id  # Or other values as needed

