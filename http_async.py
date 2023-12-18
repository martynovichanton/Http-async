import asyncio
import aiohttp
import time
import logging
# logging.basicConfig(level=logging.DEBUG)

async def download_url(session, url):
    response = await session.get(url)
    # async with session.get(url) as response:
    print("Read {0} from {1}".format(response.content_length, url))
    # print(await response.json())
    return await response.json()

async def download_all_urls(urls):
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=100))
    # async with aiohttp.ClientSession() as session:
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_url(session, url))
        tasks.append(task)
    responses = await asyncio.gather(*tasks, return_exceptions=True)
    await session.close()
    print("*******************************************************************")
    for response in responses:
        print(response)
    
async def main():
    urls = [f"http://localhost:55555/{i}" for i in range(0,100)]
    await download_all_urls(urls)
    
if __name__ == "__main__":
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(main())
    duration = time.time() - start_time
    print(f"Downloaded in {duration} seconds")