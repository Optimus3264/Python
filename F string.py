# 1.Basic usage
name='Alice'
age='25'
message=f'My name is {name} and I am {age} years old'

print(message)


# 2. Expressions inside F string
x=5
y=10
result=f'The sum of {x} and {y} is {x+y}'

print(result)


# 3.Formatting numbers in F string
pi=3.14159
message=f'Approximate value of pi is{pi: .2f}'

print(message)


# 4.Using F string with Dictionaries
person={'name':'Bob' , 'age': '30'}
message=f"{person ['name']} is {person['age']} years old"

print(message)
