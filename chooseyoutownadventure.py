name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer_2 = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
    if answer_2 == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer_2 == "walk":
        print("You walked for many miles and ran out of water. You lose.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer_3 = input("You found a dead end. Would you like to go back or explore the jungle? back to go back and explore to explore the jungle: ").lower()
    if answer_3 == "back":
        q3 = input("Would you like to swim across the river? yes to swim across and no to quit: ").lower()
        if q3 == "yes":
            print("You swam across and were eaten by an alligator.")
        elif q3 == "no":
            print("You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer_3 == "explore":
        q4 = input("You were walking through the jungle and were bitten by a mosquito. Did you bring repellent? yes to use it and no to did not bring: ").lower()
        if q4 == "yes":
            q5 = input("Nice! Do you want to continue your adventure? yes to continue and no to quit ").lower()
            if q5 == "yes":
                print("You walked for hours and could not find the exit. You lose.")
            elif q5 == "no":
                print("You lose.")
            else:
                print("Not a valid option. You lose.")
        elif q4 == "no":
            print("The mosquito was poisonous. You lose.")
        else:
            print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")