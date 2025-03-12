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


""" for block in self.body:
        #create a rect and draw the rectangle Rect(x-pos, y-pos, width, height) *IMPORTANT*
        xpos = int(block.x * cell_size)
        ypos = int(block.y * cell_size)
        block_rect = pygame.Rect(xpos, ypos, cell_size, cell_size)
        pygame.draw.rect(screen, (183, 111, 122), block_rect)"""
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BASICS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from pygame.math import Vector2
import random

class snake: 
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('Snake game/Assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Snake game/Assets/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Snake game/Assets/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Snake game/Assets/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Snake game/Assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Snake game/Assets/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Snake game/Assets/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Snake game/Assets/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Snake game/Assets/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Snake game/Assets/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Snake game/Assets/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Snake game/Assets/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Snake game/Assets/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Snake game/Assets/body_bl.png').convert_alpha()

    def draw_snake(self):
       self.update_head_graphics()
       self.update_tail_graphics()
       for index,block in enumerate(self.body):
           #1.We still need a rect for the posititoning
           xpos = int(block.x * cell_size)
           ypos = int(block.y * cell_size)
           block_rect = pygame.Rect(xpos, ypos, cell_size, cell_size)
           #2. what direction is the face heading
           if index == 0:
               screen.blit(self.head, block_rect)
           elif index == len(self.body)- 1:
               screen.blit(self.tail, block_rect)
           else:
              previous_block = self.body[index + 1] - block 
              next_block = self.body[index - 1] - block
              if previous_block.x == next_block.x:
                  screen.blit(self.body_vertical , block_rect )
              elif previous_block.y == next_block.y:
                  screen.blit(self.body_horizontal , block_rect )
              else:
                  if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x ==-1: 
                    screen.blit(self.body_tl , block_rect) # left to top and top to left
                  elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    screen.blit(self.body_bl , block_rect) # left to bottom and bottom to left
                  elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                    screen.blit(self.body_tr , block_rect) # right to top and top to right
                  elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                    screen.blit(self.body_br , block_rect) # right to bottom and bottom to right

    def update_head_graphics(self):
       # refer notes 
       head_relation = self.body[1] - self.body[0]
       if head_relation == Vector2(1,0): self.head = self.head_left
       elif head_relation == Vector2(-1,0): self.head = self.head_right
       elif head_relation == Vector2(0,1): self.head = self.head_up
       elif head_relation == Vector2(0,-1): self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

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
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)
    
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
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
           #reposion the fruit
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # < cell number because the index starts from 0 and goes to 19 not 0 <= body.x <cell_number

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect) 

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3) # 3 is the initial length of the snake
        score_surface = game_font.render(score_text, True ,(56,74,12))    # true means for smooth edges
        score_x = int(cell_size * cell_number - 60) # 60 pixels from the right
        score_y = int(cell_size * cell_number - 40) # 40 pixels from the bottom
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        # we are taking a rectangle midright of the score_rect and center of the score_rect
        # so that the apple will be placed at the left of the score
        apple_rect = apple.get_rect(midright = (score_rect.left , score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left , apple_rect.top , apple_rect.width + score_rect.width + 6 ,
                              apple_rect.height)
        pygame.draw.rect(screen,(167,209,61),bg_rect,2) # rect(draw on screen, color, rect)

        screen.blit(score_surface , score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect, 2)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Snake game/Assets/apple.png').convert_alpha() # convert_alpha is used to convert the image to the format that pygame can understand
game_font = pygame.font.Font('Snake game/Carre-JWja.ttf', 25)  # font size 40


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
