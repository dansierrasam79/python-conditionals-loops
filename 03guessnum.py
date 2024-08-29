# guesswork
import random
choice_lst = [i for i in range(1,10)]
secret_num = random.choice(choice_lst)
print(secret_num)
guessed = False
while not guessed:
    guess_num = int(input("Enter a number between 1-10: "))
    if guess_num == secret_num:
        print("Well done!")
        guessed = True
    else:
        print("Try again!")