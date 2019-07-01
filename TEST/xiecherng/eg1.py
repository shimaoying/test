import time


# 定义协程1
def work1():
    for i in range(100):
        print("work1执行中...%s",i)
        # time.sleep(0.2)
        yield

# 定义协程2
def work2():
    for i in range(100):
        print("work2执行中...%d",i)
        # time.sleep(0.2)
        yield  # 本质上使用yield就是一个生成器

if __name__ == '__main__':
    # 创建协程
    g1 = work1()
    g2 = work2()
    # print(g1, g2)
    for i in range(10):
    # 使用next函数启动协程
        next(g1)
        next(g2)
    #g1 g2 有序交替执行
