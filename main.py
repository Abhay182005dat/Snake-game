import pygame , sys
# set screen : screen = pygame.display.set_mode((width, height))
pygame.init()
screen = pygame.display.set_mode((400, 500))

clock = pygame.time.Clock() # we have to make sure the game runs at a particular speed at every pc . 
# cause the speed of the game is dependent on the speed of the pc

test_surface = pygame.Surface((100, 200)) # surface is like a canvas where we can draw our elements
test_surface.fill((0, 0, 255)) # fill the surface with red color
#xpos = 200
#test_rect = pygame.Rect(100,200,100,100)
test_rect = test_surface.get_rect(topright = (200, 250)) # xenter , top right etc ..
while True:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    #pygame.draw.ellipse(screen, (255, 0, 0), test_rect)  # draw a rectangle on the screen
    #xpos+=1                                 # fill the screen with white color
    #screen.blit(test_surface, (xpos ,250)) 
    #screen.blit(test_surface, (250 ,xpos))  # blit is used to draw the surface on the screen
    screen.blit(test_surface, test_rect)
    test_rect.right += 1
    pygame.display.update()                  # we are drawing our elements here
    clock.tick(60)                           # 60 frames per second
    
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BASICS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~