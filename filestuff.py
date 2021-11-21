import pygame, re,os

Curfile = os.path.abspath(os.getcwd())
#Imagefile = Curfile + "\sprites\\"
Imagefile = "sprites\\"
def getimage(name):
    # 
    try:
        image = pygame.image.load('{}{}'.format(Imagefile,name)).convert()
        
        return image
    except:
        return False

