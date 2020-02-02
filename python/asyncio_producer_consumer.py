import asyncio
import logging.config
from asyncio import queues

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

    async def producer_get_site(self, site_queue: queues.Queue, response_queue: queues.Queue):
        while site_queue.qsize() > 0:
            site: str = await site_queue.get()
            res = requests.get(site)
            print(res.status_code)
            await response_queue.put(res)
            site_queue.task_done()

    async def consumer_log_response(self, res_queue: queues.Queue):
        while True:
            print(res_queue.qsize())
            item: requests.Response = await res_queue.get()
            print(item.url)
            res_queue.task_done()

    async def run(self):
        site_queue: queues.Queue = queues.Queue()
        response_queue: queues.Queue = queues.Queue()
        for site in site_list:
            await site_queue.put(site)
        print(site_queue.qsize())
        await asyncio.gather(self.consumer_log_response(response_queue),
                             self.producer_get_site(site_queue, response_queue))

if __name__ == '__main__':
    m = GetWebsite()
    asyncio.run(m.run())
