print('''
 ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
''')


def aution():
    attendes = {}
    repeat = ""

    while repeat.lower() != "no":
        name = input("Enter your name: ")
        bid = int(input("Enter your bid: "))
        attendes[name] = bid

        repeat = input("Are there any there bids: Yes or No")
    else:
        max_bid = 0
        winner = ""
        for key, val in attendes.items():
            if val > max_bid:
                max_bid = val
                winner = key

    print(f"{winner} won the bid with $ {max_bid}.")


aution()
