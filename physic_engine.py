import pygame
import math
bounce_friction = 0.9
gravity = 1
friction = 0.999
RED = (255,0,0)
BLACK = (0,0,0)
def pythagoras(a,b):
	return math.sqrt(a**2 + b**2)
class stick():	
	def __init__(self,point_1,point_2,hidden,dots):
		self.point_1 = point_1
		self.point_2 = point_2
		self.length = pythagoras(dots[self.point_1].x - dots[self.point_2].x,dots[self.point_1].y-dots[self.point_2].y)
		self.hidden = hidden
	def update_sticks(self,dots):
		dx = dots[self.point_2].x - dots[self.point_1].x
		dy = dots[self.point_2].y - dots[self.point_1].y
		distance = (pythagoras(dx,dy))
		difference = (self.length - distance)
		if distance !=0:
			percent = difference / distance / 2
		else:
			percent = 0
		offset_X = dx*percent
		offset_y = dy*percent
		if dots[self.point_1].dynamic == True:
			dots[self.point_1].x -= offset_X
			dots[self.point_1].y -= offset_y
		if dots[self.point_2].dynamic == True:
			dots[self.point_2].x += offset_X
			dots[self.point_2].y += offset_y
def render_sticks(screen,dots,sticks):
	for stick in sticks:
		if not stick.hidden :
			pygame.draw.line(screen,BLACK,(dots[stick.point_1].x,dots[stick.point_1].y),(dots[stick.point_2].x,dots[stick.point_2].y))
class dot():
	def __init__(self,x,y,oldx,oldy,hidden,radius,dynamic,collision,more_or_less):
		self.x = x
		self.y = y
		self.oldx = oldx
		self.oldy = oldy
		self.hidden = hidden
		self.radius = radius
		self.dynamic = dynamic
		self.collision = collision
		self.more_or_less = more_or_less
	def update_dots(self):
		if self.dynamic:
			vx = (self.x - self.oldx)*friction
			vy = (self.y - self.oldy)*friction
			self.oldx = self.x
			self.oldy = self.y
			self.x += vx
			self.y += vy
			self.y += gravity
			if self.collision !="NIL":
				if self.more_or_less =="more":
					if self.x < self.collision.x:
						self.x = self.collision.x
						self.oldx = self.x + vx* bounce_friction
				if self.more_or_less =="less":
					if self.x > self.collision.x:
						self.x = self.collision.x
						self.oldx = self.x+vx* bounce_friction
def render_dots(screen,dots):
	DOT_COLOUR = [255,0,0]
	for d in dots:
		if d.hidden == False:
			pygame.draw.circle(screen,DOT_COLOUR,(d.x,d.y),d.radius)
dots = []
sticks = []
def draw(screen,dots,sticks):
	render_dots(screen,dots)
	render_sticks(screen,dots,sticks)
def update(dots,sticks):
	for d in dots:
		d.update_dots()

	for s in sticks:
		s.update_sticks(dots)
