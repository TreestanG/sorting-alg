import sys, random, pygame, math
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Sorting Algorithm')

width, height, tower_width = 600, 600, 2
sorting, finished, si, fi, sort_type = False, False, 0, 0, "bubble"
screen = pygame.display.set_mode((width, height))
towers = random.sample([(x+1)*tower_width for x in range(math.floor(width/tower_width))], math.floor(width/tower_width))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                towers = random.sample([(x+1)*tower_width for x in range(math.floor(width/tower_width))], math.floor(width/tower_width))
                sorting = False
                finished = False
                si = 0
                fi = 0
            else:
                sorting = True
                if event.key == K_q:
                    sort_type = "quick"
                if event.key == K_b:
                    sort_type == "bubble"
    
    if sorting:
        if towers == sorted(towers):
            sorting = False
            finished = True

        if sort_type == "bubble":
            if si < len(towers):
                if min(towers) != towers[si]:
                    gr_ind = towers.index(min(towers[si:]))
                    towers[si], towers[gr_ind] = towers[gr_ind], towers[si]
                    si += 1
        elif sort_type == "quick":
            
            if si < len(towers)-1:
                next_num = towers[si+1]
                if towers[si] > next_num:
                    towers.pop(si+1)
                    for i in towers:
                        if i > next_num:
                            towers.insert(towers.index(i), next_num)
                            break
                si += 1

    if finished: 
        pygame.draw.rect(screen, (0,255,0), (fi*2, height-fi*2, 2, fi*2))
        fi += 1

    else:
        screen.fill((255,255,255))
        for i in range(len(towers)):
            pygame.draw.rect(screen, (0,0,0), (i*tower_width, 0, tower_width, height-towers[i]))
        

    pygame.display.flip()
    pygame.time.Clock().tick(100)