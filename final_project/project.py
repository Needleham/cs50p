import pygame


#COLOURS 
BLACK= (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


pygame.init()
screen = pygame.display.set_mode((640, 240))

running = True
while running:
    for event in pygame,event.get():
        if event.type == pygame.QUIT:
            running = False

        print(event)
    screen.fill(BLACK)
    pygame.display.update()

pygame.quit()


