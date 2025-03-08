
def number_to_letter(num):
    if 1 <= num <= 26:
        return chr(ord('a') + num - 1)
    else:
        return "Invalid input. Number should be between 1 and 26."

# Examples
print(number_to_letter(1))
print(number_to_letter(3))
print(number_to_letter(26))
print(number_to_letter(27))
