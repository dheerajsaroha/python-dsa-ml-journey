word = "programming"
vowel = "aeiou"

count = 0
for i in word:
    i=i.lower()
    if i in vowel:
        count+=1
    else:
        count = count
print(count)