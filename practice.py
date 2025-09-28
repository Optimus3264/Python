#s='hello ,how are you '
#word_count=len(s.split())

#print(word_count)

def remove_vowel(s):
    vowels='aeiouAEIOU'
    result=''.join ([char for char in s if char not in vowels])
    return result

input_str=input('enter a string')
output_str=remove_vowel(input_str)

print('string after removing vowels',output_str)
