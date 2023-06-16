import sys, random, pygame, math
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Sorting Algorithm')

width, height, tower_width = 600, 600, 2
screen = pygame.display.set_mode((width, height))
towers = random.sample([(x+1)*tower_width for x in range(math.floor(width/tower_width))], math.floor(width/tower_width))
sorting = False
finished = False
si = 0
fi = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                sorting = True
            if event.key == K_UP:
                towers = random.sample([(x+1)*tower_width for x in range(math.floor(width/tower_width))], math.floor(width/tower_width))
                sorting = False
                finished = False
                si = 0
                fi = 0
    
    if sorting:
        
        if towers == sorted(towers, reverse=True):
            sorting = False
            finished = True

        if si < len(towers):
            if max(towers) != towers[si]:
                gr_ind = towers.index(max(towers[si:]))
                towers[si], towers[gr_ind] = towers[gr_ind], towers[si]
                si += 1


    if finished: 
        pygame.draw.rect(screen, (0,255,0), (fi*2, height-fi*2, 2, fi*2))
        fi += 1

    else:
        screen.fill((255,255,255))
        for i in range(len(towers)):
            pygame.draw.rect(screen, (0,0,0), (i*tower_width, 0, tower_width, towers[i]))
        

    pygame.display.flip()
    pygame.time.Clock().tick(100)