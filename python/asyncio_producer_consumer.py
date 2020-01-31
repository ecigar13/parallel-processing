import asyncio
import logging.config
import random
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

    async def producer_get_site(self, site_queue: queues.Queue, response_queue: queues.LifoQueue):
        while site_queue.qsize() > 0:
            logger.debug(site_queue.qsize())
            site: str = await site_queue.get()
            print(site)
            res = requests.get(site)
            await response_queue.put(res)
            site_queue.task_done()
        await response_queue.put(-1)

    async def consumer_log_response(self, queue: queues.Queue):
        while queue.qsize() > 0:
            item: requests.Response = await queue.get()
            print(item)
            logger.debug(item)
            queue.task_done()

    async def run(self):
        site_queue: queues.LifoQueue = queues.LifoQueue()
        response_queue: queues.LifoQueue = queues.LifoQueue()
        for site in site_list:
            site_queue.put_nowait(site)
        print(site_queue.qsize())
        run = await asyncio.gather(self.consumer_log_response(response_queue),
                                   self.producer_get_site(site_queue, response_queue)
                                   )

m = GetWebsite()
loop = asyncio.get_event_loop()
loop.run_until_complete(m.run())
loop.close()
