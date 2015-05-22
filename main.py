import pygame, lib

pygame.init()

pygame.display.set_caption("Function Game")
window = pygame.display.set_mode([1280, 720])

lib.common.loadAll()

clock = pygame.time.Clock()

state = "menu"

Menu = lib.menu("Function Game", window)
Game = lib.game()

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			
	if state == "menu":
		Menu.draw(window)
	if state == "game":
		Game.draw(window)
	
	clock.tick(60)
	pygame.display.update()
	
