import math


def circle_col(
    pos1: tuple[float, float], rad1: int, pos2: tuple[float, float], rad2: int
):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) <= rad1 + rad2
