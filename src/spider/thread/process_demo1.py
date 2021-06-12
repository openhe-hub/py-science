from multiprocessing import Process

def func():
    for i in range(1000):
        print(f'{i} in sub process')


if __name__ == '__main__':	
    p=Process(target=func)
    p.start()
    for i in range(1000):
        print(f'{i} in main process')