import aiohttp
import asyncio
import requests

async def fetch(session, url):
    headers = {}
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def main():
    url = 'http://localhost:55555/'
    async with aiohttp.ClientSession() as session:
        for i in range(1,10):
            html = await fetch(session, f'{url}{i}')
            print(html)

loop = asyncio.get_event_loop().run_until_complete(main())

