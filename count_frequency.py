arr=[1,2,2,3,4,3,5,5,6]
frequency={}

for element in arr:
    if element in frequency:
        frequency [element] +=1
    else:
        frequency [element] = 1
print('frequency of each element:')

for key,values in frequency.items():
    print(f"{key}:{values}")