str1='Hello '
str2='World !'

#1. Concatenation(combining strings)
result=str1+' '+str2
print(result) # output: Hello World !


#2. Repeatation
repeat=str1 *3
print(repeat) # output: Hello Hello Hello


#3. Indexing(accessing a character in a string)
str3='Python'
print(str3[0]) # 1st character from left
print(str3[-2]) # 2nd character from right/end


#4. Slicing(extracting portion of a string)
str4='Hello World'
print(str4[0:5]) #output 'Hello' (str4[start index:2nd last index])(does not include end index)
print(str4[7:]) #output 'orld' (str4[start index:till end of string])
print(str4[:4]) #output 'Hell' (str4[start index:2nd last index])(does not include end index)


#5. Length(length of string)
print(len(str4)) #output 11 (number of characters in a string)


#6. Changing case(converting a string to a upper/lower case)
str5='bHuShaN'
print(str5.upper()) #output:BHUSHAN (all upper case)
print(str5.lower()) #output:bhushan (all lower case)
print(str5.title()) #output:Bhushan (1st character upper case)


#7. Finding Substrings (searching for substrings in a string)
str6='I am happy'
print(str6.find('h'))  #output:5 (index of character'h')
print(str6.find('am'))  #output:2 (index of word 'am')
print(str6.find('sad'))  #output:-1 (not found=word is not there)
print(str6.find('Y'))  #output:-1 (not found=Python is case sensitive; 'Y' is not there in happy)


#8. Replacing substrings
str7='I Jump'
new_str=str7.replace('Jump','Run') #replacing string 'Jump' with 'Run' ('current string','new string')
print(new_str)  #output: I Run


#9. Trimming Whitespaces(removing unnecessary blanks)
str8='I    wake up early     '
print(str8.strip())  # output: I    wake up early(removes blank spaces AFTER END of the string; NOT WITHIN the string)
