def is_perfect(number):
    # Find the sum of proper divisors of the number
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    
    # Check if the sum of divisors equals the number
    if divisors_sum == number:
        return True
    else:
        return False

# Example usage
number = 6
if is_perfect(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")
