"""
File: anagram.py
Name: A-Bu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# dic_list = []                 # The list read from the file "dictionary.txt"
dic_list = {}


def main():
    """
    TO finds all the anagram(s) for the word input by user
    """
    # read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to guit)")
    word = input("Find anagrams for: ")
    while True:
        if word == EXIT:
            break
        else:
            start = time.time()
            read_dictionary(word)
            anagrams_list = find_anagrams(word)
            print(f"{len(anagrams_list)} anagrams: {anagrams_list}")
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')
            word = input("Find anagrams for: ")


def read_dictionary(s):
    with open(FILE, "r") as f:
        for word in f:
            # dic_list.append(word.strip())
            if len(word.strip()) == len(s):
                if word[0] not in dic_list:
                    dic_list[word[0]] = [word.strip()]
                else:
                    dic_list[word[0]].append(word.strip())


def find_anagrams(s):
    """
    :param s: str, the word input from user
    :return anagrams_list: list(str), all anagrams from searching
    """
    print("Searching...")
    anagrams_list = []
    str_list = []
    # Transfer the word(string) into a list(string)
    for i in range(len(s)):
        str_list.append(s[i].lower())    # Case-insensitive
    # Copy the elements from the original list
    new_list = str_list.copy()
    find_anagrams_helper(str_list, "", new_list, anagrams_list)
    return anagrams_list


def find_anagrams_helper(str_list, current_s, new_list, anagrams_list):
    """
    :param str_list: (list(str)), the alphabet from the original word user input
    :param current_s: str, the concatenation string currently
    :param new_list: list(str), the left alphabet currently
    :param anagrams_list: list(str), stores anagrams from recursively searching
    """
    if len(current_s) == len(str_list):
        if current_s in dic_list[current_s[0]]:
        # if current_s in dic_list:
            anagrams_list.append(current_s)
            print(f"Found: {current_s}")
            print("Searching...")
    else:
        for i in range(len(new_list)):
            # Choose
            ch = new_list[i]
            current_s += ch

            # Explore
            if 2 <= len(current_s) < len(str_list)-1:
                # Early stopping
                if not has_prefix(current_s):
                    current_s = current_s[:len(current_s) - 1]
                    continue
            # Check if the left alphabet is only one and the word startswith current_s has in anagrams_list,
            # it's redundant to check this current_s and the last alphabet.
            elif len(current_s) == len(str_list)-1:
                check_flag = False
                for word in anagrams_list:
                    if word.startswith(current_s):
                        check_flag = True
                        break
                if check_flag:
                    current_s = current_s[:len(current_s) - 1]
                    continue
            # Pop the alphabet has been chosen at this recursive.
            new_list.pop(i)
            find_anagrams_helper(str_list, current_s, new_list, anagrams_list)

            # Un-choose
            new_list.insert(i, ch)
            current_s = current_s[:len(current_s) - 1]


def has_prefix(sub_s):
    """
    :param sub_s: string, the word starts with of the sub-string
    :return: boolean, is there a word starts with the sub_s in dictionary
    """
    for word in dic_list[sub_s[0]]:
    # for word in dic_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
