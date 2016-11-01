# Functions for sorting colors
import math
import colorsys


def get_average_color(image, color_size=2048):
    colors = image.getcolors(color_size * 4)
    max_oc, most_pres = 0, 0
    try:
        for c in colors:
            if c[0] > max_oc:
                (max_oc, most_pres) = c
        return most_pres
    except TypeError:
        raise Exception("too many colors in the image")


def lum(r, g, b):
    return math.sqrt( .241 * r + .691 * g + .068 * b)


def step(r, g, b, repetitions=1):
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return int(h * repetitions), int(lum(r, g, b) * repetitions),int(v * repetitions)
