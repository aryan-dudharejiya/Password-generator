print("Hey, this is a strong password generator made by Aryan")
import random
chars = "abcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&*()_+"
length=int(input("Enter the length of your password: "))
password = ""

for a in range(length):
    password+=random.choice(chars)

print(password)

