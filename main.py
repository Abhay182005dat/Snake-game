import pygame , sys
"""
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

    """


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BASICS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from pygame.math import Vector2
import random

class snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
    def draw_snake(self):
        for block in self.body:
            #create a rect and draw the rectangle Rect(x-pos, y-pos, width, height) *IMPORTANT*
            xpos = int(block.x * cell_size)
            ypos = int(block.y * cell_size)
            block_rect = pygame.Rect(xpos, ypos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)
class Fruit:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1) # create an x and y position also it includes the second parameter 
        self.y = random.randint(0 , cell_number -1)              # so it will never go out of the screen thats why -1
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int (self.pos.y * cell_size),cell_size, cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()

fruit = Fruit()
snake = snake() 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
