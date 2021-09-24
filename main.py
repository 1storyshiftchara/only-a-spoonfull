import pygame
import time 
from spriteloader import *
import re
pygame.init()


saveobject = open("data.txt","r")
savedata = []
for line in saveobject:
    line = line.strip("\n")
    savedata.append(int(line))
if (len(savedata)==0):
    while (len(savedata)<10):
        savedata.append(0)
saveobject.close()

window = pygame.display.set_mode((1000,800))
pygame.display.set_caption('only a spoonful')
imagesurface = pygame.Surface((1000,800))

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
Running = True

keys = []
mousedown = False


images = []
images.append(getimage("spoon.png").convert())
images[0]=pygame.transform.scale(images[0],(200,200))

font = pygame.font.SysFont('martinaregular',30)


spc=1
while Running:
    (mousex,mousey)= pygame.mouse.get_pos()
    mousedownthisframe = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys.append(pygame.key.name(event.key))
        elif event.type == pygame.KEYUP:
            keys.remove(pygame.key.name(event.key))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousedown=True
            mousedownthisframe = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousedown=False
        elif event.type == pygame.QUIT:
            Running = False
            pygame.quit()
        #sadly python doesnt have switch statements
    if (Running):
        if (mousedownthisframe and mousex>106 and mousex<289 and mousey>248 and mousey<457):
            savedata[0]+=spc
        imagesurface.blit(font.render('spoonfulls:{}'.format(savedata[0]), False, white),(100,200))   
        imagesurface.blit(images[0],(100,250))
        window.blit(imagesurface,(0,0))
        pygame.display.flip()
        window.fill(black)
        imagesurface.fill(black)
        time.sleep(0.16)

#to do
    #play "only a spoon full" when spoon clicked
saveobject = open("data.txt","w")
def writedata(data):
    saveobject.write(str(data))
    saveobject.write("\n")
for x in savedata:
    writedata(x)

saveobject.close()
#put code to run when game closed here probably saving stuff    
quit()