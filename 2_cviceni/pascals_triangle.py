#!/usr/bin/env python

import svgwrite
import colorsys


def pascals_triangle(n_layers):

    if n_layers <= 0:
        raise Exception(" Non-positive values of n_layers not allowed!")

    layers = [[1]]
    for i in xrange(n_layers - 1):
        layers.append([1])
        for j in xrange(i):
            layers[-1].append(layers[-2][j] + layers[-2][j+1])
        layers[-1].append(1)
    return layers


def plot_pascals_triangle(n_layers, d):     # d = divisor

    layers  = pascals_triangle(n_layers)
    draw    = svgwrite.drawing.Drawing()

    sq_edge = 10                             # length of edge of plotted square in pixels
    center  = n_layers * sq_edge / 2 + 20    # Center coordinates
    shift   = sq_edge / 2                    # how much to shift from the center

    HSV_tuples = [(x*2.0/d, 0.75, 0.85) for x in range(d)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    RGB_tuples = [[i * 255 for i in colour] for colour in RGB_tuples]

    for i in xrange(n_layers):
        for j, n in enumerate(layers[i]):
            draw.add(draw.rect( (center - shift + j*sq_edge, sq_edge * i + 20), 
                                (sq_edge, sq_edge), 
                                fill   = svgwrite.utils.rgb(RGB_tuples[n%d][0], RGB_tuples[n%d][1], RGB_tuples[n%d][2], mode='RGB'),
                                stroke = 'black'
                              )
                    )
        shift += sq_edge / 2

    draw.saveas("pascals_triangle.svg")
    return draw.tostring()


plot_pascals_triangle(50, 13)