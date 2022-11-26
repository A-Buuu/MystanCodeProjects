"""
File: babygraphics.py
Name: A-Bu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return int(GRAPH_MARGIN_SIZE + ((width - GRAPH_MARGIN_SIZE*2)/len(YEARS))*year_index)


def get_y_coordinate(height, year_index, dic):
    """
    Given the height of the canvas and the index of the current year
    in the YEARS list, returns the y coordinate of the point
    associated with that baby-name's rank.

    Input:
        height (int): The height of the canvas
        year_index (int): The index where the current year is in the YEARS list
        dic (dict): Dictionary holding rank and year from the specific baby
    Returns:
        y_coordinate (int): The y coordinate of the point
                            associated with that baby-name's rank..
    """
    if str(YEARS[year_index]) in dic:
        rank = int(dic[str(YEARS[year_index])])
        return int(GRAPH_MARGIN_SIZE + ((height - GRAPH_MARGIN_SIZE*2)/1000)*(rank-1))
    else:
        return height - GRAPH_MARGIN_SIZE    # The rank is out of 1000, no data in that year


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for year_index in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[year_index],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for i in range(len(lookup_names)):
        # if lookup_names[i] in name_data:    # lookup_names 已自動過濾不存在的名字
        name = lookup_names[i]    # For abbr and easy to see

        # Create Line
        for year_index in range(len(YEARS)-1):
            x1 = get_x_coordinate(CANVAS_WIDTH, year_index)
            y1 = get_y_coordinate(CANVAS_HEIGHT, year_index, name_data[name])
            x2 = get_x_coordinate(CANVAS_WIDTH, year_index + 1)
            y2 = get_y_coordinate(CANVAS_HEIGHT, year_index + 1, name_data[name])
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[i % (len(COLORS))])

            # Create Text of Name and Rank
            draw_names_text(canvas, x1, y1, name, i, name_data, year_index)
            # Create the text of the last point
            if year_index == len(YEARS) - 2:
                draw_names_text(canvas, x2, y2, name, i, name_data, year_index + 1)


def draw_names_text(canvas, x, y, name, color_index, name_data, year_index):
    """
    Create the text of the name and rank.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing
        x (int): The x coordinate of the text with the current year
        y (int): The y coordinate of the text with the current year
        name (str): The baby name
        color_index (int): The index where the current color is in the COLORS list
        name_data (dict): Dictionary holding baby name data
        year_index (int): The index where the current year is in the YEARS list
    """
    if str(YEARS[year_index]) in name_data[name]:
        canvas.create_text(x + TEXT_DX, y, text=f"{name} {name_data[name][str(YEARS[year_index])]}",
                           anchor=tkinter.SW, fill=COLORS[color_index % (len(COLORS))])
    else:    # The rank is out of 1000, no data in name_data
        canvas.create_text(x + TEXT_DX, y, text=f"{name} *", anchor=tkinter.SW,
                           fill=COLORS[color_index % (len(COLORS))])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup, so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
