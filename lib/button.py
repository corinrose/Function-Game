import pygame, lib

class button():
	def __init__(self, name, font, state, pos, size, images):
		self.name 	 = name
		self.pos 	 = pos
		self.size 	 = size
		self.font	 = pygame.font.Font("resources\\fonts\\" + font + ".ttf", int(size[0]**.6))
		self.images  = [pygame.transform.scale(images[0] , (size[0], size[1])), #images[0]: unpressed
						pygame.transform.scale(images[1] , (size[0], size[1])), #images[1]: mouse hover
						pygame.transform.scale(images[2] , (size[0], size[1]))]	#images[2]: pressed
		self.state   = state
		
	def draw(self, surface):
		if self.checkInside(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0] == True:
				surface.blit(self.images[2], self.pos)
			else:
				surface.blit(self.images[1], self.pos)
		else:
			surface.blit(self.images[0], self.pos)
		surface.blit(self.font.render(self.name, True, (0, 0, 0)), (self.pos[0] + (self.size[0] - self.font.size(self.name)[0])/2, self.pos[1] + (self.size[1] - self.font.size(self.name)[1])/2))
		
	def checkInside(self, point):
		if point[0] > self.pos[0] and point[0] < self.pos[0] + self.size[0] and point[1] > self.pos[1] and point[1] < self.pos[1] + self.size[1]:
				return True
		else:
			return False
		