import pygame , sys
# set screen : screen = pygame.display.set_mode((width, height))
pygame.init()
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock() # we have to make sure the game runs at a particular speed at every pc . 
# cause the speed of the game is dependent on the speed of the pc

test_surface = pygame.Surface((100, 200)) # surface is like a canvas where we can draw our elements
while True:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 50, 255))             # fill the screen with white color
    screen.blit(test_surface, (200 ,250))    # blit is used to draw the surface on the screen
    pygame.display.update()                  # we are drawing our elements here
    clock.tick(60)                           # 60 frames per second
