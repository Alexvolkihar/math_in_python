#!/usr/bin/env python
import numpy as np

from PIL import Image
from libc.stdlib cimport malloc, free


cdef struct Complex:
    
    float re
    float im


cdef inline Complex cMultiply(Complex a, Complex b):
    
    cdef Complex result

    result.re = a.re * b.re - a.im * b.im
    result.im = a.re * b.im + a.im * b.re
    return result


cdef inline Complex cAdd(Complex a, Complex b):
    
    cdef Complex result

    result.re = a.re + b.re
    result.im = a.im + b.im 
    return result

cdef inline Complex cNewNumber( float re_min, float im_min, 
                                float step_x, float step_y,
                                int x, int y):

    cdef Complex result
    result.re = re_min + x*step_x
    result.im = im_min + y*step_y
    return result



def complexFractal(width=3000, height=2000,c_num=-0.8+0.156*1j, julia_=True, path="img/trol.png"):
     
    # Specify image width and height
    cdef int w = width
    cdef int h = height
    cdef int i
    cdef int julia    = int(julia_)
    cdef int treshold = 2 if julia else 50
    shift = 0.
    zoom  = 10. if julia else 1.
    # Specify real and imaginary range of image
    re_min, re_max = -2*(1/zoom) + shift, 1*(1/zoom) + shift
    im_min, im_max = -1*(1/zoom) + shift, 1*(1/zoom) + shift
     
    # Pick a value for c
    cdef Complex c
    c.re = c_num.real
    c.im = c_num.imag

    cdef int **output = <int **> malloc(sizeof(int *) * w)
    for i in xrange(w):
        output[i] = <int *> malloc(sizeof(int) * h)

    cdef float **shade = <float **> malloc(sizeof(float *) * w)
    for i in xrange(w):
        shade[i] = <float *> malloc(sizeof(float) * h)

    # Generate pixel values and write to file
    cdef float step_x = abs(re_max - re_min) / w
    cdef float step_y = abs(im_min - im_max) / h

    cdef int n, x, y
    cdef Complex z, zero

    zero.re = 0
    zero.im = 0

    for x in xrange(w):
        for y in xrange(h):
            if julia:
                z = cNewNumber(re_min, im_min, step_x, step_y, x, y)
            else:
                z = zero
                c = cNewNumber(re_min, im_min, step_x, step_y, x, y)
            n = 255
            while z.re**2 + z.im**2 < treshold**2 and n >= 1:
                z = cAdd(cMultiply(z, z), c)
                n -= 1
            shade[x][y]  = (z.re**2 + z.im**2) ** 0.5
            output[x][y] = n
    
    print "Calculation finished!"
    

    img     = Image.new( 'RGB', (w,h), "black")
    pix_map = img.load()
    # Write pixels to file
    for x in xrange(w):
        for y in xrange(h):
            pix_map[x, y] = (int(255 * shade[x][y]) % 256, int(255 * shade[x][y]/2) % 256, output[x][y]*2)
    img.save(path)


    # Clean up
    for i in xrange(w):
        free(output[i])
    free(output)
