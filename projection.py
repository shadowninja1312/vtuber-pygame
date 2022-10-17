import pygame
import numpy as np
import math 
import cv2
import dlib
import time
from numba import njit
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pygame.init()
start = time.time()
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
front_head_img = pygame.image.load("amongus.png").convert()
front_head_img.set_colorkey(WHITE)
scale = 100
list_of_z_rot = []
list_of_y_rot = []
list_of_x_rot = []

circle_pos = [WIDTH/2, HEIGHT/2]  # x, y
open_eye = 10
rounded = 50
x_angle = 0
y_angle = 0
z_angle = 0
points = []
framesSkipping = 2
rot_smooth = 3*framesSkipping
pos_smooth = 2*framesSkipping
count = 0
x_pos = 0
y_pos = 0
list_of_x_pos = []
list_of_y_pos = []
# all the cube vertices
points.append(np.array([-1, -1, 1]))#0[(300.0, 200.0,500.0) 
points.append(np.array([1, -1, 1]))#1(500.0, 200.0,500.0)
points.append(np.array([1,  1, 1]))#2(500.0, 400.0,500.0) 
points.append(np.array([-1, 1, 1]))#3(300.0, 400.0,500.0)
points.append(np.array([-1, -1, -1]))#4 (300.0, 200.0,300.0) 
points.append(np.array([1, -1, -1]))#5(500.0, 200.0,300.0)
points.append(np.array([1, 1, -1]))#6 (500.0, 400.0,300.0)
points.append(np.array([-1, 1, -1]))#7(300.0, 400.0,300.0)
point_data = []
projection_matrix = np.array([
	[1, 0, 0],
	[0, 1, 0],
	[0, 0 , 1]
])
projected_points = [
	[n, n] for n in range(len(points))
]
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
def connect_points(x, y, points):
	pygame.draw.line(
		screen, BLACK, (points[x][0], points[x][1]), (points[y][0], points[y][1]))
def pythagoras(a,b):
	return math.sqrt(a**2 + b**2)
def draw_front_face(point_data):
	#drawing the front face
	front = pygame.transform.scale(front_head_img,(pythagoras(abs(point_data[1][0]-point_data[0][0]),abs(point_data[1][1]-point_data[0][1])),(pythagoras(abs(point_data[2][0]-point_data[1][0]),abs(point_data[2][1]-point_data[1][1])))))
	front = pygame.transform.rotate(front,(math.atan2((point_data[0][1]-point_data[1][1]),(point_data[0][0]-point_data[1][0]))/math.pi*180))
	front = pygame.transform.flip(front,False,True)
	screen.blit(front,((min(point_data[0][0],point_data[1][0],point_data[2][0],point_data[3][0]),(min(point_data[0][1],point_data[1][1],point_data[2][1],point_data[3][1])))))
def mean (numbers):
    ans = 0
    for number in numbers:
        ans += number
    return(ans/len(numbers))
def get_z_rotation(landmarks):
	z_rot = math.atan2(((landmarks.part(42).y)-landmarks.part(39).y),(landmarks.part(42).x-landmarks.part(39).x))
	if len(list_of_z_rot) >= rot_smooth:
		if len(list_of_z_rot) > rot_smooth:
			for i in range(len(list_of_z_rot) - rot_smooth):
				list_of_z_rot.pop(0)
		temp_z_rot = []
		for i in range(rot_smooth):
			temp_z_rot.append(list_of_z_rot[i*-1])
		list_of_z_rot.append(z_rot)
		return round(mean(temp_z_rot),rounded)
	else:
		list_of_z_rot.append(z_rot)
		return(round(z_rot,rounded))
def get_y_rotation(landmarks):
	y_rot = (((math.sqrt((math.pow((landmarks.part(26).x - landmarks.part(22).x),2))+math.pow(landmarks.part(26).y - landmarks.part(22).y,2)) - math.sqrt((math.pow((landmarks.part(21).x - landmarks.part(17).x),2))+math.pow((landmarks.part(22).y - landmarks.part(17).y),2)))/180*math.pi)*-1)
	if len(list_of_y_rot) >= rot_smooth:
		if len(list_of_y_rot) > rot_smooth:
			for i in range(len(list_of_y_rot) - rot_smooth):
				list_of_y_rot.pop(0)
		temp_y_rot = []
		for i in range(rot_smooth):
			temp_y_rot.append(list_of_y_rot[i*-1])
		list_of_y_rot.append(y_rot)
		return round(mean(temp_y_rot),rounded)
	else:
		list_of_y_rot.append(y_rot)
		return(round(y_rot,rounded))
