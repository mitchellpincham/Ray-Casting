import pygame
import math
from formulas import *
pygame.init()

file = open("settings.txt", "r")
file_lines = file.readlines()
for i in range(len(file_lines)):
	try:
		file_lines[i] = int("".join(file_lines[i][:-1]))
	except ValueError:
		try:
			file_lines[i] = float("".join(file_lines[i][:-1]))
		except ValueError:
			file_lines[i] = "".join(file_lines[i][:-1]).lower()
	except:
		pass

wid = file_lines[1]
hei = file_lines[4]

ray_step = file_lines[7]

win = pygame.display.set_mode((wid, hei))
clock = pygame.time.Clock()
pygame.display.set_caption("Game")



def rays():
	mouse_pos = pygame.mouse.get_pos()

	if not editor:  # the only difference between this file and the main one is this loop's drawing
		points = []
		for i in range(round(360 / ray_step)):
			line = p2c(mouse_pos[0], mouse_pos[1], wid + hei, i * ray_step)

			end_point = intersect((line[0], line[1]), (line[2], line[3]), i * ray_step, lines, False)
			if not(end_point):
				pass
			else:
				points.append((end_point[0], end_point[1]))
				#pygame.draw.line(win, (127, 127, 127), (line[0], line[1]), (end_point[0], end_point[1]))
				pygame.draw.circle(win, (0, 255, 0), (end_point[0], end_point[1]), 5)
		pygame.draw.polygon(win, (127, 127, 127), points)


def down(mouse_pos):
	global mouse_start
	mouse_start = mouse_pos

def up(mouse_pos):
	lines.append((mouse_start[0], mouse_start[1], pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

def redraw_window():
	win.fill((0, 0, 0))

	rays()

	if editor:
		for x in lines:
			pygame.draw.line(win, (255, 255, 255), (x[0], x[1]), (x[2], x[3]))
	else:
		for x in lines:
			pygame.draw.line(win, (255, 255, 255), (x[0], x[1]), (x[2], x[3]), 2)

	if mouse_down:
		pygame.draw.line(win, (128, 255, 0), (mouse_start[0], mouse_start[1]), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

	pygame.display.update()

#		 top 			 	  bottom				 		  left			  	  right
lines = [(1, 1, wid - 1, 1), (1, hei - 1, wid - 1, hei - 1), (1, 1, 1, hei - 1), (wid - 1, 1, wid - 1, hei - 1)]
mouse_start = []
mouse_down = False
editor = True

run = True
while run:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.MOUSEBUTTONDOWN and editor:
			down(pygame.mouse.get_pos())
			mouse_down = True
		elif event.type == pygame.MOUSEBUTTONUP and editor:
			up(pygame.mouse.get_pos())
			mouse_down = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_RETURN]:
		editor = False

	redraw_window()


pygame.quit()
