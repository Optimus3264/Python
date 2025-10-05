a = int(input('enter 1st number:'))
b = int(input('enter 2nd number:'))
c = int(input('enter 3rd number:'))

if a>b and a>c:
    print(f'largest number is {a}')
elif b>c:
    print(f'largest number is {b}')
else:
    print(f'largest number is {c}')