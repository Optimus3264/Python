a =10
if a>8 :
    print("a is greater than 8")

num=int(input('enter a number'))
if num%2==0:
    print('even')
else:
    print('odd')

x=int(input('enter 1st number:'))
y=int(input('enter 2nd number:'))
z=int(input('enter 3rd number:'))

if x>y and x<z :
    print(f'largest number{x}:')
elif y>z:
    print(f'largest number{y}:')
else:
    print(f'largest number{z}:')

a= float(input('enter a number:'))
if a>0:
    print('positive')
elif a<0:
    print('negative')
else:
    print('zero')

#90+=A, 89-80 =B,79-70=C,69-60=D,<60=E
a=int(input('enter a mark:'))
if a>90:
    print('grade A')
elif a>89 and a<80:
    print('grade B')
elif a>79 and a<70:
    print('grade C')
elif a>69 and a<=60:
    print('grade D')
else:
    print('grade E')


     


