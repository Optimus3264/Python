dict={
    'name':'rushikesh',
    'age':25,
    'gender':'male',
    'grade':'A'
}

#print(dict)

#print(dict['gender'])

#adding or update
dict['age']= 24
dict['major']='pharmacy'

#print(dict)

#delete
del dict['major']

#print(dict)

#looping 
for key ,value in dict.items():
    print(key ,":", value)