
#1.Basic usage
name = 'Kathy'
age = '24'
message = f'Hello, my name is {name} and I am {age} years old'
print(message)  # Output: Hello, my name is Kathy and I am 24 years old.

#2. Expressions inside F-strings
x = 5
y = 10
result = f"the sum of {x} and {y} is {x+y}."
print(result) # output : the sum of 5 and 10 is 15

#3. Formatting numbers in F'strings
pi = 3.14159
message = f'the value of pi is approximately {pi: .2f}'
print(message)  # output: the value of pi is approximately 3.14

#4. Using f-string with dictionaries
person = {"name": "bob" , "age": 30}
message = f"{person['name']} is {person['age']} year old"
print(message) #output : bob is 30 year old

name='rushikesh'
age='25'
sport='football'
message = f'hello,my name is {name} ,i am {age} year old and my i want to play {sport}'
print(message)