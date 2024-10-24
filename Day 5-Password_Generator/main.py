import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 
           'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = [  '!', '#', '$', '%', '^', '&', '*', '(', ')', '-',
             '_', '=', '+', '{', '}', '[', ']', '|', ':', ';',
             '<', '>', '.', '?', '/',]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?"))
num_symbols = int(input("How many symbols would you like in your password?"))
num_numbers = int(input("How many numbers would you like in your password?"))

password = []


#GENERATE RANDOM LETTERS
for nums in range(num_letters):
    password.append(random.choice(letters))


#GENERATE RANDOM SYMBOLS
for nums in range(num_symbols):
    password.append(random.choice(symbols))


#GENERATE RANDOM NUMBERS
for nums in range(num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

#PRINT RANDOMLY GENERATED PASSWORD
print(''.join(password))







