"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

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


class ExtensionGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = self.create_paddle(paddle_width, paddle_height)
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = self.create_ball(ball_radius)
        self.window.add(self.ball, x=self.window.width / 2 - ball_radius, y=self.window.height / 2 - ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.is_click = False
        onmouseclicked(self.start_game)
        onmousemoved(self.paddle_move)

        # restart the game
        self.restart_game = False    # To check the restart_the_game() has done
        self.restart_img = GImage("restart.png")

        # Draw bricks
        self.draw_bricks()

        # Score
        self.__score = 0
        self.score_label = self.create_score()
        self.window.add(self.score_label, x=0, y=self.window.height)

        # Life
        self.blood1 = GImage("blood.jpeg")
        self.blood2 = GImage("blood.jpeg")
        self.blood3 = GImage("blood.jpeg")
        self.window.add(self.blood1, x=window_width - self.blood1.width, y=window_height - self.blood1.height)
        self.window.add(self.blood2, x=window_width - self.blood1.width*2, y=window_height - self.blood1.height)
        self.window.add(self.blood3, x=window_width - self.blood1.width*3, y=window_height - self.blood1.height)

    @staticmethod
    def create_ball(ball_radius):
        ball = GOval(ball_radius * 2, ball_radius * 2)
        ball.filled = True
        return ball

    @staticmethod
    def create_paddle(paddle_width, paddle_height):
        paddle = GRect(width=paddle_width, height=paddle_height)
        paddle.filled = True
        return paddle

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

    def create_score(self):
        score_label = GLabel(f"Score：{self.__score}")
        score_label.font = "-25"
        return score_label

    def set_score(self, num):
        self.__score += num
        self.score_label.text = f"Score：{self.__score}"

    def get_score(self):
        return self.__score

    def reset_lives(self, num):
        if num == 2:
            self.window.remove(self.blood3)
        elif num == 1:
            self.window.remove(self.blood2)
        else:
            self.window.remove(self.blood1)

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

    def set_mes(self, msg):
        label = GLabel(msg, self.window.width)
        label.font = "-60"
        label.color = "red"
        self.window.add(label, x=(self.window.width-label.width)/2, y=(self.window.height+label.height)/2)

    def record_page(self, rank_list):
        self.restart_game = False
        self.window.clear()
        self.window.add(self.restart_img, x=self.window.width-self.restart_img.width,
                        y=self.window.height-self.restart_img.height)
        title = GLabel("Top 10 Record：")
        title.font = "Courier-45-bold-italic"
        title.color = "red"
        self.window.add(title, x=(self.window.width-title.width)/2, y=title.height+20)
        for i in range(1, 3):
            line = GLine(title.x, title.y+5*i, title.width, title.y+5*i)
            line.color = "red"
            self.window.add(line)

        position_y = 65
        for i in range(1, 11):
            if i <= len(rank_list):
                rank = GLabel(f"No.{i}：{rank_list[i-1]}")
            else:
                rank = GLabel(f"No.{i}：")
            rank.font = "Courier-30-bold"
            self.window.add(rank, x=title.x+30, y=title.y+position_y)
            position_y += (rank.height + 20)

        onmouseclicked(self.restart_the_game)
        while True:
            pause(10)
            if self.restart_game:    # Ensure the UI had renewed done, and User code can continue
                break

    def restart_the_game(self, mouse):
        obj = self.window.get_object_at(mouse.x, mouse.y)
        if obj is self.restart_img:
            self.window.clear()

            self.paddle = self.create_paddle(PADDLE_WIDTH, PADDLE_HEIGHT)
            self.ball = self.create_ball(BALL_RADIUS)
            self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                            y=self.window.height - PADDLE_OFFSET - self.paddle.height)
            self.window.add(self.ball, x=(self.window.width-self.ball.width)/2,
                            y=(self.window.height-self.ball.height)/2)
            # Bricks
            self.draw_bricks()
            # Score
            self.__score = 0
            self.score_label = self.create_score()
            self.window.add(self.score_label, x=0, y=self.window.height)
            # Blood Img
            self.blood1 = GImage("blood.jpeg")
            self.blood2 = GImage("blood.jpeg")
            self.blood3 = GImage("blood.jpeg")
            self.window.add(self.blood1, x=self.window.width - self.blood1.width,
                            y=self.window.height - self.blood1.height)
            self.window.add(self.blood2, x=self.window.width - self.blood1.width*2,
                            y=self.window.height - self.blood1.height)
            self.window.add(self.blood3, x=self.window.width - self.blood1.width*3,
                            y=self.window.height - self.blood1.height)
            onmouseclicked(self.start_game)
            self.restart_game = True
