#Identity operators - is, is not

#******Examples with Integers******
a=10
b=10

print('a =', a)
print('b =', b)

print('a is b:', a is b)  # 'is' checks if they are same objects : TRUE

print('a is not b:', a is not b) # 'is not' check if they are diffrent objects : FALSE


#******Examples with Lists******
list1=[1,2,3]
list2=[1,2,3]
list3=list1

print('\nlist1 =', list1)
print('list2 =', list2)
print('list3 =', list3)

print('list1 is list2 :', list1 is list2) # False (same content, but different objects)
print('list1 == list2 :', list1 == list2) # True (contents are the same)
print('list1 is list3 :', list1 is list3) # True (same object in memory)
print('list1 is not list2 :', list1 is not list2) # True