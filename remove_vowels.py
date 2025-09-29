def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in s if char not in vowels])
    return result

# Input
input_str = input("Enter a string: ")

# Remove vowels
output_str = remove_vowels(input_str)

print("String after removing vowels:", output_str)