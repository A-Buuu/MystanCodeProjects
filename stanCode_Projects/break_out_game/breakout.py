"""
File: breakout.py
Name: A-Bu
-------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The basic version of Breakout Project.
User need to break the bricks by ball,
and catch the ball by paddle when it falls down.
If the ball fall out the window, the lives will decrease,
and user has only 3 lives to play the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    lives = NUM_LIVES
    num_bricks = BreakoutGraphics.get_num_bricks()
    graphics = BreakoutGraphics()
    window = graphics.window
    paddle = graphics.paddle

    # Add the animation loop here!
    while lives > 0 and num_bricks > 0:
        # Pause
        pause(FRAME_RATE)

        if graphics.is_click:
            ball = graphics.ball
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            while num_bricks > 0:
                # Update
                ball.move(dx, dy)

                # Check Collision of Object (Check 4 points of the ball)
                for i in (0, ball.height):    # Two bottom points of the ball
                    collision = False
                    for j in (0, ball.width):    # Two upper points of the ball
                        maybe_obj = window.get_object_at(ball.x + j, ball.y + i)
                        if maybe_obj is not None:
                            collision = True
                            if maybe_obj == paddle:
                                if dy > 0:
                                    dy = -dy
                            else:
                                window.remove(maybe_obj)
                                num_bricks -= 1
                                dy = -dy
                            break
                    if collision:    # To break the "i" loop
                        break

                # Check Collision of Window
                if ball.x <= 0 or ball.x + ball.width > window.width:
                    dx = -dx
                if ball.y <= 0:
                    dy = -dy
                if ball.y + ball.height > window.height:
                    lives -= 1
                    graphics.reset_ball()
                    graphics.is_click = False
                    break

                # Pause
                pause(FRAME_RATE)


if __name__ == '__main__':
    main()
