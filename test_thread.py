import threading
import time


def print_time(threadName,delay):
    count =0
    while count<5:
        time.sleep(delay)
        count+=1
        print('%s:%s '%(threadName,time.ctime(time.time())))
try:
    threading.start_new_thread(print_time,("Thread-1", 2, ))
except Exception as e:
    print(e)