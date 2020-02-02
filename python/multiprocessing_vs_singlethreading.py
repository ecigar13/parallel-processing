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

int_list: [] = [i for i in range(99999)]


class GetWebsite:

    def __init__(self):
        pass

    def print_sync(self, input_list: []):
        for link in input_list:
            self.print_base(link)

    def print_base(self, x: str):
        print(x*x, end="")

    def print_multi(self, input_list: []):
        with Pool(4) as p:
            p.map(self.print_base, input_list)


if __name__ == '__main__':
    m = GetWebsite()
    start = time.perf_counter_ns()
    m.print_sync(int_list)
    interval = time.perf_counter_ns() - start

    start = time.perf_counter_ns()
    m.print_multi(int_list)
    interval1 = time.perf_counter_ns() - start
    print("\n")
    print(interval, interval1)
    print(interval > interval1)
