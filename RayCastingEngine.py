import pygame , sys , math


'''
#### Varaibles
'''

Width , Height = 500 , 500
FPS = 60

#player
speed = 3
Rspeed = 0.05
PlayerX = 250
PlayerY = 250
PlayerA = 0


pygame.init()
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("ViewPort")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        '''
        #### Drawing on screen
        '''
        screen.fill((30,30,30))

        pygame.draw.circle(screen,(255,255,255),(PlayerX,PlayerY),(PlayerX+5,PlayerY+5),10)

        pygame.display.flip()
        clock.tick(FPS)