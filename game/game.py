import pygame     #import pygame
from sys import exit   #exit to stop the game
pygame.init()

screen=pygame.display.set_mode((800,400))   #pixel of main screen

pygame.display.set_caption("Saurabh's Game")   #title of game

clock=pygame.time.Clock()    #clock to set fps

text_font=pygame.font.Font('freesansbold.ttf',32)  #font of text
sky_surface=pygame.image.load('Sky.png').convert()  #load image
ground_surface=pygame.image.load('ground.png').convert() #to set the ground surface over the sky surface

snial_surface=pygame.image.load('snail1.png').convert_alpha()   #snail picture
player_surface=pygame.image.load('player_walk_1.png').convert_alpha()   #player walk 
text_surface=text_font.render('My Game',False,"Black")     #text on screen

player_rect=player_surface.get_rect(topleft=(120,212))   #to set the player position


snail_x_pos=600     #snail position initalize

while True:
    for event in pygame.event.get():     #to get the event
        if event.type==pygame.QUIT:  #to stop the game
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))    #blit shows the image one above other 
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(350,100))
    screen.blit(player_surface,player_rect) 
    snail_x_pos-=5
    if snail_x_pos<-100:   #repeat the snail when goes out of screen
        snail_x_pos=800
    screen.blit(snial_surface,(snail_x_pos,265))
    pygame.display.update()   #keep updating the screen till While True
    clock.tick(60)   #set the fps









        
