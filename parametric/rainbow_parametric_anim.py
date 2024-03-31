from PIL import Image, ImageDraw
from math import sin, cos, pi

images: list[Image.Image] = []
# Enter equations for x and y, and a rainbow comes out!

s = lambda t: (sin(14 * t), cos(15 * t))

SIZE = 250
DETAIL = 500  # more detail = more points (slower)
THICK = 2
IMAGE_STEP = 10
PERIOD = 2 * pi

step = PERIOD / DETAIL


def map(x, y):
    return x * (SIZE / 2 - THICK * 2) + SIZE / 2, y * (SIZE / 2 - THICK * 2) + SIZE / 2


def create_image(start, end):
    im = Image.new(mode="HSV", size=(SIZE, SIZE))
    ctx = ImageDraw.Draw(im)

    for i in range(start, end):
        theta = (i / DETAIL) * PERIOD

        (x1, y1), (x2, y2) = map(*s(theta)), map(*s(theta + step))

        hue = round((2 * i / DETAIL) * 255) % 255

        ctx.line((x1, y1, x2, y2), (hue, 255, 255), width=2 * THICK)

    im = im.convert(mode="RGB")
    images.append(im)


for md in range(0, DETAIL + IMAGE_STEP, IMAGE_STEP):
    create_image(0, md)

for md in range(0, DETAIL + IMAGE_STEP, IMAGE_STEP):
    create_image(md, DETAIL)

images[0].save(
    "output.gif",
    save_all=True,
    append_images=images[1:],
    optimize=True,
    duration=40,
    loop=0,
)
