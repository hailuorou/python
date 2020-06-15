# 线程池

from concurrent.futures import ThreadPoolExecutor
import time
import threading

def work(n):
    print(f'给{n}打电话,线程号：{threading.current_thread()}')
    time.sleep(3)
    print(f'通话结束:{n}')


userlist = {'张三', '李四', '王五', '赵六', '田七'}

# 创建线程池
pool = ThreadPoolExecutor(max_workers=3)

# 循环指派任务
for i in userlist:
    # 指定任务
    pool.submit(work, i)

# 关闭线程池
pool.shutdown()