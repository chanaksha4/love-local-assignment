# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n
def count_digit_one(n):
    count = 0
    factor = 1

    while factor <= n:
        # Calculate the number of times the current factor contributes to the count
        div = factor * 10
        count += (n // div) * factor + min(max(n % div - factor + 1, 0), factor)

        # Move to the next factor (ones, tens, hundreds, etc.)
        factor *= 10

    return count
# user input
user_input = int(input("Enter a non-negative integer: "))
result = count_digit_one(user_input)

print(f"The total number of digit 1 appearing in all non-negative integers less than or equal to {user_input} is: {result}")
# usage of example
n1 = 13
print(count_digit_one(n1))  # Output: 6

n2 = 0
print(count_digit_one(n2))  # Output: 0


