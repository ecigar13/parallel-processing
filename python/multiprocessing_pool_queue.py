import random
import time
from multiprocessing import *

int_list: [] = [i for i in range(999)]
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


class TestMulti:
    def __init__(self):
        pass

    def producer_add(self, q: Queue, limit: int):
        while q.qsize() < limit:
            num = random.random()
            q.put(num)
            print(f"Q size {q.qsize()}")
            time.sleep(0.25)
        q.put(None)

    def consumer(self, q: Queue):
        while True:
            temp = q.get()
            if temp is None:
                break
            print(f"Getting: {temp}")

    def run(self):
        # pool = Pool(cpu_count())
        m = Manager()
        q: Queue = m.Queue()
        producer_pool = Pool(2)
        consumer_pool = Pool(2)
        limit: int = 20

        consumer_pool.apply_async(self.consumer, args=(q,))
        producer_pool.apply(self.producer_add, args=(q, limit))


if __name__ == '__main__':
    tm = TestMulti()
    start = time.perf_counter_ns()
    tm.run()
    interval = time.perf_counter_ns() - start
    print(interval)
