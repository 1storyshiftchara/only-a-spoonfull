import pygame, re,math,random
from time import sleep
pygame.init()
def getimage(name):
    try:
        return pygame.image.load(name).convert()
    except Exception as e:
        print(e)

class upgrade(object):
    def __init__(self,cost,text,name):
        self.cost=cost
        self.text=text
        self.name=name

saveobject = open("data.txt","r")
savedata = []
try:
    for line in saveobject:
        line = line.strip("\n")
        if (len(line)==1):
            line=int(line)
        savedata.append((line))

    while (len(savedata)<=14):
        savedata.append(0)
    saveobject.close()

    savedata[12]=list(str(savedata[12]))

    if (len(savedata[12])<10):
        i = len(savedata[12])
        while i<10:
            i+=1
            savedata[12]+="0"



    i=0
    while (i<len(savedata[12])):
        savedata[12][i]=int(savedata[12][i])
        i+=1
except Exception as e:
    print(e)
    time.sleep(2)
    quit()
#loads all the save stuff

upgradetofile=["goldspoon.png","spoon.png","recycle.png","sun.png","recycle.png","hammer.png","hammer.png"]

i=len(savedata[12])-1
curupgrade = 0
for x in savedata[12]:
    if (x==1):
        curupgrade=i+1
        break
    i-=1


window = pygame.display.set_mode((1000,800))

upgrades = [
upgrade(100,"doubles the size of your spoon!","comically larger spoon")
,upgrade(2000,"10x spoonfulls for plastic benders","stronger benders")
,upgrade(5000,"2x spoonfulls for plastic recyclers","bigger bags")
,upgrade(10000,"2x spoonfulls for plastic forgers","hotter forges")
,upgrade(10000,"plastic market","unlocks plastic market")
,upgrade(25000,"2x spoonfulls for plastic factorys","child labor")
,upgrade(50000,"2x spoonfulls for plastic harvestors","child processing plants")
,upgrade(75000,"2x spoonfulls for plastic priests","child sacrifices")
,upgrade(100000,"2x spoonfulls for spoon enlargers","larger resizing")
]
modifiers = [
    None,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
]
def evalmodifiers():
    modifiers[1]=(savedata[12][1]*4)+1
    modifiers[2]=savedata[12][2]+1
    modifiers[3]=savedata[12][3]+1
    modifiers[4]=savedata[12][5]+1
    modifiers[5]=savedata[12][6]+1
    modifiers[6]=savedata[12][7]+1
    modifiers[7]=(savedata[12][8]*0.25)+1
evalmodifiers()



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

images = [pygame.transform.scale(getimage("spoon.png"),(200,200))]


curupgradeimage = None
if (curupgrade<len(upgradetofile)):
    if (upgradetofile[curupgrade]!="hammer.png"):
        curupgradeimage=pygame.transform.scale(getimage(upgradetofile[curupgrade]),(64,64))
    else:
        curupgradeimage=pygame.transform.scale(getimage(upgradetofile[curupgrade]),(32,64))




pygame.display.set_icon(pygame.transform.scale(getimage("spoon2.png"),(32,32)))

spc=1*savedata[12][0]+1
frame = 0


def buy1():
    if (frame!=0):
        if (savedata[0]>=(savedata[1]+1)*savedata[1]+10) and gridy==0:
            savedata[0]-=(savedata[1]+1)*savedata[1]+10
            savedata[1]+=1
    return
def buy2():
    if (frame!=0):
        if (savedata[0]>=(savedata[2]+1)*(savedata[2]*10)+100) and gridy==1:
            savedata[0]-=(savedata[2]+1)*(savedata[2]*10)+100
            savedata[2]+=1
    return
def buy3():
    if (frame!=0):
        if (savedata[0]>=(savedata[3]+1)*(savedata[3]*500)+1000):
            savedata[0]-=(savedata[3]+1)*(savedata[3]*500)+1000
            savedata[3]+=1
    return
def buy4():
    if (frame!=0):
        if (savedata[0]>=(savedata[4]+1)*(savedata[4]*1000)+2500):
            savedata[0]-=(savedata[4]+1)*(savedata[4]*1000)+2500
            savedata[4]+=1
    return
