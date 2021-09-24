import os, pygame, re
sprites = []
Curfile = __file__
Curfile = re.sub("spriteloader.py", "",Curfile)
Imagefile = Curfile + "sprites"
Imagefile = re.sub("/",r'\\',Imagefile)
Imagefile += r'\''
Imagefile = re.sub("'","",Imagefile)

# yet its dumb no i dont know how to change it

print("images: "+Imagefile)

def getimage(name):
    # 
    try:
        image = pygame.image.load('{}{}'.format(Imagefile,name)).convert()
        return image
    except:
        return None