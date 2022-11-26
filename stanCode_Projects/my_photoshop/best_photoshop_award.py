"""
File: best_photoshop_award.py
Name: A-Bu
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.2

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(bg, abu):
    """
    :param bg: SimpleImage, the picture of the background of Dragon Ball
    :param abu: SimpleImage, the picture of two A-Bu
    :return: SimpleImage, the picture of two A-Bu with new background
    """
    for x in range(bg.width):
        for y in range(bg.height):
            pixel_abu = abu.get_pixel(x, y)
            avg = (pixel_abu.red + pixel_abu.blue + pixel_abu.green) // 3
            total = pixel_abu.red + pixel_abu.blue + pixel_abu.green
            if pixel_abu.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_abu.red = pixel_bg.red
                pixel_abu.blue = pixel_bg.blue
                pixel_abu.green = pixel_bg.green
    return abu


def horizontal_flip(img):
    """
    :param img: SimpleImage, the original picture of A-Bu
    :return: SimpleImage, the picture with mirrored A-Bu
    """
    b_img = SimpleImage.blank(img.width*2, img.height)
    for x in range(img.width):
        for y in range(img.height):
            colored_pixel = img.get_pixel(x, y)

            blank_pixel_1 = b_img.get_pixel(img.width + x, y)
            blank_pixel_1.red = colored_pixel.red
            blank_pixel_1.green = colored_pixel.green
            blank_pixel_1.blue = colored_pixel.blue

            blank_pixel_2 = b_img.get_pixel(img.width - 1 - x, y)
            blank_pixel_2.red = colored_pixel.red
            blank_pixel_2.green = colored_pixel.green
            blank_pixel_2.blue = colored_pixel.blue

    return b_img


def main():
    """
    創作理念：有誰一看到就知道這什麼舞步嗎？ಥ_ಥ (小心透露年紀XD
    我是超愛動漫的宅宅，剛好現在正上映七龍珠超~~★★★★★★★
    所以致敬一下這童年經典作中的經典融合術 ❤ (雖然依照設定我手指沒有貼齊會融合失敗XD
    """
    abu = SimpleImage("image_contest/Abu.JPG")
    bg = SimpleImage("image_contest/Abu_bg.jpeg")

    abu_twin = horizontal_flip(abu)
    bg.make_as_big_as(abu_twin)

    combined_img = combine(bg, abu_twin)
    combined_img.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
