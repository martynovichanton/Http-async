import time
import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
# logging.basicConfig(level=logging.DEBUG)



def download_url(url, session):
    response = session.request("get", url)
    print(f"Read {len(response.content)} from {url}")
    # print(response.json())
    return response.json()

def download_all_urls(urls):
    session = requests.Session()
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_list = []
        for url in urls:
            future = executor.submit(download_url, url, session)
            future_list.append(future)
        session.close()
        print("*******************************************************************")
        for f in as_completed(future_list):
            print(f.result())

def main():
    urls = [f"http://localhost:55555/{i}" for i in range(0,100)]
    download_all_urls(urls)

if __name__ == "__main__":
    start_time = time.time()
    main()
    duration = time.time() - start_time
    print(f"Downloaded in {duration} seconds")
