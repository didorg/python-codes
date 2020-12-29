from threading import Thread, Lock
import time

db_value = 0


def increase(lock):
    global db_value

    with lock:  # Acquire and release the lock for you
        local_copy = db_value
        local_copy += 1
        time.sleep(0.1)
        db_value = local_copy


if __name__ == "__main__":
    lock = Lock()
    print('Start value ', db_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('End value ', db_value)
    print('End main')
