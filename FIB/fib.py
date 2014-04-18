# algo taken from:
# http://recologia.com.br/2013/02/rosalind-rabbits-and-recurrence-relations-fib/

results = {0: 0, 1: 1, 2: 1}

def fib(n,k):
    if n in results:
        return results[n]
    else:
        results[n] = fib(n-1,k) + k*fib(n-2,k)
        return results[n]

n = 30
k = 4
fib(n, k)
print results[n]
