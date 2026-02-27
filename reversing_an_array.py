arr = [2,4,6,8,10]

new_arr = arr
rev_arr = []
len_arr=len(new_arr)
while len_arr > 0:
    rev_arr.append(new_arr[len_arr-1])
    len_arr -= 1
print(rev_arr)


    

