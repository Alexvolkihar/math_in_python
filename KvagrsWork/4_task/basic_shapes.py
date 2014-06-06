#! usr/bin/env python

from PIL 	   import Image
from math 	   import tan, sqrt, pi, cos, sin, floor, ceil
from itertools import product

""" Example of Image.new and putpixel - puts black pixel at [100,100] """
#im = Image.new("RGB", (2300, 200), "white")
#im.putpixel((100,100), (0,0,0))
#im.show()

WHITE = (255,255,255)
BLACK = (0,0,0)

def circle(r, x0=100, y0=100, fill=False, eps = 0.05):
# r = radius, the center of the circle = [x0,y0]

	coordinates = []
	for x in xrange(-r,r):
		for y in xrange(-r,r):
			if fill and x**2 + y**2 - r**2 <= eps :				# fill == True, therefore fill it!
				coordinates.append([x+x0,y+y0])				# creating the circle somwhere, and then moving it 
				print "fill"
			if ~fill and abs((x**2 + y**2 - r**2)/float(r**2)) <= eps:	# fill == False 
				coordinates.append([x+x0,y+y0])

	return coordinates


def circle_par(r, start, end, thickness=20, fill=True):		# r = radius, start/end, absolute angles

	coordinates = []
	for t in xrange(start, end):
		r_t = (t*pi)/180									# Convert degrees to radians
		x = r+int(r*cos(r_t))								# Calculate coordinates		
		y = r+int(r*sin(r_t))
		coordinates.extend(circle(thickness, x+r, y+r, fill))

	return coordinates


def ellipse_par(a, b, start=0, end=360, thickness=5, fill=True):	# a, b axis, start/end, absolute angles

	coordinates = []
	for t in xrange(start, end):
		r_t = (t*pi)/180									# Convert degrees to radians
		x = a+int(a*cos(r_t))								# Calculate coordinates		
		y = b+int(b*sin(r_t))
		coordinates.extend(circle(thickness, x+a, y+b, fill))

	return coordinates


def spiral(a, b, eps=0.05):

	coords = []
	for x, y in product(range(-a, a), range(-b, b)):
		if (x / a)**2 + (y / b)**2 - 1 <= eps:
			coords.extend()

	return


def spiral_par(start=0, end=3*360, thickness=3, fill=True):	# start/end, absolute angles

	# Calculate the offset
	#r_t = ((end%360)*pi)/180
	#a = int(end*cos(r_t) )
	#b = int(end*sin(r_t))
	coordinates = []
	for t in xrange(start, end):
		r_t = (t*pi)/180									# Convert degrees to radians
		x = int(cos(r_t))									# Calculate coordinates		
		y = int(sin(r_t))
		
		coordinates.extend(circle(thickness, x, y, fill))

	#print coordinates
	return coordinates


def equilateral_triangle(side):

	coordinates = []
	#print -side/2, side/2,int((sqrt(3)*side)/2)
	for x in xrange(-side/2, side/2):
		for y in xrange(int((sqrt(3)*side)/2)):
			v = (sqrt(3)*side)/2
			if y <= sqrt(3)*x+v and y <= -sqrt(3)*x+v:
				coordinates.append([x+side,-y+side])		# minus y-coordinate - [0,0] is top left and pos. directions are v and >

	return coordinates


#######################################

def movePointsTowardsOrigin(points):

	minX = points[0][0]
	minY = points[0][1]
	maxX = points[0][0]
	maxY = points[0][1]

	for point in points:
		if minX > point[0]: minX = point[0]
		if minY > point[1]:	minY = point[1]
		if maxX < point[0]:	maxX = point[0]
		if maxY < point[1]:	maxY = point[1]

	minA = min(minX, minY)

	for point in points:
		point[0] -= minX
		point[1] -= minY

	size = max(maxX - minX, maxY - minY) + 1
	return points, size	


def draw(coordinates, filename=''):
	
	coordinate, size = movePointsTowardsOrigin(coordinates)
	im = Image.new("RGB", (size,size), "white")
	for pixel in coordinates:
		r = pixel[0]
		g = pixel[1]
		b = pixel[0] + pixel[1]+100
		#b = (200)

		color = (r,g,b)
		im.putpixel( pixel, color)

	if filename:
		im.save('img/'+ filename + ".bmp")
	else:
		im.show()


if __name__ == '__main__':

	#draw(circle(100, 300,300, fill=True), filename="circle_fill")
	#draw(circle(100, 300,300, fill=False), filename="circle")
	#draw(circle_par(100, 0, 360, thickness=5, fill=True), filename="circle_par")
	#draw(equilateral_triangle(100), filename="equilateral_triangleA")
	#draw(ellipse_par(100,50), filename="spiral_par")
	#draw(spiral_par())	
	draw(spiral())