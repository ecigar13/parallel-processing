import random
import time
from multiprocessing import *

int_list: [] = [i for i in range(99999)]


class TestMulti:
    def __init__(self):
        pass

    def producer_add(self, q: Queue):
        num = random.random()
        q.put(num)

    def consumer(self, q: Queue):
        print(q.get())

    def run(self):
        # pool = Pool(cpu_count())
        q: Queue = Queue()
        process_generate = Process(target=self.producer_add, args=(q,))
        # process_print = Process(target=self.consumer, args=(q,))
        process_generates = [process_generate for i in range(cpu_count())]
        # process_prints = [process_print for i in range(cpu_count())]
        for p in process_generates:
            p.start()

        for p in process_generates:
            p.join()


        # for pr in process_prints:
        #     pr.start()
        # for pr in process_prints:
        #     pr.join()


if __name__ == '__main__':
    tm = TestMulti()
    start = time.perf_counter_ns()
    tm.run()
    interval = time.perf_counter_ns() - start
    print(interval)