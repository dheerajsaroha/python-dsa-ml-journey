# digit = input()
# def sum_of_digits(digit):
#     sum = 0
#     for i in digit:
#         sum += int(i)
#     return sum
# print(sum_of_digits(digit))

digit = int(input())
def sum_of_digit(digit):
    sum = 0
    rem = 0
    while digit > 0:
        rem = digit%10
        digit = digit//10
        sum += rem
    return sum

print(sum_of_digit(digit))
