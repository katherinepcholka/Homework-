from multiprocessing import Process
from time import time, sleep


def math(num):
    sleep(5)
    print("Result {}".format(num ** 2 + -num*3 + 6))


if __name__ == "__main__":  
    start = time() * 1000
    nums = [-3, 8, 5]
    procs = []

    print("Process simulation")
    sleep(1)
    print("Important calculation...")

    for num in nums:
        proc = Process(target=math, args=(num,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    end = time() * 1000

    print(f"Total time: {end - start}")