def get_x_rotation(landmarks):
	x_rot = (((((landmarks.part(30).y- landmarks.part(27).y)/(landmarks.part(42).x-landmarks.part(39).x))))/math.pi*180-45)/180*math.pi*-1
	if len(list_of_x_rot) >= rot_smooth:
		if len(list_of_x_rot) > rot_smooth:
			for i in range(len(list_of_x_rot) - rot_smooth):
				list_of_x_rot.pop(0)
		temp_x_rot = []
		for i in range(rot_smooth):
			temp_x_rot.append(list_of_x_rot[i*-1])
		list_of_x_rot.append(x_rot)
		return round(mean(temp_x_rot),rounded)
	else:
		list_of_x_rot.append(x_rot)
		return(round(x_rot,rounded))
while True:
	_, frame = cap.read()
	frame = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	if (count % framesSkipping == 0):
		faces = detector(gray)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				exit()

	# update stuff
	if len(faces) !=0:
		for face in faces:
			circle_pos = [face.left()+(face.right()-face.left())/2,face.top()]
			if len(list_of_x_pos) >= pos_smooth:
				if len(list_of_x_pos) > rot_smooth:
					for i in range(len(list_of_x_pos) - pos_smooth):
						list_of_x_pos.pop(0)
					for i in range(len(list_of_y_pos)- pos_smooth):
						list_of_y_pos.pop(0)
				temp_x_pos = []
				temp_y_pos = []
				for i in range(pos_smooth):
					temp_x_pos.append(list_of_x_pos[i*-1])
					temp_y_pos.append(list_of_y_pos[i*-1])
				list_of_x_pos.append(circle_pos[0])
				list_of_y_pos.append(circle_pos[1])
				x_pos = (round(mean(temp_x_pos)))
				y_pos = (round(mean(temp_y_pos)))
				circle_pos = [x_pos, y_pos]
			else:
				list_of_x_pos.append(circle_pos[0])
				list_of_y_pos.append(circle_pos[1])
			landmarks = predictor(gray, face)
			x_angle = get_x_rotation(landmarks)
			y_angle = get_y_rotation(landmarks)
			z_angle = get_z_rotation(landmarks)
			face = []
	count += 1
	rotation_z = np.array([
		[math.cos(z_angle), -math.sin(z_angle), 0],
		[math.sin(z_angle), math.cos(z_angle), 0],
		[0, 0, 1],
	])

	rotation_y = np.array([
		[math.cos(y_angle), 0, math.sin(y_angle)],
		[0, 1, 0],
		[-math.sin(y_angle), 0, math.cos(y_angle)],
	])

	rotation_x = np.array([
		[1, 0, 0],
		[0, math.cos(x_angle), -math.sin(x_angle)],
		[0, math.sin(x_angle), math.cos(x_angle)],
	])

	screen.fill(WHITE)
	# drawining stuff
	point_data = []
	i = 0
	for point in points:
		rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
		rotated2d = np.dot(rotation_y, rotated2d)
		rotated2d = np.dot(rotation_x, rotated2d)
		projected2d = np.dot(projection_matrix, rotated2d)
		x = int(projected2d[0][0] * scale) + circle_pos[0]
		y = int(projected2d[1][0] * scale) + circle_pos[1]
		z = int(projected2d[2][0] * scale) + circle_pos[0]
		projected_points[i] = [x, y, z]
		i += 1
		point_data.append((x,y,z))
	for p in range(4):
		connect_points(p, (p+1) % 4, projected_points)
		connect_points(p+4, ((p+1) % 4) + 4, projected_points)
		connect_points(p, (p+4), projected_points)
	pygame.draw.polygon(screen, (255,0,0),((point_data[0][0], point_data[0][1]),(point_data[1][0], point_data[1][1]),(point_data[2][0], point_data[2][1]),(point_data[3][0], point_data[3][1])))
	if y_angle < 0:
		pygame.draw.polygon(screen,(228,32,21),((point_data[1][0],point_data[1][1]),(point_data[2][0],point_data[2][1]),(point_data[6][0],point_data[6][1]),(point_data[5][0],point_data[5][1])))
		#draw_left_face(point_data)
	elif y_angle > 0:
		pygame.draw.polygon(screen,(228,32,21),((point_data[0][0],point_data[0][1]),(point_data[3][0],point_data[3][1]),(point_data[7][0],point_data[7][1]),(point_data[4][0],point_data[4][1])))
		#draw_right_face(point_data)
	draw_front_face(point_data)
	pygame.display.set_caption(f"FPS:{round(count/(time.time()-start))}")	
	pygame.display.update()