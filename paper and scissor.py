import sys

user1 = input("What's your name?")
user2 = input("And your name?")
u1 = input(" do yo want to choose rock, paper or scissors?")
u2 = input("do you want to choose rock, paper or scissors?")

if u1 == u2:
    print("It's a tie!")
elif u1 == 'rock':
        if u2 == 'scissors':
            print("Rock wins!")
        else:
            print("Paper wins!")
elif u1 == 'scissors':
        if u2 == 'paper':
            print("Scissors win!")
        else:
            print("Rock wins!")
elif u1 == 'paper':
        if u2 == 'rock':
            print("Paper wins!")
        else:
            print("Scissors win!")
else:
       print("Invalid input")