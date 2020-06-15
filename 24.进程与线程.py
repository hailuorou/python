
'''

'''
import os,threading
import time
from multiprocessing import Process
from threading import Thread

def work(n):
    print(f'给{n}打咨询电话，进程号{os.getpid()},线程号:{threading.current_thread()}')
    time.sleep(3)
    print(f'销售电话结束:{n}')


userlist = {'张三', '李四', '王五'}

# 启动一个进程，进程中有一个线程
# for item in userlist:
#     work(item)

# 多进程类似创建多个部门
# if __name__ == '__main__':
#     plist = []
#     for item in userlist:
#         # 循环创建进程
#         p = Process(target=work, args=(item,))
#         # 启动进程
#         p.start()
#         # 吧创建的进程加入到列表中
#         plist.append(p)
#
#     # 阻塞终止进程的执行
#     for i in plist:
#         i.join()


# 多线程类似给该部门增加人手参加工作
if __name__ == '__main__':
    plist = []
    for item in userlist:
       # 循环创建线程
        p = Thread(target=work, args=(item,))
        # 生成线程
        p.start()
        # 吧创建的线程加入到列表中
        plist.append(p)

    # 阻塞终止线程的执行
    for i in plist:
        i.join()