string = "hello"
string = list(string)
rev_arr = []
len_arr=len(string)
while len_arr > 0:
    rev_arr.append(string[len_arr-1])
    len_arr -= 1
rev_str = "".join(rev_arr)
print(rev_str)

