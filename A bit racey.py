import pygame
import time
import random
pygame.init()

def dot(x, y):
    game_display.blit(dot_img, (x, y))

def item(item_x, item_y, item_w, item_h, color):
    pygame.draw.rect(game_display, color, [item_x, item_y, item_w, item_h])

def crash():
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render('You Crashed', True, red)
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    game_display.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)

def display_score(score):
    score_font = pygame.font.Font('freesansbold.ttf', 30)
    score_txt = score_font.render('Score: '+ str(score), True, red)
    score_txt_rect = score_txt.get_rect()
    text_width = score_txt.get_width()
    text_height = score_txt.get_height()
    score_txt_rect.center = (text_width/2, text_height/2)
    game_display.blit(score_txt, score_txt_rect)
    pygame.display.update()

def game_loop():
    x = width * 0.48
    y = height * 0.75
    x_change = 0
    item_x = random.randrange(0, width - dot_width)
    item_y = -600
    item_w = 70
    item_h = 100
    item_speed = 3
    score = 0
    running = True
    
    while running:
        prev_score = score
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        if x > width - dot_width or x < 0: #checks if the dot comes in contact with the boundaries
            crash()
            x = width * 0.48
            item_y = 0 - item_h
            item_x = random.randrange(0, width - dot_width)
            score = 0
            item_speed = 3

        if item_y > height: # checks if the block has passed through the screen 
            item_y = 0 - item_h
            item_x = random.randrange(0, width - dot_width)
            score += 1

        #boolean checks
        cond_1 = x in range(item_x, item_x + item_w) or x + dot_width in range(item_x, item_x + item_w)
        cond_2 = (y + 5) in range(item_y , item_y + item_h) or y + dot_height in range(item_y, item_y + item_h)
        if cond_1 == True and cond_2 == True:
            crash()
            x = width * 0.48
            item_y = 0 - item_h
            item_x = random.randrange(0, width - dot_width)
            score = 0
            item_speed = 3

        if (prev_score//10) < (score//10):
            item_speed += 1

        x += x_change
        game_display.fill(blue)
        dot(x, y)
        item(item_x, item_y, item_w, item_h, black)
        item_y += item_speed
        display_score(score)
        pygame.display.update()
        clock.tick(170) 
        
    
#variables
width = 800
height = 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
dot_width = 42
dot_height = 42

clock = pygame.time.Clock()

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('A bit Racey')
dot_img = pygame.image.load('dot_image.PNG')

game_loop()

pygame.quit()
quit()
