import random


def cards():
    """This function is the game 'BlackJack'"""
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_list = []
    computer_list = []

    for i in range(2):
        value = random.choice(cards_list)
        user_list.append(value)
        value = random.choice(cards_list)
        computer_list.append(value)

    total = sum(user_list)
    print(f"Your cards are {user_list}, current score is {total}:")
    print("Dealer's first card is {}".format(computer_list[0]))
    check = ""
    while check.lower() != "no" and total <= 21:
        check = input("Would you like to draw another card, select 'yes' or 'no': ")
        if check.lower() != "no":
            value = random.choice(cards_list)
            user_list.append(value)
            total = sum(user_list)
            if total > 21 and 11 in user_list:
                user_list.remove(11)
                user_list.append(1)
                total = sum(user_list)
                
            print("Your cards now are ", user_list)
    if total > 21:
        print("\nDealer Win:")
        return

    computer_total = sum(computer_list)
    while computer_total < 18:
        value = random.choice(cards_list)
        computer_list.append(value)
        computer_total = sum(computer_list)
        if computer_total > 21 and 11 in computer_list:
            computer_list.remove(11)
            computer_list.append(1)

    print("Your cards are ", user_list)
    print("Computer cards are ", computer_list)

    if computer_total > 21:
        return print("\nYou Win:")

    if total > computer_total:
        return print("\nYou Win:")
    elif total == computer_total:
        return print("\nGame Draw")
    else:
        return print("\nDealer Win:")



cards()
