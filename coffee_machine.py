import coffee_machine_data as data


def coffee_machine(coffee_menu, resources):
    check = True
    while check:
        entered = input("What would you like? (espresso, latte, cappuccino): ")

        if entered.lower() == "off":
            print("Machine is shutting down:")
            check = False

        elif entered.lower() == "report":
            print(f"Water: {resources.get('water')}ml")
            print(f"Milk: {resources.get('milk')}ml")
            print(f"Coffee: {resources.get('coffee')}g")
            print(f"Money: ${resources.get('money')}")

        elif entered.lower() == "espresso" or entered.lower() == "latte" or entered.lower() == "cappuccino":
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25

            if entered.lower() == "espresso":
                if resources["water"] >= coffee_menu["espresso"]["ingredients"].get("water") and \
                        resources["coffee"] >= coffee_menu["espresso"]["ingredients"].get("coffee"):

                    price = coffee_menu["espresso"].get("cost")
                    if total >= price:
                        reminder = total - price
                        print("Here is ${0:.2f} in change.".format(reminder))
                        print("Here is your espresso Enjoy!")

                        resources["water"] = resources["water"] - coffee_menu["espresso"]["ingredients"].get("water")
                        resources["coffee"] = resources["coffee"] - coffee_menu["espresso"]["ingredients"].get("coffee")
                        resources["money"] = resources["money"] + price
                    else:
                        print("Sorry that's not enough money. Money refunded")
                else:
                    print("Not enough resources. Money refunded:")
                    check = False

            elif entered.lower() == "latte":
                if resources["water"] >= coffee_menu["latte"]["ingredients"].get("water") and \
                        resources["coffee"] >= coffee_menu["latte"]["ingredients"].get("coffee") and \
                        resources["milk"] >= coffee_menu["latte"]["ingredients"].get("milk"):
                    price = coffee_menu["latte"].get("cost")
                    if total >= price:
                        reminder = total - price
                        print("Here is ${0:.2f} in change.".format(reminder))
                        print("Here is your latte Enjoy!")

                        resources["water"] = resources["water"] - coffee_menu["latte"]["ingredients"].get("water")
                        resources["coffee"] = resources["coffee"] - coffee_menu["latte"]["ingredients"].get("coffee")
                        resources["milk"] = resources["milk"] - coffee_menu["latte"]["ingredients"].get("milk")
                        resources["money"] = resources["money"] + price
                    else:
                        print("Sorry that's not enough money. Money refunded")
                else:
                    print("Not enough resources. Money refunded:")
                    check = False

            else:
                if resources["water"] >= coffee_menu["cappuccino"]["ingredients"].get("water") and \
                        resources["coffee"] >= coffee_menu["cappuccino"]["ingredients"].get("coffee") and \
                        resources["milk"] >= coffee_menu["cappuccino"]["ingredients"].get("milk"):
                    price = coffee_menu["cappuccino"].get("cost")
                    if total >= price:
                        reminder = total - price
                        print("Here is ${0:.2f} in change.".format(reminder))
                        print("Here is your cappuccino Enjoy!")

                        resources["water"] = resources["water"] - coffee_menu["cappuccino"]["ingredients"].get("water")
                        resources["coffee"] = \
                            resources["coffee"] - coffee_menu["cappuccino"]["ingredients"].get("coffee")
                        resources["milk"] = resources["milk"] - coffee_menu["cappuccino"]["ingredients"].get("milk")
                        resources["money"] = resources["money"] + price
                    else:
                        print("Sorry that's not enough money. Money refunded")
                else:
                    print("Not enough resources. Money refunded:")
                    check = False
        else:
            print("Invalid coffee:")


coffee_machine(data.menu, data.resources)
