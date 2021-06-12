from threading import Thread


class MyThread(Thread):
    def run(self):
        for i in range(100):
            print(f'{i} in thread 2')


if __name__ == '__main__':
    t = MyThread()
    t.start()

    for i in range(100):
        print(f'{i} in main thread')
        
