arr=[10,20,15,16,17]
element =15

if element in arr:
    print(f'{element} found at index {arr.index(element)}')
else:
    print(f'element not found in array')