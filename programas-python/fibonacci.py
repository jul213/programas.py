def fibonacci(n):
    sec_fibo = []
    a,b = 0,1

    while n > len(sec_fibo):

        sec_fibo.append(a)
        a,b = b, a+b

    return sec_fibo

sas = fibonacci(20)

print(sas)
