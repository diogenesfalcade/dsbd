from multiprocessing import Process

def f(name, id):
    print('Hello, sou ', name, id)


if __name__ == '__main__':
    procs = []
    times = 100
    for i in range(times):
        p = Process(target=f, args=('bob filho', i, ))
        procs.append(p)
    
   
    print('hello, sou', 'bob pai')
    
    for i in range(times):
        procs[i].start()
    for i in range(times):
        procs[i].join()