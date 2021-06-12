from concurrent.futures import ThreadPoolExecutor

def fn(name):
    for i in range(100):
        print(f'{i} in {name}')

if __name__ == '__main__':	
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn,name=f'thread{i}')
        
    print('done.')