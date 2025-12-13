num=input('enter a number:')

digit_sum=sum(int(digit) for digit in num if digit.isdigit())
print('sum of digit:',digit_sum)