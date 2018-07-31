# import time
# import threading
# c=0
# lock = threading.Lock()
# def chang_id(n):
#     global c
#     c = c+n
#     c = c-n
#
# def run(n):
#     for i in range(10000):
#         lock.acquire()
#         try:
#             chang_id(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run,args=(5,))
# t2 = threading.Thread(target=run,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(c)
import time
import threading
import multiprocessing

def loop():
    x=0
    while x<5:
        x = x+1
        print(x)
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target =loop)
    t.start()
