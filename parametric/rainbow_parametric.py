# Enter equations for x and y, and a rainbow comes out!
from PIL import Image, ImageDraw
from math import sin, cos, pi
from typing import Callable


def draw(
    s: Callable[[float], tuple[float, float]],
    name: str,
    size: int,
    detail: int,
    thickness: int,
    period: int,
):
    SIZE = size
    DETAIL = detail
    THICK = thickness
    PERIOD = period

    step = PERIOD / DETAIL

    im = Image.new(mode="HSV", size=(SIZE, SIZE))
    ctx = ImageDraw.Draw(im)

    def map(x, y):
        return (
            x * (SIZE / 2 - THICK * 2) + SIZE / 2,
            -y * (SIZE / 2 - THICK * 2) + SIZE / 2,
        )

    for i in range(0, DETAIL):
        theta = (i / DETAIL) * PERIOD

        (x1, y1), (x2, y2) = map(*s(theta)), map(*s(theta + step))

        hue = round(i % 255)

        ctx.line((x1, y1, x2, y2), (hue, 255, 255), width=2 * THICK)

    im = im.convert(mode="RGB")
    im.save(f"{name}.png")
