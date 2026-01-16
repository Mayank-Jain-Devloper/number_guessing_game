import random

user_num = int(
    input("Select the right number between 1-5⏰ {You will have only one chance!😬}: "))

comp_num = random.randint(1, 5)

if user_num == comp_num:
    print("Congratulations!!🥳")
else:
    print("Boo, You Lost.💩")
    print(f"{comp_num} was the right number🤣")
