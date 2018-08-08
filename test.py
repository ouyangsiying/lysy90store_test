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


# import time
# import threading
# import multiprocessing
#
# def loop():
#     x=0
#     while x<5:
#         x = x+1
#         print(x)
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target =loop)
#     t.start(）


# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('Run child process %s (%s)..'%(name,os.getpid()))
#
# if __name__ == '__main__':
#     print('父进程%s'%os.getpid())
#     p = Process(target = run_proc,args=('test',))
#     print("孩子进程开始了")
#     p.start()
#     p.join()
#     print("孩子进程结束")

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('task name is %s ,id is %s'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('task %s run 0.2f seconds'%(name,end-start))

if __name__ =='__main__':
    print('父进程%s'%os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')



