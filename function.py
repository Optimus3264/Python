#def greet (name):
 #   print(f'Hello, {name}!')

#greet('Adhiraj')

#def add_number(a,b):
 #   return a+b
#result = add_number(10,5)
#print(result)

#def even_odd(number):
   # if number%2==0:
   #   return f'{number} is even'
  #  else:
 #     return f'{number} is odd'
#print(even_odd(50))
  
#def find_max(a,b,c):
 #  return max(a,b,c)
#print(find_max(10,50,60))

def fractional(n):
   result = 1
   for i in range(1,n+1):
      result *=i
      return result
print(fractional(5))

#def is_palindrome(word):
 #  return word == ['::-1']
#print(is_palindrome("madam"))

#def multiplication_table(num):
 #   for i in range(2,6):
  #    print(f"{num}*i ={num*i}")
#multiplication_table(5)

#def is_prime(number):
 #   if number  <=1:
  #      return false
   # for i in range(2, int(number **0.5)+1):
    #    if number % i==0:
     #       return False
      #  return True
#print(is_prime(7))


#def reverse_list(Ist):
 #   return Ist[::-1]
#my_list=[1,2,3,4]
#print (reverse_list(my_list))

def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text:
        for char in vowels:
            count +=1
    return count
print(count_vowels('Hello world'))


