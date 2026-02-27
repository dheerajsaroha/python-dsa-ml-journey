arr = [10,20,30,40,50]

target = 30
def linear_search(arr,target):
    flag = None
    for i in range(len(arr)):
        if arr[i] == target:
            flag = f"Found at index {i}"
            break
        else:
            flag="Not Found"
    return flag

print(linear_search(arr,target))

