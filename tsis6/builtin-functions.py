# #1
# import math

# def multiply_list(numbers):
#     if not numbers:
#         return None 

#     result = math.prod(numbers)
#     return result

# numbers = [2, 3, 4, 5]
# result = multiply_list(numbers)
# print("Result of multiplying all numbers in the list:", result)

# #2
# def count_upper_lower(string):
#     upper_count = 0
#     lower_count = 0

#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1

#     return upper_count, lower_count

# input_string = input("Enter a string: ")
# upper, lower = count_upper_lower(input_string)

# print("Number of uppercase letters:", upper)
# print("Number of lowercase letters:", lower)

# #3
# def is_palindrome(s):
    
#     s = ''.join(char.lower() for char in s if char.isalnum())
    
    
#     return s == s[::-1]

# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#4
import time
import math

def square_root(number):
    return math.sqrt(number)

def invoke_square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = square_root(number)
    return result

number = 16
milliseconds = 2000  

print(f"Invoking square root function after {milliseconds} milliseconds...")
result = invoke_square_root_after_milliseconds(number, milliseconds)
print(f"Square root of {number} is:", result)



