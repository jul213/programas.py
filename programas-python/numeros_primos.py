def es_primo(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos(hasta):
    primos = []
    for i in range(2, hasta +1):
        if es_primo(n):
            primos.append(i)
    return numeros_primos
        