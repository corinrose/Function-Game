import pygame, os

images  = {}
sounds  = {}

def loadAll():
	resources = list(os.walk("resources"))
	totalFiles = 0
	print "Loading " + str(len(resources)) + " files."
	for file in resources:
		for i in range(0, len(file[2])):
			if file[2][i] == "Thumbs.db":
				continue
			path = file[0] + "\\" + file[2][i]
			if file[2][0][-3] == "p": 							#put png's in the images
				images[path] = pygame.image.load(path)
			elif file[2][0][-3] == "w":							#put wav's in sounds
				sounds[path] = pygame.mixer.music.load(path)
	