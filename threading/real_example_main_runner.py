import time
from datetime import datetime
import threading


# Convert the str from [datetime.now().strftime('%H:%M:%S')] to tuples of integers and compare the tuples
def split_hrs(s):
    return tuple(int(x) for x in s.split(':'))


def cal_sqre(num):  # define a square calculating function
    for n in num:  # Use for loop
        time.sleep(0.5)  # at each iteration it waits for 0.3 time
        print(" Calculate the square root of the given number")
        print(' Square is : ', n * n)


def cal_cube(num):  # define a cube calculating function
    for n in num:  # for loop
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print(" Calculate the cube of  the given number")
        print(" Cube is : ", n * n * n)


def cal_cumbia(num):  # define a cube calculating function
    for n in num:  # for loop
        time.sleep(3)  # at each iteration it waits for 0.3 time
        print("###################################")
        print(" Calculate the Cumbia of  the given number")
        print(f"Cumbia is : {n * n * n * n} ######")
        print("###################################")


try:
    start = time.perf_counter()
    ar = [4, 5, 6, 7, 2]  # given array
    finish_time = finish_time = '20:16:00'
    print("Starting Threads... ")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        t = time.time()  # get total time to execute the functions
        th1 = threading.Thread(target=cal_sqre, args=(ar,))
        th2 = threading.Thread(target=cal_cube, args=(ar,))
        th3 = threading.Thread(target=cal_cumbia, args=(ar,))
        th1.start()
        th2.start()
        th3.start()
        th1.join()
        th2.join()
        th3.join()
        if split_hrs(current_time) > split_hrs(finish_time):
            print(" Again executing the main thread... ")
            break
except Exception as e:
    raise
finally:
    finish = time.perf_counter()
    print(f"Stop the script at: {datetime.now().strftime('%H:%M:%S')}")
    print(f'Finished in {round(finish - start, 2)} second(s)')
