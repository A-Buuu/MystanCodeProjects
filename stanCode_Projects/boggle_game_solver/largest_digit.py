"""
File: largest_digit.py
Name: A-Bu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number needed to find the largest digit
	:return: int, the largest digit in input number
	"""
	return find_largest_digit_helper(abs(n), 0)


def find_largest_digit_helper(n, maximum):
	"""
	:param n: int, the number needed to find the largest digit
	:param maximum: int, the current largest digit from previous recursive function
	:return maximum: int, the largest digit in input number
	"""
	if n % 10 == n:
		if n > maximum:
			maximum = n
		return maximum
	else:
		if n % 10 > maximum:
			maximum = n % 10
		return find_largest_digit_helper(n//10, maximum)


if __name__ == '__main__':
	main()