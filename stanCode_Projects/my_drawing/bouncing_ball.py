"""
File: bouncing_ball.py
Name: A-Bu
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
The ball can be started only three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

is_clicked = False  # Check if the mouse has been clicked
counter = 0  # The ball can only be started three times


def main():
    """
    Click the mouse to make the ball start falling.
    """
    onmouseclicked(click)
    create_ball()


def click(_):
    global is_clicked, counter
    if counter < 3 and not is_clicked:
        is_clicked = True
        counter += 1

        # Update the window to ready for starting
        window.clear()
        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
        ball.filled = True
        window.add(ball)

        # Falling ball
        vy = 0
        while ball.x <= window.width:
            vy += GRAVITY
            ball.move(VX, vy)
            if (ball.y + SIZE) >= window.height:
                # Avoiding the ball getting stuck on the floor and vibrating up and down.
                if vy >= 0:
                    vy = -vy*REDUCE
            pause(DELAY)

        # Update the window to beginning step
        window.clear()
        create_ball()
        is_clicked = False


def create_ball():
    """
    To create the stopped ball at (START_X, START_Y)
    that is the beginning step window shows.
    """
    init_ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    init_ball.filled = True
    window.add(init_ball)


if __name__ == "__main__":
    main()
