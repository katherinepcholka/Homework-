from threading import Thread
from time import sleep

def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n

def math(num):
    sleep(1)
    print(f'Factorial {num} = {fac(num)}')

if __name__ == "__main__":
    nums = []

    for x in range(3):
        x = int(input('Number: '))
        nums.append(x)
    
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
