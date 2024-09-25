import aiohttp
import asyncio
from website import Website
from fetcher import fetch
def main():
    async with aiohttp.ClientSession() as session:
        website = Website("Bauhaus")
        site_response = await fetch(session,website.site,return_type='json')
        print(site_response)
if __name__ == "__main__":
    main()
