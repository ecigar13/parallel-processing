import random
import time
from multiprocessing import *

int_list: [] = [i for i in range(99999)]


class TestMulti:
    def __init__(self):
        pass

    def producer_add(self, q: Queue, limit: int):
        while q.qsize() < limit:
            num = random.random()
            q.put(num)

    def consumer(self, q: Queue):
        if q.qsize() != 0:
            print(q.get())

    def run(self):
        # pool = Pool(cpu_count())
        q: Queue = Queue()
        limit: int = 999
        process_generates = [Process(target=self.producer_add, args=(q, 999)) for i in range(cpu_count())]
        process_prints = [Process(target=self.consumer, args=(q,)) for i in range(cpu_count())]
        for p in process_generates:
            p.start()

        # time.sleep(5)
        for p in process_generates:
            p.join()

        print(q.qsize(), len(process_generates))

        # for pr in process_prints:
        #     pr.start()
        # for pr in process_prints:
        #     pr.join()

        print(q.qsize(), len(process_prints))


if __name__ == '__main__':
    tm = TestMulti()
    start = time.perf_counter_ns()
    tm.run()
    interval = time.perf_counter_ns() - start
    print(interval)
