from pygame.constants import NOFRAME


class upgrade(object):
    def __init__(self,cost,subject,effect,text,name):
        self.cost=cost
        self.subject=subject
        self.effect=effect
        self.text=text
        self.name=name
    