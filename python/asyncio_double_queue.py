import asyncio
import logging.config
import random

import requests

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)
site_list: [] = [
    "http://www.microsoft.com",
    "http://www.google.com",
    "http://docs.google.com",
    "http://en.wikipedia.org",
    "http://github.com", "https://www.yahoo.com/", "https://www.quickstart.com/",
    "http://www.linkedin.com",
    "http://www.bbc.co.uk", "https://www.reddit.com/", "https://www.surveymonkey.com/", "https://bitly.com/",
    "https://www.dropbox.com/", "https://www.youtube.com/channel/UCNJIEbGZaScUDsq_DMYTjYg"
]


class GetWebsite:

    def __init__(self):
        pass

    async def producer_site(self, site_queue: asyncio.Queue):
        for i in site_list:
            print(i)
            await site_queue.put(i)
        await site_queue.put(None)

    async def producer_get_site(self, site_queue: asyncio.Queue, response_queue: asyncio.LifoQueue):
        while True:
            site: str = await site_queue.get()
            if site is None:
                break
            print(site)
            res: requests.Response = requests.get(site)
            await response_queue.put(res)
            site_queue.task_done()
        await response_queue.put(None)

    async def consumer_log_response(self, response_queue: asyncio.Queue):
        while True:
            item: requests.Response = await response_queue.get()
            if item is None:
                break
            print(item)
            response_queue.task_done()

    async def run(self):
        site_queue: asyncio.Queue = asyncio.Queue()
        response_queue: asyncio.Queue = asyncio.Queue()

        run = await asyncio.gather(self.consumer_log_response(response_queue),
                                   self.producer_get_site(site_queue, response_queue),
                                   self.producer_site(site_queue)
                                   )

if __name__ == '__main__':
    m = GetWebsite()
    asyncio.run(m.run())
