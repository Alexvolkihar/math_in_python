#!/usr/bin/env python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/plhak')
def plhak():
	return render_template('plhak.html')

@app.route('/kvapil')
def kvapil():
	return render_template('kvapil.html')
if __name__ == '__main__':
	app.run(port=8080)
