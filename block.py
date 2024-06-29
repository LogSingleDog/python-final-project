import pygame
from random import randint
from public import *

class Block(pygame.sprite.Sprite):
    def __init__(self,img,pos,type):
        super().__init__()
        self.image=pygame.image.load(img)
        self.rect=pos
        self.type=type
    
    def draw(self,screen:pygame.surface.Surface):
        screen.blit(self.image,self.rect)

class Map:
    def __init__(self,screen):
        #精灵类管理砖块
        self.blocks=pygame.sprite.Group()
        self.blocks.empty()
        self.screen=screen
    
    def empty(self):
        self.blocks.empty()

    # 整幅图是19*19的大小所以是[0,18]
    def build(self):
        self.empty()
        barriers=[]
        # 不可被毁坏的固定砖块
        for c in range(1,18,4):
            for r in range(1,18,4):
                barriers.append((c,r))
        for barrier in barriers:
            block=getImage("img/barrier.png",barrier,-1)
            self.blocks.add(block)
        # 角落不可有砖块否则玩家无法进行游戏
        cant=[(0,0),(0,1),(1,0),(18,18),(18,17),(17,18)]
        boxes=[]
        # 生成宝箱150个
        for _ in range(150):
            c,r=0,0
            # 生成位置直到该位置从来没有出现过
            while (c,r) in cant or (c,r) in barriers or (c,r) in boxes:
                c=randint(0,18)
                r=randint(0,18)
            boxes.append((c,r))
        for box in boxes:
            boxType=randint(0,3)
            block=getImage("img/box"+str(boxType)+".png",box,1)
            self.blocks.add(block)
         
    def draw(self):
        self.blocks.draw(self.screen)

def getImage(img,pos,type):
    x,y=posToMap(pos)
    block=Block(img,(x,y),type)
    return block