#!/usr/bin/env python

import sys
sys.path.append("../../JendasWork/2_task/")
sys.path.append("/home/ubuntu/math_in_python/JendasWork/2_task/")

from flask import Flask, render_template
app = Flask(__name__)

from urlparse         import parse_qs
from bottle           import route, run, template, static_file
from pascals_triangle import plot_pascals_triangle


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/plhak')
def plhak():
    return render_template('plhak.html')


@app.route('/plhak/pascal/<qstring>')
def index(qstring):
    print "Attempting to print pascals triangle"
    print "     Parameters: %s\n" % qstring

    params = parse_qs(qstring)
    print params
    if not (int(params["n_layers"][0]) > 0 and int(params["n_layers"][0]) < 150):
        params["n_layers"][0] = 50
        
    return plot_pascals_triangle( int(params["n_layers"][0]),
                                  int(params["d"][0])
                                )

@app.route('/kvapil')
@app.route('/kvapil/task/<task>')
def kvapil_task(task=None):
    if task == 1:
        return render_template('1_taskKvapil.html')   
        
    return render_template('kvapil.html', name=name)




if __name__ == '__main__':
    app.run(port=8080)