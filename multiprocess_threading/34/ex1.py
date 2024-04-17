import threading
from random import randint

lst = [randint(10, 100) for i in range(20)]

even = []
odd = []

def func():
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

if __name__ == '__main__':
    lock = threading.Lock()

    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

print(f"Четные числа: {even}\nНечётные числа: {odd}")