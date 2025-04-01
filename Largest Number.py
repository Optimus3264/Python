a=int(input('Enter 1st Number:'))
b=int(input('Enter 2nd Number:'))
c=int(input('Enter 3rd Number:'))

if a>b and a>c:
    print(f'largest numnber is {a}')
elif b>c:
    print(f'largest number is {b}')
else:
    print(f'largest number is {c}')