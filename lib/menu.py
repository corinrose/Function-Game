import pygame, lib

class menu():
	def __init__(self, title, surface):	
		self.title				= title
		self.mainbg 			= lib.common.images["resources\menu\main\\bg.png"]
		self.levelselectbg 		= lib.common.images["resources\menu\levelselect\\bg.png"]
		self.creditsbg			= lib.common.images["resources\menu\credits\\bg.png"]
		
		self.windowx			= surface.get_size()[0]
		self.windowy			= surface.get_size()[1]
		
		self.state 				= "main"
		self.mainbuttons		= [lib.button("Level Select", "times", "levelselect"  , (self.windowx/2 - 350, self.windowy/2)      , [300,50] , [lib.common.images["resources\menu\main\\button.png"]       , lib.common.images["resources\menu\main\\buttonhover.png"]       , lib.common.images["resources\menu\main\\buttonpress.png"]]), 
								   lib.button("Credits"     , "times", "credits"      , (self.windowx/2 + 50 , self.windowy/2)      , [300,50] , [lib.common.images["resources\menu\levelselect\\button.png"], lib.common.images["resources\menu\levelselect\\buttonhover.png"], lib.common.images["resources\menu\levelselect\\buttonpress.png"]]),
								   lib.button("Settings"     , "times", "settings"    , (self.windowx/2 + 50 , self.windowy/2 + 150), [300,50], [lib.common.images["resources\menu\levelselect\\button.png"], lib.common.images["resources\menu\levelselect\\buttonhover.png"], lib.common.images["resources\menu\levelselect\\buttonpress.png"]])]
		#self.levelselectbuttons = 
	
	def draw(self, surface):
		if self.state == "main":
			surface.blit(self.mainbg, [0,0])
			for button in self.mainbuttons:
				button.draw(surface)
				if pygame.mouse.get_pressed()[0]:
					if button.checkInside(pygame.mouse.get_pos()):
						self.state = button.state
						
		if self.state == "levelselect":
			surface.blit(self.levelselectbg, [0,0])
			'''
			for button in self.levelselectbuttons:
				button.draw(surface)
				if pygame.mouse.get_pressed()[0]:
					if button.checkInside(pygame.mouse.get_pos()):
						self.state = button.state
			'''
		if self.state == "credits":
			surface.blit(self.creditsbg, [0,0])
			
		if self.state == "settings":
			surface.blit(self.mainbg, [0,0])