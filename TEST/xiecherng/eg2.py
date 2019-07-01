
import greenlet
import time


# 任务1
def work1():
    for i in range(5):
        print("work1执行中...")
        time.sleep(0.2)
        # 切换到第二个协程执行对应的任务
        a2.switch()

# 任务2
def work2():
    for i in range(5):
        print("work2执行中...")
        time.sleep(0.2)
        # 切换到第一个协程执行对应的任务
        a1.switch()

# 创建协程1
a1 = greenlet.greenlet(work1)

# 创建协程2
a2 = greenlet.greenlet(work2)

if __name__ == '__main__':
    # 切换到第一个协程执行对应的任务
    a1.switch()
