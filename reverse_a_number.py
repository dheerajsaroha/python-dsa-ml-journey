n= 2
rem = 0
rev = 0
while n > 0:
    rem = n%10
    print(rem)
    n = n//10
    print(n)
    rev = rev * 10 + rem
print(rev)
# print(n ** rev)

