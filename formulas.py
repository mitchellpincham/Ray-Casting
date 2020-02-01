import math

def find_dis(x1, x2, y1, y2):  # this function returns the absolute distance between 2 points
	return math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2);

# polar to cartesian
def p2c(x, y, r, a):
	# r = radius, a = angle

	# degrees to radians and reverses it to go anti-clockwise
	a *= -math.pi / 180

	# delta variables - how much to increase x and y by
	dx = r * math.cos(a)
	dy = r * math.sin(a)
	# returns the new coords
	return [x, y, x + dx, y + dy]

# this function finds the closest intercecing point for a line
def intersect(a, b, angle, lines, hor=True):
	closest = [999999, 999999]
	point = False
	for line in lines:
		"""
			https://www.geeksforgeeks.org/program-for-point-of-intersection-of-two-lines/
		"""

		# Line AB represented as a1x + b1y = c1
		a1 = b[1] - a[1]
		b1 = a[0] - b[0]
		c1 = a1 * a[0] + b1 * a[1]

		# Line CD represented as a2x + b2y = c2
		a2 = line[3] - line[1]
		b2 = line[0] - line[2]
		c2 = a2 * line[0] + b2 * line[1]

		determinant = a1 * b2 - a2 * b1
		if determinant != 0:
			x = (c1 * b2 - c2 * b1) / determinant
			y = (a1 * c2 - a2 * c1) / determinant

			if find_dis(a[0], a[1], x, y) < find_dis(a[0], a[1], closest[0], closest[1]):								# if closer than the closest found point
				if (x + 2 >= line[0] or x + 2 >= line[2]) and (x - 2 <= line[0] or x - 2 <= line[2]):					# if x is within the line's x coords
					if (y + 2 >= line[1] or y + 2 >= line[3]) and (y - 2 <= line[1] or y - 2 <= line[3]):				# if y is withing the line's y coords
						angle = angle % 360
						if (y < a[1] and angle > 180) or (y > a[1] and angle < 180):						# if not pointing opposite to where it should be pointing
							closest = [int(x), int(y)]
							point = True
						elif (((angle == 180) and x < a[0]) or ((angle == 0) and x > a[0])) and hor:		# if hor is true then it checks 0 and 180
							closest = [int(x), int(y)]
							point = True


	if point:
		return closest
	else:
		return False
