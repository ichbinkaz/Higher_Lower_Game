
from os import system, name
from game_data import data
from art import logo
from art import vs
import random


def clear():
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def random_person():
    random_celebrity = random.sample(data, len(data))

    return random_celebrity


def higher_lower():
    is_game_over = False
    score = 0
    move = 0

    person = random_person()
    a_list = [person[0]["name"], person[0]["follower_count"], person[0]["description"], person[0]["country"]]
    b_list = [person[1]["name"], person[1]["follower_count"], person[1]["description"], person[1]["country"]]

    while not is_game_over:
        print(logo)
        print(f"Your current score is: {score}")
        print(f"Compare A: {a_list[0]}), a {a_list[2]}, from {a_list[3]}")
        print(vs)
        print(f"Against B: {b_list[0]}), a {b_list[2]}, from {b_list[3]}")

        choice = input("Who has more followers? Type 'A' or 'B' ").lower()

        if choice == 'a' and a_list[1] > b_list[1]:
            score += 1
            move += 1
            a_list = [person[0 + move]["name"], person[0 + move]["follower_count"], person[0 + move]["description"],
                      person[0 + move]["country"]]
            b_list = [person[1 + move]["name"], person[1 + move]["follower_count"], person[1 + move]["description"],
                      person[1 + move]["country"]]
            clear()

        elif choice == 'b' and b_list[1] > a_list[1]:
            score += 1
            print(f"Your current score is: {score}")
            move += 1
            a_list, b_list = b_list, a_list
            b_list = [person[1 + move]["name"], person[1 + move]["follower_count"], person[1 + move]["description"],
                      person[1 + move]["country"]]
            clear()
        else:
            clear()
            print(logo)
            print(f"You have lost, your final score is: {score}")
            is_game_over = True
    restart = input("Do you want to restart? 'Y' or 'N' ").lower()
    if restart == 'y':
        clear()
        higher_lower()


higher_lower()