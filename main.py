import aiohttp
import asyncio
from website import Website
from fetcher import fetcher
async def main():
    async with aiohttp.ClientSession() as session:
        website = Website("Bauhaus")
        for element in website.sites:
            page = f'{website.site}{element}'
            site_response = await fetcher.find_items(session,page)
            
if __name__ == "__main__":
    asyncio.run(main())
