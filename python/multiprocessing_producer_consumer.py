import logging.config
import time
from multiprocessing import *

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

    def print_sync(self):
        for link in site_list:
            print(link)

    def print_base(self, x: str):
        print(x)

    def print_multi(self):
        with Pool(5) as p:
            p.map(self.print_base, site_list)


if __name__ == '__main__':
    m = GetWebsite()
    start = time.perf_counter_ns()
    m.print_sync()
    print(time.perf_counter_ns() - start)

    start = time.perf_counter_ns()
    m.print_multi()
    print(time.perf_counter_ns() - start)
