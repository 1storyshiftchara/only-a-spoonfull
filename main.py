import pygame
from time import sleep
from filestuff import *
import filestuff
pygame.init()



saveobject = open("data.txt","r")
savedata = []
for line in saveobject:
    line = line.strip("\n")
    savedata.append(int(line))

while (len(savedata)<=10):
    savedata.append(0)
saveobject.close()
print(savedata)



window = pygame.display.set_mode((1000,800))



red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
brown = (160,82,45)
Running = True

keys = []
mousedown = False




font = pygame.font.SysFont('martinaregular',30)


font2 = pygame.font.SysFont('rondaloregular',20)

images = []
images.append(getimage("spoon.png"))
images[0]=pygame.transform.scale(images[0],(200,200))



pygame.display.set_icon(pygame.transform.scale(getimage("spoon2.png"),(32,32)))

spc=1
frame = 0
def buy1():
    if (savedata[0]>(savedata[1]+1)*10):
        savedata[0]-=(savedata[1]+1)*10
        savedata[1]+=1
        
while Running:
    (mousex,mousey)= pygame.mouse.get_pos()
    gridx = int(mousex/50)
    gridy = int(mousey/50)
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
            break
        #sadly python doesnt have switch statements
    if (Running):
        
        pygame.draw.rect(window,brown,pygame.Rect(0,0,600,800))
        pygame.draw.rect(window,white,pygame.Rect(0,0,301,799),1)
        i = 0
        while i <=10:
            pygame.draw.rect(window,white,pygame.Rect(300,50*i,300,50),1)
            i+=1
        pygame.draw.rect(window,white,pygame.Rect(300,550,300,250),1)
        sps = (savedata[1])+(savedata[2]*10)+(savedata[3]*100)+(savedata[4]*1000)+(savedata[5]*10000)+(savedata[6]*100000)+(savedata[7]*1000000)+(savedata[8]*10000000)+(savedata[9]*100000000)+(savedata[10]*1000000000)
        if (frame%60==0):
            savedata[0]+=sps
            
        if (mousedownthisframe and gridx>=1 and gridx<=4 and gridy>=5 and gridy<=8):
            savedata[0]+=spc
        elif (gridx>=5 and gridx<=11 and mousedownthisframe):
            switch = {"0":buy1()}#,"1","2","3","4","5","6","7","8","9","10"}
            switch[str(gridy)]
            #upgrade time
        window.blit(font.render('spoonfulls: {}'.format(savedata[0]), False, white),(50,150))   
        window.blit(font2.render('sps: {}'.format(sps),False,white),(100,200))
        window.blit(font2.render('plastic benders: {}   cost: {}'.format(savedata[1],(savedata[1]+1)*10),False,white),(325,15))
        window.blit(images[0],(50,250))
        
        pygame.display.flip()
        window.fill(black)
        pygame.display.set_caption('{} spoonfulls'.format(savedata[0]))
    sleep(0.016)
    
    frame+=1
    #pretty sure thats like 60 fps
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
