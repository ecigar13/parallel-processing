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
            print(f"Putting")
            time.sleep(0.5)

    def consumer(self, q: Queue):
        while True:
            print(f"Getting: {q.get()}")
            time.sleep(0.5)

    def run(self):
        # pool = Pool(cpu_count())
        q: Queue = Queue()
        limit: int = 20
        process_generates = [Process(target=self.producer_add, args=(q, 999)) for i in range(cpu_count())]
        process_prints = [Process(target=self.consumer, args=(q,)) for i in range(cpu_count())]
        for p in process_generates:
            p.start()

        # time.sleep(5)

        print(q.qsize(), len(process_generates))

        for pr in process_prints:
            pr.start()
        for p in process_generates:
            p.join()
        for pr in process_prints:
            pr.join()

        print(q.qsize(), len(process_prints))


if __name__ == '__main__':
    tm = TestMulti()
    start = time.perf_counter_ns()
    tm.run()
    interval = time.perf_counter_ns() - start
    print(interval)
