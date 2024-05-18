import sys
def fat(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    print(res)
n = int(sys.argv[1])
fat(n)