def buy5():
    if (frame!=0):
        if (savedata[0]>=(savedata[5]+1)*(savedata[5]*5000)+5000):
            savedata[0]-=(savedata[5]+1)*(savedata[5]*5000)+5000
            savedata[5]+=1
    return 
def buy6():
    if (frame!=0):
        if (savedata[0]>=(savedata[6]+1)*(savedata[6]*10000)+10000):
            savedata[0]-=(savedata[6]+1)*(savedata[6]*10000)+10000
            savedata[6]+=1
    return
def buy7():
    if (frame!=0):
        if (savedata[0]>=(savedata[7]+1)*(savedata[7]*20000)+20000):
            savedata[0]-=(savedata[7]+1)*(savedata[7]*20000)+20000
            savedata[7]+=1
    return
buyswitch = {"0":buy1,"1":buy2,"2":buy3,"3":buy4,"4":buy5,"5":buy6,"6":buy7}
millnames = ["","K","M","B","T","Quad","Quint","Sext","Sept","Oct","Non","Dec","Und","Duo","Tre"]
def smallify(name):
    cappedspoonfulls=""
    arrspoons = list(str(name))
    if (len(arrspoons)>3):
        length = len(arrspoons)
        divied = math.floor((length-1)/3)*3
        
        thing = name/(pow(10,divied))
        thing*=100
        thing = round(thing)
        thing/=100
        thing = str(int(thing))
        letter = millnames[math.ceil((length-3)/3)]
        
        cappedspoonfulls+=thing
        cappedspoonfulls+=letter
    else:
        cappedspoonfulls+=str(name)
    return cappedspoonfulls




