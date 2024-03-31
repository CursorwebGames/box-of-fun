# Enter equations for x and y, and a rainbow comes out!
from math import sin, cos, pi

sx = lambda t: sin(4 * t) * cos(5 * t)
sy = lambda t: sin(5 * t) * cos(7 * t)

from PIL import Image, ImageDraw

SIZE = 500
DETAIL = 500
THICK = 2

step = 2 * pi / DETAIL

im = Image.new(mode="HSV", size=(SIZE, SIZE))
ctx = ImageDraw.Draw(im)


def map(x, y):
    return x * (SIZE / 2 - THICK * 2) + SIZE / 2, y * (SIZE / 2 - THICK * 2) + SIZE / 2


for i in range(0, DETAIL):
    theta = (i / DETAIL) * 2 * pi

    (x1, y1), (x2, y2) = map(sx(theta), sy(theta)), map(
        sx(theta + step), sy(theta + step)
    )

    hue = round(i % 255)

    ctx.line((x1, y1, x2, y2), (hue, 255, 255), width=2 * THICK)

im = im.convert(mode="RGB")
im.save("output.png")
