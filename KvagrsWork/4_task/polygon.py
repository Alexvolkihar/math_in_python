#! usr/bin/env python

import sys
sys.path.append("../5_week")
import itertools
from PIL 				  import Image
from segment_intersection import cross_point


def vectorizePoints(A,B):

	return [ B[0] - A[0], B[1] - A[1] ]


def determinant(u, v):
# determinant for 2x2 matrix

	# | u0  v0 | = u0*v1 - u1*v0
	# | u1  v1 |

	return u[0] * v[1] - u[1] * v[0]


def irregularPolygon(points, size):
# points describing a irregular polygon in plane
	
	pixels = []
	for x, y in itertools.product(range(size), range(size)):
		if yAxisCrossing(points, [x, y] ) == True:
			pixels.append( [x + size, -y + size] )

	return pixels


def yAxisCrossing(vertices, point):

	saw_line = point + [0] + point[1:]
	lines 	 = []

	for i in range(len(vertices)):
		line = vertices[i] + vertices[ (i + 1) % len(vertices) ]
		lines.append( line )

	crossings = 0

	for line in lines:
		if determinantCrossPoint(line, saw_line) == True:
			crossings += 1

	if crossings % 2 == 1:
		return True
	else:
		return False


def furthesPoint(points):

	max_coordinate = 0

	for point in points:
		if max(point) > max_coordinate:
			max_coordinate = point[0]

	return max_coordinate

def drawIrregularPolygon(points, save=False, filename=""):

	size   = furthesPoint( points )
	im 	   = Image.new("RGB", (size, size), (255,255,255))
	pixels = irregularPolygon( points, size )

	for pixel in pixels:
		im.putpixel( pixel, (0,0,0) )

	im.show()
	if save:
		im.save(filename)
	return


def scoreVectorToPoints(fixed_point, vector, points):				# score = (+, -, 0)

	score = [0,0,0]

	for i in range(len(points)):		
		if determinant( vector, vectorizePoints( fixed_point, points[i] ) ) > 0:
			score[0] += 1
		elif determinant( vector, vectorizePoints( fixed_point, points[i] ) ) < 0:
			score[1] -= 1			
		else:
			score[2] -= 1

	return sum(score)


def determinantCrossPoint(line_1, line_2):

	vector_1 = vectorizePoints( line_1[:2], line_1[2:] )
	vector_2 = vectorizePoints( line_2[:2], line_2[2:] )

	score_1 = scoreVectorToPoints( line_1[:2], vector_1, [line_2[2:], line_2[:2]] )
	score_2 = scoreVectorToPoints( line_2[:2], vector_2, [line_1[2:], line_1[:2]] )

	if score_1 == 0 and score_2 == 0:
		return True
	else:
		return False


if __name__ == '__main__':

	data = [[10, 10], [180, 20], [160, 150], [100,50], [20, 180]]
	#data = [[238,196],[392,0],[498,216],[824,338],[508,422],[362,618],[254,408],[0,312]]
	drawIrregularPolygon( data, save=True, filename="polygon.bmp")