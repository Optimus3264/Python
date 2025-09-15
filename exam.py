#Q1-a.even odd
num=int(input('enter a number:'))
if num%2==0:
    print('even')
else:
    print('odd')


#b. List and tuple 
#list= list is array that we can change. 
#tuple=tuple is fix array that cannot be change.

#example-
list=['apple','banana','orange']
list[0]='mango'
print(list)

tuple=('apple','banana','orange')
tuple[0]='mango'
print(tuple)

#c.fractional
def fractional(n):
    result=1
    for i in range(1,n+1):
        result *=i
        return result
print(fractional(2))


#e.how dict is different from list
#dict is list that contain a number and finding with help of giving name to them
#list is simple list that finding by there postion.

#f.vowels
def count_vowels(a):
    vowels='aeiouAEIOU'
    count=0
    for char in a:
        for char in vowels:
            count +=1
            return count
print(count_vowels('Rushikesh'))
 
#Q2. a(Minimum)
a=[10,2,15,14,13,12,16]
smallest=min(a)
for num in a:
    if num< smallest:
        smallest=num
print('minimum number is:',smallest)
#(Maximum)-
largest=max(a)
for num in a:
    if num > largest:
        largest=num
print('maximum number is :',largest)
   

#Q3.
def greet(name):
    return f'hello',{'name'}
print('hello',('alice'))
greet('alice')




