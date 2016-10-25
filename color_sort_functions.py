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


def tester(r, g, b):
    return math.sqrt(2 * r + 3 * g + .134 * b)


def hsv_sort():
    pass


def hls_sort():
    pass


def lum_sort():
    pass


def step_sort():
    pass


def hilbert_sort():
    pass


    # hsv sort
    # slices['hsv_sort_sequence'] = []
    # colours.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb)    )

    # hls sort
    # slices['hls_sort_sequence'] = []
    # colours.sort(key=lambda rgb: colorsys.rgb_to_hls(*rgb)    )

    # lum sort
    # colours.sort(key=lambda rgb: lum(*rgb)    )

    # step sort
    # colours.sort(key=lambda (r,g,b): step(r,g,b,8)    )

    # hilbert sort
    # find hilbert
    # colours.sort(key=lambda (r,g,b):hilbert.Hilbert_to_int([int(r*255),int(g*255),int(b*255)])