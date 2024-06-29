import pygame
import block
from public import *
import bomb

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,id):
        super().__init__()
        self.image={}
        self.x=pos[0]
        self.y=pos[1]
        self.speed=1
        way=['up', 'down', 'left', 'right']
        for w in way:
            self.image[w]=pygame.image.load(
                "img/player"+str(id)+"_"+w+".png"
            )
        self.now=self.image['left']
        self.id=id
        # 玩家的各项属性
        self.HP=1
        self.moreSpeed=0
        self.bombSpand=1
        self.bombMaxNum=1
        self.bombNum=0
        
    def draw(self,screen:pygame.surface.Surface):
        screen.blit(self.now,(self.x,self.y))
        attributes=[self.HP,self.moreSpeed,self.bombSpand,self.bombMaxNum]
        y = 70 if self.id==1 else 350
        font = pygame.font.SysFont("FangSong", 25)
        for i,attr in enumerate(attributes):
            text=font.render(str(attr),True,(0,0,0))
            screen.blit(text,(735,y+i*56.5))

    def isCrush(self,map:block.Map):
        d=28
        for block_ in map.blocks:
            block_:block.Block
            if self.x+d>block_.rect[0] and block_.rect[0]+d>self.x and \
                self.y+d>block_.rect[1] and block_.rect[1]+d>self.y:
                return True
        return False

    def move(self,nowWay,map:block.Map):
        self.now=self.image[nowWay]
        speed=self.speed+self.moreSpeed*0.3
        if nowWay=="up" and self.y>=dx:
            self.y-=speed
        if nowWay=="down" and self.y<=border-px-dx:
            self.y+=speed
        if nowWay=="left" and self.x>=dx:
            self.x-=speed
        if nowWay=="right" and self.x<=border-px-dx:
            self.x+=speed
        # 砖块碰撞检测，如果碰撞了，则恢复移动，即未移动
        crush=self.isCrush(map)
        if not crush:
            return
        if nowWay=="up" :
            self.y+=speed
        if nowWay=="down" :
            self.y-=speed
        if nowWay=="left" :
            self.x+=speed
        if nowWay=="right" :
            self.x-=speed
    # 放置炸弹
    def setBomb(self,bombs:bomb.AllBomb):
        if self.bombMaxNum==self.bombNum:
            return
        c=self.x//px
        r=self.y//px
        mapxy=posToMap((c,r))
        for bomb_ in bombs.bombs:
            bomb_:bomb.Bomb
            #同一位置不可在相近的时刻放置多个炸弹
            if bomb_.rect[0]==mapxy[0] and bomb_.rect[1]==mapxy[1]:
                return
        bomb_=bomb.Bomb(mapxy,self.id,self.bombSpand)
        self.bombNum+=1
        return bomb_