plasticshares = int(savedata[13])
plasticprice = int(savedata[14])
change=1
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


    if (Running):
        
        pygame.draw.rect(window,brown,pygame.Rect(0,0,1000,800))
        pygame.draw.rect(window,white,pygame.Rect(0,0,301,799),1)
        pygame.draw.rect(window,white,pygame.Rect(600,0,399,799),1)
        i = 0
        while i <=10:
            pygame.draw.rect(window,white,pygame.Rect(300,50*i,300,50),1)
            i+=1
        pygame.draw.rect(window,white,pygame.Rect(300,550,300,250),1)
        #RIGHT HERE
        sps = savedata[1]*modifiers[1]
        sps +=(savedata[2]*10)*modifiers[2]
        sps +=(savedata[3]*50)*modifiers[3]
        sps +=(savedata[4]*100)*modifiers[5]
        sps +=(savedata[5]*500)*modifiers[6]
        sps +=(savedata[6]*1000)*modifiers[7]
        sps +=(savedata[7]*5000)*modifiers[8]
        savedata[0]+=sps/60
        
        if (mousedownthisframe):

            if (gridx>=1 and gridx<=4 and gridy>=5 and gridy<=8):
                savedata[0]+=spc

            elif (gridx>=5 and gridx<=11):
                if (gridy<11):
                    try:
                        buyswitch[str(gridy)]()
                    except:
                        pass
                #buy stuff
                else:
                    cost = upgrades[curupgrade].cost
                    if (cost<=savedata[0]):
                        evalmodifiers()
                        #can afford
                        if (curupgrade==0):
                            spc*=2
                        savedata[12][curupgrade]=1
                        savedata[0]-=cost
                        try:
                            thing=getimage(upgradetofile[curupgrade+1])
                            if (thing):
                                if (upgradetofile[curupgrade+1]!="hammer.png"):
                                    curupgradeimage=pygame.transform.scale(thing,(64,64))
                                else:
                                    curupgradeimage=pygame.transform.scale(thing,(32,64))
                                thing=None
                            else:
                                curupgradeimage=False
                        except:
                            curupgradeimage=False
                        curupgrade+=1
                #upgrade stuff
        
            elif (gridx>11):
                gridx = int(mousex/25)
                gridy = int(mousey/25)
                if (gridx==28):
                    if (gridy==5):
                        #buy
                        if (savedata[0]>=plasticprice):
                            savedata[0]-=round(plasticprice)
                            plasticshares+=1
                    elif (gridy==7):
                        #big buy
                        num = math.floor(savedata[0]/round(plasticprice))
                        plasticshares+=num
                        savedata[0]-=num*round(plasticprice)
                        
                    
                elif (gridx==32):
                    if (gridy==5):
                        #sell
                        if (plasticshares>0):
                            plasticshares-=1
                            savedata[0]+=round(plasticprice)
                    elif (gridy==7):
                        #bigsell
                        savedata[0]+=round(plasticprice)*plasticshares
                        plasticshares=0
                pass
        
        
        window.blit(font.render('spoonfulls: {}'.format(smallify(savedata[0])), False, white),(50,150))   
        window.blit(font2.render('sps: {}'.format(sps),False,white),(100,200))
        
        window.blit(font2.render('plastic benders: {}   cost: {}'.format(savedata[1],
        smallify((savedata[1]+1)*savedata[1]+10)),False,white)
        ,(325,15))

        window.blit(font2.render('plastic recyclers: {}  cost:  {}'.format(savedata[2],
        smallify((savedata[2]+1)*(savedata[2]*10)+100))
        ,False,white),(325,65))

        window.blit(font2.render('plastic forge:{}  cost: {}'.format(savedata[3],
        smallify((savedata[3]+1)*(savedata[3]*500)+1000))
        ,False,white),(325,115))
        
        
        window.blit(font2.render('plastic factory: {} cost {}'.format(savedata[4],
        smallify((savedata[4]+1)*(savedata[4]*1000)+2500)),
        False,white),(325,165))
        
        window.blit(font2.render('plastic harvester: {} cost {}'.format(savedata[5],
        smallify((savedata[5]+1)*(savedata[5]*5000)+5000)),
        False,white),(325,215))
        
        window.blit(font2.render('plastic priest: {} cost {}'.format(savedata[6],
        smallify((savedata[6]+1)*(savedata[6]*10000)+10000)),
        False,white),(325,265))
        
        window.blit(font2.render('spoon enlarger: {} cost {}'.format(savedata[7],
        smallify((savedata[7]+1)*(savedata[7]*20000)+20000)),
        False,white),(325,315))
        if (curupgrade>4):
            pygame.draw.rect(window,white,pygame.Rect(600,0,400,200),1)
            window.blit(font2.render('Plastic Market',False,white),(750,25))
            window.blit(font2.render('Shares: {}'.format(plasticshares),False,white),(700,75))
            window.blit(font2.render('Price: {}'.format(round(plasticprice)),False,white),(800,75))
            window.blit(font2.render('Buy',False,white),(700,125))
            window.blit(font2.render('Sell',False,white),(800,125))
            window.blit(font2.render('Buy all',False,white),(700,175))
            window.blit(font2.render('Sell all',False,white),(800,175))
        pass
        #buildings
        try:
            window.blit(font2.render('{}'.format(upgrades[curupgrade].name),False,white),(325,625))
            window.blit(font2.render('{}'.format(upgrades[curupgrade].text),False,white),(325,675))
            window.blit(font2.render('cost: {}'.format(upgrades[curupgrade].cost),False,white),(325,725))
            if (curupgradeimage!=False):
                window.blit(curupgradeimage,(301,551)) 
        except:
            pass
        #upgrades
        window.blit(images[0],(50,250))
        
        pygame.display.flip()
        window.fill(black)
        pygame.display.set_caption('{} spoonfulls'.format(savedata[0]))
        thing=1
        
        plasticprice+=change/60
        if (frame%60==0):
            change=random.randint(1,5)*(math.sin((frame/(240+random.randint(-10,10)))*3.14)*5)
    sleep(0.016)
    frame+=1
    #pretty sure thats like 60 fps

saveobject = open("data.txt","w")
savedata2=savedata.copy()
savedata2.pop(11)
savedata2[13]=plasticshares
savedata2[14]=plasticprice
def writedata(data):
    saveobject.write(str(data))
    saveobject.write("\n")
for x in savedata2:
    writedata(x)

writedata(re.sub(" ","",' '.join(map(str,savedata[12]))))
#converts upgrades list into one line
saveobject.close()
#put code to run when game closed here probably saving stuff    
quit()