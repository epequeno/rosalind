data = [line.strip("\n") for line in open("rosalind_fibo.txt", "r")]

n = int(data[0])

fibs = {0: 0, 1: 1, 2: 1}


def fibo(n):
    if n in fibs:
        return fibs[n]
    else:
        fibs[n] = fibo(n - 1) + fibo(n - 2)
        return fibs[n]

print fibo(n)
