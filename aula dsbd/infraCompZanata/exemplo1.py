from multiprocessing import Process

def f(name):
    print('Hello, sou ', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob filho', )) #argumento vazio indica que não tem mais argumentos pra receber
    p.start()
    p.join()