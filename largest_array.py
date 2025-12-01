arr=[10,24,25,13,24,20]
largest=max(arr)

for num in arr:
    if num > largest:
        largest=num
print('largest number is :',largest)