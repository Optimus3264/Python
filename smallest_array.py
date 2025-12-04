arr=[10,20,3,4,6,1,14]
smallest=min(arr)

for num in arr:
    if num < smallest:
        smallest=num
print('smallest number is :',smallest)