# Importing libraries
import pygame
import numpy as np
import math 
import cv2 
import dlib 
import time
import physic_engine
import skin_grabber as sg
clock = pygame.time.Clock()
user = sg.skin("technoblade")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pygame.init()
start = time.time()
WIDTH, HEIGHT = 800, 800
pygame.display.set_caption("Minecraft VTUBER!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
scale = 100
list_of_z_rot = []
list_of_y_rot = []
list_of_x_rot = []
circle_pos = [WIDTH/2, 200]
open_eye = 10
rounded = 50
x_angle = 0
y_angle = 0
z_angle = 0
points = []
framesSkipping = 3
rot_smooth = 2*framesSkipping
pos_smooth = 4*framesSkipping
count = 0
x_pos = 0
y_pos = 0
list_of_x_pos = []
list_of_y_pos = []
body_connections = []
Slim = 75
Classic = 100
model = Classic
#====================================BODY PHYSICS ====================================
body_connections = []
physics_points = []
#TOP FACE PHYSICS POINTS 
physics_points.append(physic_engine.dot(300, 200, 300, 200,False,5,False,"NIL","more"))#0
physics_points.append(physic_engine.dot(500, 200, 500, 200,False,5,False,"NIL","more"))#1
physics_points.append(physic_engine.dot(500, 200, 500, 200,False,5,False,"NIL","more"))#2
physics_points.append(physic_engine.dot(300, 200, 300, 200,False,5,False,"NIL","more"))#3
#BOTTOM FACE PHYSICS POINTS
physics_points.append(physic_engine.dot(300, 400, 300, 400,False,5,False,"NIL","more"))#4
physics_points.append(physic_engine.dot(500, 400, 500, 400,False,5,False,"NIL","more"))#5
physics_points.append(physic_engine.dot(500, 400, 500, 400,False,5,False,"NIL","more"))#6
physics_points.append(physic_engine.dot(300, 400, 300, 400,False,5,False,"NIL","more"))#7
#TOP SQUARE PHYSICS POINTS
physics_points.append(physic_engine.dot(300, 400, 300, 400,False,5,False,"NIL","more"))#8
physics_points.append(physic_engine.dot(500, 400, 500, 400,False,5,False,"NIL","more"))#9
physics_points.append(physic_engine.dot(500, 400, 500, 400,False,5,False,"NIL","more"))#10
physics_points.append(physic_engine.dot(300, 400, 300, 400,False,5,False,"NIL","more"))#11
#BOTTOM SQUARE PHYSICS POINTS
physics_points.append(physic_engine.dot(300, 700, 300, 700,False,5,True,"NIL","more"))#12
physics_points.append(physic_engine.dot(500, 700, 500, 700,False,5,True,"NIL","more"))#13
physics_points.append(physic_engine.dot(500, 700, 500, 700,False,5,True,"NIL","more"))#14
physics_points.append(physic_engine.dot(300, 700, 300, 700,False,5,True,"NIL","more"))#15
#TOP SQUARE CONNECTIONS
#body_connections.append(physic_engine.stick(0,1,False,physics_points))
#body_connections.append(physic_engine.stick(1,2,False,physics_points))
#body_connections.append(physic_engine.stick(2,3,False,physics_points))
#body_connections.append(physic_engine.stick(3,0,False,physics_points))

# BOTTOM SQUARE CONNECTIONS
body_connections.append(physic_engine.stick(12,13,False,physics_points))#0
body_connections.append(physic_engine.stick(13,14,False,physics_points))#1
body_connections.append(physic_engine.stick(14,15,False,physics_points))#2
body_connections.append(physic_engine.stick(15,12,False,physics_points))#3

# VERTICAL CONNECTIONS
body_connections.append(physic_engine.stick(8,12,False,physics_points))#4
body_connections.append(physic_engine.stick(9,13,False,physics_points))#5
body_connections.append(physic_engine.stick(10,14,False,physics_points))#6
body_connections.append(physic_engine.stick(11,15,False,physics_points))#7

#DIAGONAL CONNECTIONS IN Y POINTS
body_connections.append(physic_engine.stick(8,13,True,physics_points))#8
body_connections.append(physic_engine.stick(9,12,True,physics_points))#9
#body_connections.append(physic_engine.stick(1,6,False,physics_points)
body_connections.append(physic_engine.stick(10,15,True,physics_points))#10
body_connections.append(physic_engine.stick(11,14,True,physics_points))#11
#body_connections.append(physic_engine.stick(3,4,False,physics_points))

#====================================RIGHT ARM PHYSICS ====================================

#RIGHT ARM PHYSICS POINTS
physics_points.append(physic_engine.dot(500 + model, 400, 500 + model, 400,False,5,True,physics_points[1],"more"))#16+
physics_points.append(physic_engine.dot(500 + model, 400, 500 + model, 400,False,5,True,physics_points[2],"more"))#17-

physics_points.append(physic_engine.dot(500, 700, 500, 700,False,5,False,"NIL","more"))#18+
physics_points.append(physic_engine.dot(500 + model, 700, 500 + model, 700,False,5,True,physics_points[5],"more"))#19+
physics_points.append(physic_engine.dot(500 + model, 700, 500 + model, 700,False,5,True,physics_points[6],"more"))#20-
physics_points.append(physic_engine.dot(500, 700, 500, 700,False,5,False,"NIL","more"))#21-

#RIGHT ARM PHYSICS CONNECTIONS

#TOP CONNECTIONS
body_connections.append(physic_engine.stick(9,16,False,physics_points))#12
body_connections.append(physic_engine.stick(10,17,False,physics_points))#13
body_connections.append(physic_engine.stick(16,17,False,physics_points))#14
#BOTTOM CONNECTIONS
body_connections.append(physic_engine.stick(18,19,False,physics_points))#15
body_connections.append(physic_engine.stick(19,20,False,physics_points))#16
body_connections.append(physic_engine.stick(20,21,False,physics_points))#17
body_connections.append(physic_engine.stick(21,18,False,physics_points))#18
#VERTICAL CONNECTIONS
body_connections.append(physic_engine.stick(16,19,False,physics_points))#19
body_connections.append(physic_engine.stick(17,20,False,physics_points))#20
body_connections.append(physic_engine.stick(9,18,False,physics_points))#21
body_connections.append(physic_engine.stick(10,21,False,physics_points))#22

#DIAGONAL CONNECTIONS
body_connections.append(physic_engine.stick(16,18,True,physics_points))#23
body_connections.append(physic_engine.stick(9,19,True,physics_points))#24
body_connections.append(physic_engine.stick(17,21,True,physics_points))#25
body_connections.append(physic_engine.stick(10,20,True,physics_points))#26

#===================================== LEFT ARM PHYSICS ====================================
#LEFT ARM PHYSICS POINTS
physics_points.append(physic_engine.dot(300 - model, 400, 300 - model, 400,False,5,True,physics_points[0],"less"))#22
physics_points.append(physic_engine.dot(300 - model, 400, 300 - model, 400,False,5,True,physics_points[3],"less"))#23

physics_points.append(physic_engine.dot(300, 700, 300, 700,False,5,False,"NIL","more"))#24
physics_points.append(physic_engine.dot(300 - model, 700, 300 - model , 700,False,5,True,physics_points[4],"less"))#25
physics_points.append(physic_engine.dot(300 - model, 700, 300 - model , 700,False,5,True,physics_points[7],"less"))#26
physics_points.append(physic_engine.dot(300, 700, 300, 700,False,5,False,"NIL","more"))#27

#LEFT ARM PHYSICS CONNECTIONS

#TOP CONNECTIONS
body_connections.append(physic_engine.stick(8,22,False,physics_points))#27
body_connections.append(physic_engine.stick(11,23,False,physics_points))#28
body_connections.append(physic_engine.stick(22,23,False,physics_points))#29
#BOTTOM CONNECTIONS
body_connections.append(physic_engine.stick(24,25,False,physics_points))#30
body_connections.append(physic_engine.stick(25,26,False,physics_points))#31
body_connections.append(physic_engine.stick(26,27,False,physics_points))#32
body_connections.append(physic_engine.stick(27,24,False,physics_points))#33
#VERTICAL CONNECTIONS
body_connections.append(physic_engine.stick(22,25,False,physics_points))#34
body_connections.append(physic_engine.stick(23,26,False,physics_points))#35
body_connections.append(physic_engine.stick(8,24,False,physics_points))#36
body_connections.append(physic_engine.stick(11,27,False,physics_points))#37

#DIAGONAL CONNECTIONS
body_connections.append(physic_engine.stick(22,24,True,physics_points))#38
body_connections.append(physic_engine.stick(8 ,25,True,physics_points))#39
body_connections.append(physic_engine.stick(23,27,True,physics_points))#40
body_connections.append(physic_engine.stick(11,26,True,physics_points))#41

#====================================DRAWING STUFF====================================
# all the cube vertices
points.append(np.array([-1, -1, 1]))#0(300.0, 200.0,500.0) 
points.append(np.array([1, -1, 1]))#1(500.0, 200.0,500.0)
points.append(np.array([1,  1, 1]))#2(500.0, 400.0,500.0) 
points.append(np.array([-1, 1, 1]))#3(300.0, 400.0,500.0)
points.append(np.array([-1, -1, -1]))#4 (300.0, 200.0,300.0) 
points.append(np.array([1, -1, -1]))#5(500.0, 200.0,300.0)
points.append(np.array([1, 1, -1]))#6 (500.0, 400.0,300.0)
points.append(np.array([-1, 1, -1]))#7(300.0, 400.0,300.0)

#TOP BODY POINTS
points.append(np.array([-1, 1, 0.5]))#8
points.append(np.array([1, 1, 0.5]))#9
points.append(np.array([1, 1, -0.5]))#10
points.append(np.array([-1, 1, -0.5]))#11

point_data = []
projection_matrix = np.array([
	[1, 0, 0],
	[0, 1, 0],
	[0, 0 , 1]
])
projected_points = [
	[n, n] for n in range(len(points))
]
#getting video
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def draw_face(face,top_left,top_right,bottom_left,bottom_right,axis_dependent,more_or_less,axis,x_angle,y_angle,z_angle):
	check = 0
	if axis_dependent == False:
		check +=1
	else:
		if axis == 'x':
			if more_or_less == 'more' and x_angle>0:
				check +=1
			elif more_or_less == 'less'and x_angle<0:
				check +=1
		elif axis == 'y':
			if more_or_less == 'more' and y_angle>0:
				check +=1
			elif more_or_less == 'less'and y_angle<0:
				check +=1
		elif axis == 'z':
			if more_or_less == 'more' and z_angle>0:
				check +=1
			elif more_or_less == 'less'and z_angle<0:
				check +=1
	if check>0:
		texture = face.get_face_surface(user.get_skin())
		texture.set_colorkey((0,0,0))
		face = pygame.transform.scale(texture,(pythagoras(abs(top_right.x-top_left.x),abs(top_right.y-top_left.y)),(pythagoras(abs(bottom_left.x-top_left.x),abs(bottom_left.y-top_left.y)))))
		face = pygame.transform.rotate(face,mean([(math.atan2((bottom_right.y-bottom_left.y),(bottom_right.x-bottom_left.x))/math.pi*180),(math.atan2((top_right.y-top_left.y),(top_right.x-top_left.x))/math.pi*180)]))
		face = pygame.transform.flip(face,True,False)
		screen.blit(face,((min(top_left.x,top_right.x,bottom_left.x,bottom_right.x),(min(top_left.y,top_right.y,bottom_left.y,bottom_right.y)))))
def pythagoras(a,b):
	return math.sqrt(a**2 + b**2)
def mean (numbers):
	return(sum(numbers)/len(numbers))
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

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				exit()
	_, frame = cap.read()
	frame = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if (count % framesSkipping == 0):
		faces = detector(gray)
	# update stuff
	if len(faces) !=0:
		clock.tick()
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
			face_shape = pygame.Rect(face.left(),face.top(),face.right()-face.left(),face.bottom()-face.top())
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

	point_data = []
	i = 0
	screen.fill([0,255,0])
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

#================================================ UPDATE POINTS IN BODY POINTS ===============================
	physic_engine.update(physics_points,body_connections)
	physics_points[0].x = point_data[0][0]
	physics_points[0].y = point_data[0][1]

	physics_points[1].x = point_data[1][0]
	physics_points[1].y = point_data[1][1]

	physics_points[2].x = point_data[5][0]
	physics_points[2].y = point_data[5][1]

	physics_points[3].x = point_data[4][0]
	physics_points[3].y = point_data[4][1]

	physics_points[4].x = point_data[3][0]
	physics_points[4].y = point_data[3][1]

	physics_points[5].x = point_data[2][0]
	physics_points[5].y = point_data[2][1]

	physics_points[6].x = point_data[6][0]
	physics_points[6].y = point_data[6][1]

	physics_points[7].x = point_data[7][0]
	physics_points[7].y = point_data[7][1]



	physics_points[8].x = point_data[8][0]
	physics_points[8].y = point_data[8][1]

	physics_points[9].x = point_data[9][0]
	physics_points[9].y = point_data[9][1]

	physics_points[10].x = point_data[10][0]
	physics_points[10].y = point_data[10][1]

	physics_points[11].x = point_data[11][0]
	physics_points[11].y = point_data[11][1]

	physics_points[18].x = physics_points[13].x
	physics_points[18].y = physics_points[13].y

	physics_points[21].x = physics_points[14].x
	physics_points[21].y = physics_points[14].y

	physics_points[24].x = physics_points[12].x
	physics_points[24].y = physics_points[12].y

	physics_points[27].x = physics_points[15].x
	physics_points[27].y = physics_points[15].y

	body_connections[0].length = abs(pythagoras(point_data[8][0]-point_data[9][0],point_data[8][1]-point_data[9][1]))
	body_connections[1].length = abs(pythagoras(point_data[9][0]-point_data[10][0],point_data[9][1]-point_data[10][1]))
	body_connections[2].length = abs(pythagoras(point_data[10][0]-point_data[11][0],point_data[10][1]-point_data[11][1]))
	body_connections[3].length = abs(pythagoras(point_data[11][0]-point_data[8][0],point_data[11][1]-point_data[8][1]))
	body_connections[14].length = body_connections[1].length
	body_connections[16].length = body_connections[1].length
	body_connections[29].length = body_connections[3].length
	body_connections[31].length = body_connections[3].length


#==================================================DRAWING THINGS TO SCREEN =================================
	physic_engine.draw(screen,physics_points,body_connections)
	#pygame.draw.polygon(screen, (255,0,0),((point_data[0][0], point_data[0][1]),(point_data[1][0], point_data[1][1]),(point_data[2][0], point_data[2][1]),(point_data[3][0], point_data[3][1])))
	if y_angle < 0:
		pygame.draw.polygon(screen,(228,32,21),((point_data[1][0],point_data[1][1]),(point_data[2][0],point_data[2][1]),(point_data[6][0],point_data[6][1]),(point_data[5][0],point_data[5][1])))
	elif y_angle > 0:
		pygame.draw.polygon(screen,(228,32,21),((point_data[0][0],point_data[0][1]),(point_data[3][0],point_data[3][1]),(point_data[7][0],point_data[7][1]),(point_data[4][0],point_data[4][1])))
#	draw_face(sg.face(sg.left_face,True,sg.left_helmet),physics_points[3],physics_points[0],physics_points[7],physics_points[5],True,'more','y',x_angle,y_angle,z_angle)
#	draw_face(sg.face(sg.right_face,True,sg.right_helmet),physics_points[1],physics_points[2],physics_points[5],physics_points[6],True,'less','y',x_angle,y_angle,z_angle)
#	draw_face(sg.face(sg.top_face),physics_points[3],physics_points[2],physics_points[0],physics_points[1],True,'less','x',x_angle,y_angle,z_angle)
#	draw_face(sg.face(sg.bottom_face),physics_points[4],physics_points[5],physics_points[7],physics_points[6],True,'more','x',x_angle,y_angle,z_angle)
	draw_face(sg.face(sg.front_face,False,sg.front_helmet),physics_points[0],physics_points[1],physics_points[4],physics_points[5],False,'more','x',0,0,0)

	draw_face(sg.face(sg.front_torso,False,sg.front_second_layer_torso),physics_points[8],physics_points[9],physics_points[12],physics_points[13],False,'more','x',0,0,0)
#	draw_face(sg.face(sg.bottom_torso),physics_points[12],physics_points[13],physics_points[15],physics_points[14],True,'more','x',x_angle,y_angle,z_angle)

#	draw_face(sg.face(sg.bottom_torso),physics_points[12],physics_points[13],physics_points[15],physics_points[14],True,'more','x',x_angle,y_angle,z_angle)
#	draw_face(sg.face(sg.bottom_torso),physics_points[12],physics_points[13],physics_points[15],physics_points[14],True,'more','x',x_angle,y_angle,z_angle)
#	draw_face(sg.face(sg.bottom_torso),physics_points[12],physics_points[13],physics_points[15],physics_points[14],True,'more','x',x_angle,y_angle,z_angle)
	draw_face(sg.face(sg.front_left_arm,False,sg.front_second_layer_left_arm),physics_points[22],physics_points[8],physics_points[25],physics_points[24],False,'more','x',0,0,0)

#	draw_face(sg.face(sg.bottom_torso),physics_points[12],physics_points[13],physics_points[15],physics_points[14],True,'more','x',x_angle,y_angle,z_angle)
#	draw_face(sg.face(sg.bottom_torso),physics_points[12],physics_points[13],physics_points[15],physics_points[14],True,'more','x',x_angle,y_angle,z_angle)
#	draw_face(sg.face(sg.bottom_torso),physics_points[12],physics_points[13],physics_points[15],physics_points[14],True,'more','x',x_angle,y_angle,z_angle)
	draw_face(sg.face(sg.front_right_arm,False,sg.front_second_layer_right_arm),physics_points[9],physics_points[16],physics_points[18],physics_points[19],False,'more','x',0,0,0)

	pygame.display.set_caption(f"FPS:{math.floor(clock.get_fps())}")
	pygame.display.update()