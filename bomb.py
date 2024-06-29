import pygame
from public import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self,pos,id,spand):
        super().__init__()
        # 图片资源，位置，存活期
        self.image=pygame.image.load("img/bomb.png")
        self.rect=pos
        self.life=maxlife
        self.id=id
        self.spand=spand

    def draw(self,screen:pygame.surface.Surface):
        screen.blit(self.image,self.rect)
        if self.life<=edge:
            #上下左右的绘制
            self.drawLeft(screen)
            self.drawRight(screen)
            self.drawUp(screen)
            self.drawDown(screen)

    def drawLeft(self,screen:pygame.surface.Surface):
        left=pygame.image.load("img/bomb_left.png")
        x_img=pygame.image.load("img/bomb_x.png")
        for i in range(self.spand-1,-1,-1):
            x,y=self.rect
            x=x-px*(self.spand-i)
            if not inBox((x,y)):
                break
            if i==0:
                screen.blit(left,(x,y))
            else:
                screen.blit(x_img,(x,y))

    def drawRight(self,screen:pygame.surface.Surface):
        right=pygame.image.load("img/bomb_right.png")
        x_img=pygame.image.load("img/bomb_x.png")
        for i in range(self.spand-1,-1,-1):
            x,y=self.rect
            x=x+px*(self.spand-i)
            if not inBox((x,y)):
                break
            if i==0:
                screen.blit(right,(x,y))
            else:
                screen.blit(x_img,(x,y))

    def drawUp(self,screen:pygame.surface.Surface):
        up=pygame.image.load("img/bomb_up.png")
        y_img=pygame.image.load("img/bomb_y.png")
        for i in range(self.spand-1,-1,-1):
            x,y=self.rect
            y=y-px*(self.spand-i)
            if not inBox((x,y)):
                break
            if i==0:
                screen.blit(up,(x,y))
            else:
                screen.blit(y_img,(x,y))

    def drawDown(self,screen:pygame.surface.Surface):
        down=pygame.image.load("img/bomb_down.png")
        y_img=pygame.image.load("img/bomb_y.png")
        for i in range(self.spand-1,-1,-1):
            x,y=self.rect
            y=y+px*(self.spand-i)
            if not inBox((x,y)):
                break
            if i==0:
                screen.blit(down,(x,y))
            else:
                screen.blit(y_img,(x,y))
# 创建精灵组
class AllBomb:
    def __init__(self,screen) -> None:
        self.bombs=pygame.sprite.Group()
        self.bombs.empty()
        self.screen=screen
    
    def empty(self):
        self.bombs.empty()
    
    def draw(self):
        for bomb_ in self.bombs:
            bomb_:Bomb
            bomb_.draw(self.screen)

    def update(self,player1,player2,is_pause):
        if is_pause:
            return
        for bomb_ in self.bombs:
            bomb_:Bomb
            bomb_.life-=1
            if bomb_.life==cent:
                bomb_.image=pygame.image.load("img/bomb_center.png")
            if bomb_.life<=0:
                if bomb_.id==1:
                    player1.bombNum-=1
                else :
                    player2.bombNum-=1
                self.bombs.remove(bomb_)