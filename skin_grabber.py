import requests
import base64 
import json
import pygame
import numpy as np

run = ''
front_face = [8,8,8,8]
left_face = [0,8,8,8]
right_face = [16,8,8,8]
top_face = [8,0,8,8]
bottom_face = [16,0,8,8]

front_helmet = [40,8,8,8]
left_helmet = [32,8,8,8]
right_helmet = [48,8,8,8]
top_helmet = [40,0,8,8]
bottom_helmet = [48,0,8,8]

front_torso = [20,20,8,12]
bottom_torso = [28,16,8,4]

front_second_layer_torso = [20,36,8,12]
bottom_second_layer_torso = [28,32,8,4]

front_left_arm = [44,20,4,12]
side_left_arm = [40,20,4,12]
top_left_arm = [44,16,4,4]
bottom_left_arm = [48,16,4,4]

front_second_layer_left_arm = [44,36,4,12]
side_second_layer_left_arm = [40,36,4,12]
top_second_layer_left_arm =   [44,32,4,4]
bottom_second_layer_left_arm = [48,32,4,4]

front_right_arm = [36,52,4,12]
side_right_arm = [40,52,4,12]
top_right_arm = [36,48,4,4]
bottom_right_arm = [40,47,4,4]

front_second_layer_right_arm = [52,52,4,12]
side_second_layer_right_arm = [56,52,4,12]
top_second_layer_right_arm = [52,48,4,4]
bottom_second_layer_right_arm = [56,47,4,4]

face_surface_list = []
def check_array(array1,array2):
	check = 0
	for i in range(len(array1)):
		if array1[i] == array2[i]:
			check+=1
	if check == len(array1):
		return True
	return False
class face():
	def __init__(self,face_img,has_second_layer,second_layer_img):
		self.face_img_x = face_img[0]
		self.face_img_y = face_img[1]
		self.face_img_width = face_img[2]
		self.face_img_height = face_img[3]
		self.name = self
		if has_second_layer == True:
			self.second_layer_face_img_x = second_layer_img[0]
			self.second_layer_face_img_y = second_layer_img[1]
			self.second_layer_face_img_width = second_layer_img[2]
			self.second_layer_face_img_height = second_layer_img[3]
			self.has_second_layer = True
		self.has_second_layer = False
		self.texture = []
	def get_face_surface(self,atlas):
		if len(self.texture) == 0:
			surface  = np.zeros((self.face_img_width,self.face_img_height,3))
			for y in range(self.face_img_height):
				for x in range(self.face_img_width):
					if self.has_second_layer:
						if check_array(atlas[self.second_layer_face_img_x+x][self.second_layer_face_img_y+y],[255,255,255]) == False:
							surface[x][y] = atlas[self.second_layer_face_img_x+x][self.second_layer_face_img_y+y]
						else:
							surface[x][y] = atlas[self.face_img_x+x][self.face_img_y+y]
					else:
						surface[x][y] = atlas[self.face_img_x+x][self.face_img_y+y]
			frame = pygame.surfarray.make_surface(surface)
			self.texture = frame
			return(frame)
		else:
			return(self.texture)
class skin():
	def __init__(self,username):
		self.username = username
		self.model = 'classic'
		self.texture = []
	def get_skin(self):
		global run
		if run != self.username and self.texture == []:#run supposed to be != and self.texture supposed to be == []
			r = requests.get('https://api.mojang.com/users/profiles/minecraft/'+self.username)
			r_dict = r.json()
			profile = requests.get('https://sessionserver.mojang.com/session/minecraft/profile/'+ r_dict['id'])
			skin_dict = profile.json()
			
			base64_string = skin_dict['properties'][0]['value']
			base64_bytes = base64_string.encode("ascii")
			
			character = base64.b64decode(base64_bytes)
			character = character.decode("ascii")
			character = json.loads(character)
			#self.model = character['textures']['SKIN']['metadata']['model']
			skin_url = character['textures']['SKIN']['url']
			with open(f"{self.username}.png",'wb') as f:
				f.write(requests.get(skin_url).content)
			texture_temp = pygame.image.load(f"{self.username}.png")
			texture = pygame.surfarray.array3d(texture_temp)
			run = self.username
			self.texture = texture
			return(texture)
		else:
			return self.texture
#face_surface_list.append(face(front_face,True,front_helmet))
#face_surface_list.append(face(left_face ,True,left_helmet))
#face_surface_list.append(face(right_face,True,right_helmet))
#face_surface_list.append(face(top_face,True,top_helmet))
#face_surface_list.append(face(bottom_face,True,bottom_helmet))
#
#face_surface_list.append(face(front_torso,True,front_second_layer_torso))
#face_surface_list.append(face(bottom_torso,True,bottom_second_layer_torso))
#
#face_surface_list.append(face(front_left_arm,True,front_second_layer_left_arm))
#face_surface_list.append(face(side_left_arm,True,side_second_layer_left_arm))
#face_surface_list.append(face(top_left_arm,True,top_second_layer_left_arm))
#face_surface_list.append(face(bottom_left_arm,True,bottom_second_layer_left_arm))
#
#face_surface_list.append(face(front_right_arm,True,front_second_layer_right_arm))
#face_surface_list.append(face(side_right_arm,True,side_second_layer_right_arm))
#face_surface_list.append(face(top_right_arm,True,top_second_layer_right_arm))
#face_surface_list.append(face(bottom_right_arm,True,bottom_second_layer_right_arm))

