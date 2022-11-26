"""
File: hangman.py
Name: A-Bu
-----------------------------
This program plays hangman game.
User sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Users sees a dashed word, trying to correctly figure the un-dashed word out
    by inputting one character each round.
    """
    answer = random_word()
    input_ch = ans = ""
    n_turns = N_TURNS
    while n_turns != 0:
        ans = concatenation(answer, ans, input_ch.upper())
        if ans.isalpha():    # User guessed correctly.
            break
        draw_hung_man(n_turns)
        print("The word looks like " + ans)
        print("You have " + str(n_turns) + " wrong guesses left.")
        input_ch = input("Your guess: ")

        while not input_ch.isalpha() or len(input_ch) > 1:    # Illegal input
            print("Illegal format.")
            input_ch = input("Your guess: ")

        if input_ch.upper() in answer:
            print("You are correct!")
        else:
            print("There is no " + input_ch.upper() + "'s in the word.")
            n_turns -= 1

    if n_turns == 0:
        print("You are completely hung : (")
        draw_hung_man(n_turns)
    else:
        print("You win!!")
        draw_hung_man(-1)
    print("The word was: " + answer)


def draw_hung_man(n_turns):
    if n_turns != -1:
        print("————————————————————")
        print("|        |")
        # head
        if 0 < n_turns <= 6:
            print("|        ()")
        elif n_turns == 0:
            print("|      (X.X)")
        else:
            print("|")
        # body and hands
        if n_turns == 5:
            print("|        |")
        elif n_turns == 4:
            print("|        |\\")
        elif n_turns <= 3:
            print("|        |\\\\")
        else:
            print("|")
        if n_turns <= 5:
            print("|        |")
        else:
            print("|")
        # legs
        if n_turns == 2:
            print("|        /")
        elif n_turns <= 1:
            print("|        /\\")
        else:
            print("|")
        print("|")
        if n_turns == 0:
            print("|   You are dead!")
        else:
            print("|")
        print("————————————————————")
    else:
        print("————————————————————")
        print("|")
        print("|      (^o^)")
        print("|       \\|/")
        print("|        |")
        print("|        /\\")
        print("|")
        print("|        YA!")
        print("————————————————————")


def concatenation(answer, old_ans, alphabet):
    """
    :param answer: string, the complete word from dictionary
    :param old_ans: string, user has guessed so far
    :param alphabet: string, user inputs
    :return: string, concatenate the new input user guessed with old_ans
    """
    new_ans = ""
    if old_ans == "":
        for i in range(len(answer)):
            new_ans += "-"
    else:
        for i in range(len(answer)):
            if old_ans[i].isalpha():
                new_ans += old_ans[i]
            else:
                if alphabet == answer[i]:
                    new_ans += alphabet
                else:
                    new_ans += "-"
    return new_ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
