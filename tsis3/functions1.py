import random
from itertools import permutations

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (2 * chickens) + (4 * rabbits) == numlegs:
            return chickens, rabbits
    return "No solution found"

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def string_permutations(s):
    return [''.join(perm) for perm in permutations(s)]

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

def sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)

def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def histogram(numbers):
    for num in numbers:
        print('*' * num)

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

# Пример использования функций:
print(grams_to_ounces(100))
print(fahrenheit_to_celsius(75))
print(solve(35, 94))
print(filter_prime([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(string_permutations("abc"))
print(reverse_words("We are ready"))
print(has_33([1, 3, 3]))
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(sphere_volume(5))
print(unique_elements([1, 2, 2, 3, 3, 4, 5, 5]))
print(is_palindrome("madam"))
histogram([4, 9, 7])
guess_the_number()
