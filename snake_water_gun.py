import random as r
while True:
    random_integer = r.randint(1,3)
    computer_choice = "Snake" if random_integer == 1 else "Water" if random_integer == 2 else "Gun"
    print("\n\n\n1 for Snake")
    print("2 for Water")
    print("3 for Gun")
    print("4 for exit")
    ch = int(input("Enter your choice: "))
    print("\n\n\n")
    if ch == 1:
        print("You chooses Snake")
        print(f"Computer chooses {computer_choice}")
        if random_integer == 1:
            print("Draw")
        elif random_integer == 2:
            print("You Win!!!!!")
        else:
            print("Loose")
    elif ch == 2:
        print("You chooses Water")
        print(f"Computer chooses {computer_choice}")
        if random_integer == 1:
            print("Loose")
        elif random_integer == 2:
            print("Draw")
        else:
            print("Win!!!!!")
    elif ch == 3:
        print("You chooses Gun")
        print(f"Computer chooses {computer_choice}")
        if random_integer == 1:
            print("You Win!!!!!")
        elif random_integer == 2:
            print("Loose")
        else:
            print("Draw")
    elif ch == 4:
        print("Exiting the game...")
        break
    else:
        print("Invalid Input Enter between 1-4")
