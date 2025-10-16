# concatenation (combing string):
str1= 'Hello'
str2= 'world'

result= str1+ " " +str2
print(result)

#repitation:
str3="rushikesh"
repeated =str3 *3
print(repeated)

#indexing
str4='Python'
print(str4[1])
print(str4[-1])

#slicing
str5="rushikesh patil"
print(str5[0:5])
print(str5[10:])
print(str5[:9])

#length
str6="samsung"
print(len(str6))

#changing case
str7= 'Hello'
print(str7.upper())
print(str7.capitalize())
print(str7.lower())
print(str7.title())

#finding substring
str8='Hello welcome'
print(str8.find('welcome'))
print(str8.find("bhushan"))

#replace substring
str9="Hello Rahul"
new_str=str9.replace('Rahul','welcome')
print(new_str)

#trimming
str10='hello welcome'
print(str10.strip())