#!/usr/bin/env python

from PIL import Image


def bifurcation(path, zoom=(2.5, 4., 0., 1.), n_iter=700):

    s_x   = 1000
    s_y   = 500
    img = Image.new("RGB", (s_x, s_y), "white")

    # zoom parameters
    x_a, x_b, y_a, y_b = zoom

    for i in xrange(s_x):
        r = x_a + (x_b - x_a) * i / float(s_x - 1)
        x = 0.5
        for j in xrange(n_iter):
            x = r * x * (1 - x)
            if j > n_iter / 3:
                if x > y_a and x < y_b:
                    q = 1 / (y_b - y_a)
                    y = int( (x - y_a) * q * s_y )
                    img.putpixel((i, y), (100, 0, 200))

    img.save(path, "png")


if __name__ == '__main__':
    
    bifurcation("img/BifurcationFull.png")
    bifurcation("img/BifurcationZoomed.png", (3.5, 4., 0.3, 0.5), 1200)
