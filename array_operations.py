arr = [2,4,6,8,10]

def arr_operation(arr):
    def sum_of_item(arr):
        result = 0
        for i in range(len(arr)):
            result += arr[i]
        return result

    def max_element(arr):
        max_item = arr[0]
        for i in arr:
            if i > max_item:
                max_item = i
        return max_item

    def reverse_arr(arr):
        new_arr = arr
        rev_arr = []
        len_arr=len(new_arr)
        while len_arr > 0:
            rev_arr.append(new_arr[len_arr-1])
            len_arr -= 1
        arr = rev_arr
        return arr
    return f"Sum = {sum_of_item(arr)}\nMax = {max_element(arr)}\nReversed = {reverse_arr(arr)}"

print(arr_operation(arr))

        