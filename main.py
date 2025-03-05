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
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            #create a rect and draw the rectangle Rect(x-pos, y-pos, width, height) *IMPORTANT*
            xpos = int(block.x * cell_size)
            ypos = int(block.y * cell_size)
            block_rect = pygame.Rect(xpos, ypos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)
   
    def move_snake(self):
        if self.new_block == True:
            bodycopy = self.body[:]
            bodycopy.insert(0,bodycopy[0] + self.direction)
            self.body = bodycopy[:]
            self.new_block = False
        else :
            bodycopy = self.body[:-1] # first element to the second last element
            bodycopy.insert(0,bodycopy[0] + self.direction)
            self.body = bodycopy[:]

    def add_block(self):
        self.new_block = True

class Fruit:
    def __init__(self):
        self.randomize()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int (self.pos.y * cell_size),cell_size, cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0,cell_number - 1) # create an x and y position also it includes the second parameter
        self.y = random.randint(0 , cell_number -1)     # so it will never go out of the screen thats why -1
        self.pos =  Vector2(self.x, self.y)        

class MAIN:
    def __init__(self):
        self.snake = snake()
        self.fruit = Fruit()

    def update(self):   
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
           #reposion the fruit
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # < cell number because the index starts from 0 and goes to 19

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
 
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) # every 150 milliseconds the event will be triggered
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN: # check for specific keys (if you press any button)
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)  # -ve y direction is up
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)  # +ve y direction is down
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
