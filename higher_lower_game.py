import higher_lower_game_ascii as dic_art
import higher_lower_game_data as dic
import random


def high_low():
    print(dic_art.logo)
    total_elements = len(dic.data_dict)
    points = 0
    rand_num = random.randint(0, total_elements-1)
    data = dic.data_dict[rand_num]
    check = True
    while check:
        rand_num = random.randint(0, total_elements-1)
        data2 = dic.data_dict[rand_num]
        print(f"Compare A: {data['name']}, a {data['description']}, from {data['country']}")
        print(f"\n{dic_art.vs_sign}\n")
        print(f"Compare B: {data2['name']}, a {data2['description']}, from {data2['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer.lower() == 'a' and data["followers"] >= data2["followers"] or \
                answer.lower() == 'b' and data2["followers"] >= data["followers"]:
            points += 1
            data = data2
        else:
            check = False
    print("Wrong answer")
    print(f"\nYour scored points are : {points}")


high_low()
