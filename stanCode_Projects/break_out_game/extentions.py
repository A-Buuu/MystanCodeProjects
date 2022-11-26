"""
File: breakout.py
Name: A-Bu
-------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The extension version of Breakout Project.
Based on the basic version, there are some additional items.
1. Show the remained lives
2. The score system: one brick get 5 points
3. Leaderboard: Show up the top 10 record
4. Restart icon to let user play again
"""

from campy.gui.events.timer import pause
from extensiongraphics import ExtensionGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
record_list = []


def main():
    graphics = ExtensionGraphics()
    window = graphics.window
    while True:
        # Pause
        pause(FRAME_RATE)

        lives = NUM_LIVES
        num_bricks = ExtensionGraphics.get_num_bricks()
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
                                elif maybe_obj == graphics.score_label or maybe_obj == graphics.blood1 \
                                        or maybe_obj == graphics.blood2 or maybe_obj == graphics.blood3:
                                    pass
                                else:
                                    window.remove(maybe_obj)
                                    graphics.set_score(5)
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
                        graphics.reset_lives(lives)
                        graphics.reset_ball()
                        graphics.is_click = False
                        break

                    # Pause
                    pause(FRAME_RATE)
        # The End
        if lives > 0:
            graphics.set_mes("Congratulations! You win!")
        else:
            graphics.set_mes("GAME OVER!!!")
        pause(1000)     # Show the message for 1 second

        # Record the score
        record(graphics.get_score())
        graphics.record_page(record_list)


def record(score):
    """
    To add the score in the list
    :param score: int, the score user get in this run
    """
    record_list.append(score)
    record_list.sort(reverse=True)
    if len(record_list) > 10:
        record_list.pop()


if __name__ == '__main__':
    main()
