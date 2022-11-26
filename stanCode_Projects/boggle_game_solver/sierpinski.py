"""
File: sierpinski.py
Name: A-Bu
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Prints the 6 order Sierpinski triangle on GWindow.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the current order number
	:param length: int, the length of the triangle
	:param upper_left_x: int, the upper left x-coordinated of the triangle
	:param upper_left_y: int, the upper left y-coordinated of the triangle
	"""
	if order == 0:
		pass
	else:
		draw_triangle(length, upper_left_x, upper_left_y)
		# Upper Left Triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# Upper Right Triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length/2, upper_left_y)
		# Bottom Triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x + (length/2)*0.5, upper_left_y+(length/2)*0.866)


def draw_triangle(length, upper_left_x, upper_left_y):
	"""
	:param length: int, the length of the triangle
	:param upper_left_x: int, the upper left x-coordinated of the triangle
	:param upper_left_y: int, the upper left y-coordinated of the triangle
	"""
	line = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
	window.add(line)
	# pause(600)
	line = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
	window.add(line)
	# pause(600)
	line = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
	window.add(line)
	# pause(600)


if __name__ == '__main__':
	main()
