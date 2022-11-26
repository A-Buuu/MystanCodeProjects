"""
File: boggle.py
Name: A-Bu
----------------------------------------
This program recursively finds all the word(s)
from the square letter platter input by user.

For example, if you correctly implement this program,
you should see the number of words from platter below:

	* 1 row of letters: f y c l
	* 2 row of letters: i o m g
	* 3 row of letters: o r i l
	* 4 row of letters: h j h u

	--> 21 words in total
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic = {}
SIZE = 4


def main():
	"""
	1. Print the Welcome.
	2. Let user enter the letters, and store in the platter(dictionary).
	3. Judgment:
		3-1. If the input is invalid, end the program.
		3-2. If the input is valid, continue to find the words.
	"""
	platter = {}
	print(f"It is {SIZE} x {SIZE} platter!")
	valid_input = set_up_the_platter(platter)

	if valid_input:
		start = time.time()
		word_search(platter)
		end = time.time()

		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')
	else:
		print("Illegal input")


def set_up_the_platter(platter):
	"""
	To establish the SIZE * SIZE square letter platter, and achieve case-insensitive.

	:param platter: dic, to store the letters from user
	:return: bool, the platter had set up successfully or not
	"""
	key_number = 0
	while key_number < SIZE:
		row = list(ele.lower() for ele in input(f"{key_number + 1} row of letters: ").split())
		if len(row) == SIZE:
			for ch in row:
				if len(ch) != 1:    # avoid user inputting double or more letters
					return False
				elif not ch.isalpha():    # avoid user inputting other sign
					return False
		else:
			return False

		platter[key_number] = row
		key_number += 1
	return True


def word_search(platter):
	"""
	Check the words entered by the user to find out if there are any reorganized words.

	1. Read the dictionary: search the words which length is longer than 4 in FILE.
	2. Create list: after word_search_helper process, the answer will be attached to this list.
	3. Call helper: the function that actually finds the words recursively.

	:param platter: dic, stored the letters user entered
	"""
	read_dictionary()

	ans_list = []
	for x in range(SIZE):
		for j in range(SIZE):
			word_search_helper(platter, ans_list, "", x, j, [], False)

	print(f"There are {len(ans_list)} words in total.")


def word_search_helper(platter, ans_list, current_s, row, column, path, to_check):
	"""
	The main purpose is to search the word in the platter.

	Basic Framework
		1. Recursive Case
			1-1. choose     : Insert a letter at the end, and put its position into the path.
			1-2. explore    : Recursion.
			1-3. un-choose  : Remove a letter from the end, and its position from the path.
		2. Base Case
			2-1. When the length of the word is >= 4.
			2-2. current_s is in dic and not in the answer before it is printed (to avoid duplicate answers).

	:param platter: dic, stored the letters user entered
	:param ans_list: list[str], record the word that find in platter
	:param current_s: string, the concatenation string currently.
	:param row: int, the key of the platter(dic)
	:param column: int, the index of the value of the platter(dic)
	:param path: list[tuple], stored the position of the letter in platter that had been chosen
	:param to_check: bool, check the condition which len(current_s) >= 4 matched or not
	"""
	# Base case
	if to_check:
		if current_s not in ans_list:
			if current_s in dic[current_s[0]]:
				ans_list.append(current_s)
				print(f"Found \"{current_s}\"")
	else:
		# choose
		current_s += platter[row][column]
		if len(current_s) >= 4:
			to_check = True
		path.append((row, column))

		# Explore
		if has_prefix(current_s):
			# 8 neighborly letters
			for i in range(-1, 2, 1):
				for j in range(-1, 2, 1):
					new_row = row + i
					new_column = column + j
					if 0 <= new_row < SIZE and 0 <= new_column < SIZE and (new_row, new_column) not in path:
						word_search_helper(platter, ans_list, current_s, new_row, new_column, path, to_check)

						# Keep find next letter when answer word had been searched.
						if has_prefix(current_s + platter[new_row][new_column]):
							to_check = False
							word_search_helper(platter, ans_list, current_s, new_row, new_column, path, to_check)
		# Un-choose
		current_s = current_s[:-1]
		path.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python dictionary
	"""
	with open(FILE, "r") as f:
		for word in f:
			if len(word.strip()) >= 4:
				if word[0] in dic:
					dic[word[0]].append(word.strip())
				else:
					dic[word[0]] = [word.strip()]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
