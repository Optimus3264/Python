arr=[10,25,34,12,15,11]
reversed_arr=[]

for i in range(len(arr)-1,-1,-1):
    reversed_arr.append(arr[i])

print('reversed array :',reversed_arr)
