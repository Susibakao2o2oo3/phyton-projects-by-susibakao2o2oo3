from random import *
user_pass = input("Enter your password:")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]
guess = ""
countofgueses = 0
while (guess != user_pass):
    guess = ""
    countofgueses += 1
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    print(guess)
print("Your password is",guess)
print("Guesed " + str(countofgueses) + " times.")
