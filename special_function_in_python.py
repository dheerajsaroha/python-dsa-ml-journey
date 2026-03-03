list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

# Use of zip function
zipped = zip(list1,list2)
print(list(zipped))

# Use of filter funtion
filtered = filter(lambda x: x<=2,list1)
print(list(filtered))

# Use of mapped function
mapped = map(lambda x: x * 2,list1)
print(list(mapped))