import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second ... ')
    time.sleep(seconds)
    return f'Done Sleeping in {seconds} second(s) '


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # submit() Method returns a 'Future instance' representing the execution of the callable
    # --------
    # result = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(result):
    #     print(f.result())

    # map() returns the result
    # -----
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
