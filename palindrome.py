def is_palindrome(number):
    num_str=str(number)

    return num_str==num_str[::-1]
number=121
if is_palindrome(number):
    print(f'{number} is palindrome')

else:
    print(f'{number} is not palindrome')

# when there is word then use string instead of number
