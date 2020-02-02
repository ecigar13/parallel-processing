import random
import time
from multiprocessing import *

int_list: [] = [i for i in range(999)]


class TestMulti:
    def __init__(self):
        pass

    def producer_add(self, q: Queue, limit: int):
        while q.qsize() < limit:
            num = random.random()
            q.put(num)
            print(f"Q size {q.qsize()}")
            time.sleep(0.5)
        q.put(None)

    def consumer(self, q: Queue):
        while True:
            temp = q.get()
            if temp is None:
                break
            print(f"Getting: {temp}")

    def run(self):
        # pool = Pool(cpu_count())
        q: Queue = Queue()
        limit: int = 20
        process_generates = [Process(target=self.producer_add, args=(q, limit)) for i in range(2)]
        process_prints = [Process(target=self.consumer, args=(q,)) for i in range(2)]


        print(q.qsize(), len(process_generates))

        for pr in process_prints:
            pr.start()
        for p in process_generates:
            p.start()

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
