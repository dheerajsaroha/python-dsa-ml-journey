import math

n = 9
res = []


while n > 1:
    res.append(n)
    if n % 2 == 0:
        # If even: floor(sqrt(n))
        n = math.floor(math.sqrt(n))
    else:
        # If odd: floor(sqrt(n)^3) = floor(n^1.5)
        n = math.floor(pow(n, 1.5))

res.append(n) # Append the final 1
print(res)