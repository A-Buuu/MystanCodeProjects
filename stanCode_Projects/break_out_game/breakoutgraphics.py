"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.is_click = False
        onmouseclicked(self.start_game)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.draw_bricks()

    def start_game(self, _):
        if not self.is_click:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.is_click = True

    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - PADDLE_WIDTH/2
        if self.paddle.x + PADDLE_WIDTH >= self.window.width:
            self.paddle.x = self.window.width - PADDLE_WIDTH
        elif self.paddle.x <= 0:
            self.paddle.x = 0

    def draw_bricks(self):
        position_y = BRICK_OFFSET
        for i in range(BRICK_ROWS):
            position_x = 0
            for j in range(BRICK_COLS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                if i < 2:
                    brick.fill_color = "red"
                elif i < 4:
                    brick.fill_color = "orange"
                elif i < 6:
                    brick.fill_color = "yellow"
                elif i < 8:
                    brick.fill_color = "green"
                else:
                    brick.fill_color = "blue"
                self.window.add(brick, x=position_x, y=position_y)
                position_x += (BRICK_WIDTH + BRICK_SPACING)
            position_y += (BRICK_HEIGHT + BRICK_SPACING)

    @staticmethod
    def get_num_bricks():
        return BRICK_ROWS*BRICK_COLS

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_ball(self):
        self.window.remove(self.ball)
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2,
                          x=self.window.width/2-BALL_RADIUS, y=self.window.height/2-BALL_RADIUS)
        self.ball.filled = True
        self.window.add(self.ball)
