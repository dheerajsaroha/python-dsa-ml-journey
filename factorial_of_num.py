def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return  
    fact = 1
    while n > 0:
        fact = n * fact
        n -= 1
    return fact
print(factorial(5))