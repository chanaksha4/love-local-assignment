def length_of_last_word(s):
    # Split the string into words
    words = s.split()

    # Check if there are any words in the string
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])

#for user input
user_input = input("Enter a string: ")
result = length_of_last_word(user_input)

print(f"The length of the last word is: {result}")


# Example usage:
s1 = "Hello World"
print(length_of_last_word(s1))  # Output: 5

s2 = "   fly me   to   the moon  "
print(length_of_last_word(s2))  # Output: 4

s3 = "luffy is still joyboy"
print(length_of_last_word(s3))  # Output: 6

