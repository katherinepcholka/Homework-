from threading import Thread
from time import time, sleep


def math(num):
    sleep(5)
    print("Result {}".format(num ** 2 + -num*3 + 6))


if __name__ == "__main__":  
    start = time() * 1000
    nums = [4, -10, 7]
    threads = []

    print("Threading simulation")
    sleep(1)
    print("Important calculation...")

    for num in nums:
        thread = Thread(target=math, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time() * 1000

    print(f"Total time: {end - start}")