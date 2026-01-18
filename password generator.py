import random

letters = "abcde12345"

length = int(input("Enter length: "))

pwd = ""

for i in range(length):
    pwd = pwd + random.choice(letters)

print("Password:", pwd)