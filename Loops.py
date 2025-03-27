#Basic structure
#for item in sequence
#doing something with item

#1. Loop through list

fruits=['Apple','Banana','Cherry']
for fruit in fruits:
    print(fruit)


#2. Loop using range
for i in range(5):
    print(i)


#3. Loop with range (start,stop,step)
for i in range(0,10,2):
    print(i)


#4. Loop through character in string
word='HELLO'
for letter in word:
    print(letter)


#5. Nested For Loops
for i in range(2):
    for j in range(3):
        print(f'i={i} , j={j}')