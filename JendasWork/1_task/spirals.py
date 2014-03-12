#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import floor, sqrt, sin, cos


def first_n_primes(n):           # Calculates first n primes using sieve of Eratosthenes

    sieve = [True] * (n/2)
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i/2]: 
            sieve[i*i/2::i] = [False] * ((n - i*i - 1)/(2*i) + 1)
    return [2] + [2*i + 1 for i in xrange(1, n/2) if sieve[i]]


def calculate_coordinates_Ulam_spiral(n):    # Calculates [x,y] coordinates of given number n in Ulam spiral using formula 
                                             # listed on web-page http://danpearcymaths.wordpress.com/2012/09/30/infinity-programming-in-geogebra-and-failing-miserably/
    p = floor(sqrt(4*n + 1))
    q = n - floor(p**2 / 4)
    z = q * 1j**p + ( floor((p + 2)/4) - 1j*floor((p + 1)/4) ) * 1j**(p - 1)

    z *= -1j
    return [z.real, z.imag]


def calculate_coordinates_archimedian_spiral(n):

    angle = n * 0.5
    x     = (1 + angle)*cos(angle)
    y     = (1 + angle)*sin(angle)
    return [x, y]


def plot_and_save_spiral(n, spiral_fun, path):

    primes        = first_n_primes(n)
    coord_primes  = zip(*[spiral_fun(i) for i in primes])
    
    fig = plt.figure(figsize=(23.5, 23.5)) 
    plt.plot(coord_primes[0], coord_primes[1],    'ro')

    if spiral_fun == calculate_coordinates_Ulam_spiral:

        coord_quad_form = {}   # Interesting patterns can be observed when highlighting primes of form 4n + an + b
        for i in xrange(n):
            coord_quad_form[4*i**2 + 7*i - 49] = None 
            if 4*i**2 + 3*i - 19 > primes[-1]:
                break
        coord_quad_form = zip(*[spiral_fun(i) for i in primes if i in coord_quad_form])
        plt.plot(coord_quad_form[0], coord_quad_form[1], 'bo', markersize=15)
    # else:
    #     coord_spiral  = zip(*[spiral_fun(i) for i in range(n)])
    #     plt.plot(coord_spiral[0], coord_spiral[1], 'k')

    plt.axis([ min(coord_primes[0]) - 1, max(coord_primes[0]) + 1, min(coord_primes[1]) - 1, max(coord_primes[1]) + 1 ])

    fig.savefig(path, dpi=80, bbox_inches='tight')
    plt.clf()


if __name__ == "__main__":

    plot_and_save_spiral(100000, calculate_coordinates_Ulam_spiral,       "img/Ulam_spiral.png");
    plot_and_save_spiral(50000, calculate_coordinates_archimedian_spiral, "img/Archimed_spiral.png");
