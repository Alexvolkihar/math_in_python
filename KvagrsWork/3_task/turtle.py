#######################################
#
# Turtle graphics
#
#######################################

import svgwrite
from svglib import svg
from math 	import sin, cos, pi, sqrt, atan

def tan(alpha):

	return sin(alpha)/cos(alpha)


class Turtle(object):

	def __init__(self, absolute=False):
		self.x = 0							# Turtle starts at [0,0]
		self.y = 0
		self.phi = 0						# Starting angle
		self.pen = True
		self.absolute = absolute
		self.lines = []

	def forward(self, d):

		phi = self.degToRad(self.phi)		# conversion

		n_x = self.x + d*cos(phi)			# Calculating new coordinates
		n_y = self.y + d*sin(phi)

		if self.pen == True:				# Drawing lines
			self.lines.append([self.x, self.y, n_x, n_y])	# One line is #4 list with starting coord. and ending coord.
			if self.absolute == False:
				self.x = n_x
				self.y = n_y
		else:								# Changing the starting positions
			if self.absolute == False:
				self.x = n_x
				self.y = n_y
		return

	def back(self, d):

		self.forward(-d)
		return


	def left(self, phi):

		self.phi -= phi
		return


	def right(self, phi):
		self.phi += phi
		return


	def penup(self):

		self.pen = False
		return


	def pendown(self):

		self.pen = True
		return


	def degToRad(self,phi):						# Conversion function from degrees to radians

		r_phi = (phi*pi)/180
		return r_phi


	def draw_object(self, filename, width=200, height=200):
		
		im = svgwrite.drawing.Drawing()
		for x in range(len(self.lines)):
			A = (self.lines[x][0]+width/2,self.lines[x][1]+height/2)			# Different offsets, to make i clearer on web
			B = (self.lines[x][2]+width/2,self.lines[x][3]+height/2)
			im.add( im.line(	start = A,\
								end   = B,\
								stroke= 'black'))		

		im.saveas(filename)
		return


########################################

def polygon(turtle, k, n=5):					# turtle = object from Turtle class, k = length of a side, n = number of sides
	for x in range(n):
		turtle.forward(k)
		turtle.left(360/n)
	return

def star(turtle, k, n=9):						# not working quite yet
	for x in range(n):
		turtle.forward(k)
		turtle.left( ((n+1)/2)*360/n )
	return	

""" Third task picture B /relatively """
def infsquare(turtle, k, x, n=100):				# turtle = object from Turtle class, k = length of the biggest side, x = the offset of smaller square		
	angle = radToDeg(atan( float(x/(k-x)) ))
	for i in range(n):
		polygon(turtle, k, 4)
		turtle.penup()							# penup/down is not neccesary here, but svgwrite overwrites some lines..
		turtle.forward(x)
		turtle.pendown()
		turtle.left(angle)
		print angle
		tmp = sqrt((k-x)**2 + x*2)
		x 	= (x*tmp)/k
		k 	= tmp
	return

""" Third task picture D /relatively """
def triangles(turtle, side, step, n=5):
	for i in range(n):
		#print side
		side += (3*step)
		#print side
		polygon(turtle, side, 3)
		turtle.right(120)
		turtle.penup()
		turtle.forward(step)
		turtle.left(120)
		turtle.back(step)
		turtle.pendown()
	return

""" Third task picture E /relatively """
def polycircle(turtle, n=12):
	for x in range(n):
		polygon(turtle, 30, n)
		turtle.left(360/n)
	return

""" Third task picture C/absolutely"""
def line_circle(turtle, R, n):	# turtle is absolute
	step = R/n*1.
	lines = []
	for i in range(n):
		x0 = 0
		y0 = step/2+i*step
		x1 = sqrt(R**2-y0**2)
		y1 = y0

		turtle.lines.append([x0, y0, x1, y1])
		turtle.lines.append([x0, y0, -x1, y1])
		turtle.lines.append([x0, -y0, x1, -y1])
		turtle.lines.append([x0, -y0, -x1, -y1])

	for i in range(n+1):
		y0 = 0
		x0 = i*step
		y1 = sqrt(R**2-x0**2)
		x1 = x0

		turtle.lines.append([x0, y0, x1, y1])
		turtle.lines.append([x0, y0, x1, -y1])
		turtle.lines.append([-x0, y0, -x1, y1])
		turtle.lines.append([-x0, y0, -x1, -y1])
	return 

""" Fractals """

def bush(turtle, n, step):
	vertices = []
	if n == 1:						# Drawing simple V
		turtle.left(45)
		turtle.forward(step)
		turtle.back(step)
		turtle.right(90)
		turtle.forward(step)
	else:
		turtle.left(45)
		turtle.forward(step)
		vertices.append([turtle.x, turtle.y, turtle.phi])	# Writing down coordinates and angle
		turtle.back(step)
		turtle.right(90)
		turtle.forward(step)
		vertices.append([turtle.x, turtle.y, turtle.phi])	# Writing down coordinates and angle
		step /= 2
		n -= 1
		
		for vertex in vertices:
			turtle.x = vertex[0]
			turtle.y = vertex[1]
			turtle.phi = vertex[2]
			bush(turtle, n, step)
	return

#def snow_flake(turtle, n, )

#######################################

def radToDeg(rad):
		deg = (rad * 180)/pi
		return deg

#######################################


if __name__ == '__main__':

	turtle = Turtle()
	"""
	turtle.left(90)
	polygon(turtle, 30)
	turtle.save("polygon")
	"""
	
	triangles(turtle, 5., 5,10)
	turtle.draw_object("triangles.svg")