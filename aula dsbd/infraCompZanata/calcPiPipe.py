import time
from multiprocessing import Process, Pipe

times = 8
a, b = Pipe()

def pi_naive(start, end, step, conn):
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    conn.send(sum)


if __name__ == "__main__":
    num_steps = 100000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    procs = []

    tic = time.time() # Tempo Inicial
    proc_size = num_steps//times

    for i in range(times):
        start = i * proc_size
        end = ((i  + 1) * proc_size) - 1

        p = Process(target = pi_naive, args = (start, end, step, b, ))
        procs.append(p)

    for i in range(times):
        procs[i].start()

    for i in range(times):
        procs[i].join()

    total = 0
    for i in range(times):
        soma = a.recv()
        total = total + soma
    print('Total: %.20f ' %(step * total))
    
    toc = time.time() # Tempo Final
    print ("Tempo: %.8f s" %(toc-tic)) 