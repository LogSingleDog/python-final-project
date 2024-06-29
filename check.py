import pygame
import player
import block
import bomb
from public import *
from random import randint

# 检查键盘事件，从而让玩家进行移动与防止炸弹的活动
def check_keyboard(is_play,is_pause,map:block.Map,bombs:bomb.AllBomb,
                   player1:player.Player,player2:player.Player):
    if not is_play or is_pause:
        return
    press=pygame.key.get_pressed()
    # 写成字典的形式，从而便于循环遍历，而不用一个个写，提高代码可读性
    key_p1 = {
        pygame.K_w:'up',pygame.K_s:'down',
        pygame.K_a:'left',pygame.K_d:'right'
    }
    key_p2 = {
        pygame.K_UP:'up',pygame.K_DOWN:'down',
        pygame.K_LEFT: 'left',pygame.K_RIGHT:'right'
    }
    # 放置炸弹
    if press[pygame.K_SPACE]:
        bomb_=player1.setBomb(bombs)
        if bomb_:
            bombs.bombs.add(bomb_)
    if press[pygame.K_KP0]:
        bomb_=player2.setBomb(bombs)
        if bomb_:
            bombs.bombs.add(bomb_)
    # 检测上下左右
    for key in key_p1:
        if press[key]:
            player1.move(key_p1[key],map)
    for key in key_p2:
        if press[key]:
            player2.move(key_p2[key],map)
# 检测爆炸波及的范围
def check_explode(bombs:bomb.AllBomb,map:block.Map,special:pygame.sprite.Group,
                  player1:player.Player,player2:player.Player):
    for bomb_ in bombs.bombs:
        bomb_:bomb.Bomb
        if bomb_.life==cent:
            checkCenter(bomb_,player1,player2)
        if bomb_.life==edge:
            # 上下左右的判断
            t1,t2=checkLeft   (bomb_,map,special,player1,player2)
            t3,t4=checkRight  (bomb_,map,special,player1,player2)
            t5,t6=checkUp     (bomb_,map,special,player1,player2)
            t7,t8=checkDown   (bomb_,map,special,player1,player2)
            if t1 or t3 or t5 or t7:
                player1.HP-=1
            if t2 or t4 or t6 or t8:
                player2.HP-=1
# 碰撞检测collision            
def collision(x,y,player:player.Player,xx=0):
    if -px+xx<x-player.x<px-xx and -px<y-player.y<px+xx:
        return True
    else:
        return False

def checkCenter(bomb:bomb.Bomb,player1:player.Player,player2:player.Player):
    x,y=bomb.rect
    if collision(x,y,player1):
        player1.HP-=1
    if collision(x,y,player2):
        player2.HP-=1

def checkLeft(bomb:bomb.Bomb,map:block.Map,special:pygame.sprite.Group,
              player1:player.Player,player2:player.Player):
    flag1=False
    flag2=False
    for i in range(bomb.spand-1,-1,-1):
        x,y=bomb.rect
        x=x-px*(bomb.spand-i)
        state=sameCheck(x,y,map,special,player1,player2)
        if not state:
            break
        else:
            flag1=(flag1 or state[1])
            flag2=(flag2 or state[2])
    return flag1,flag2

def checkRight(bomb:bomb.Bomb,map:block.Map,special:pygame.sprite.Group,
              player1:player.Player,player2:player.Player):
    flag1=False
    flag2=False
    for i in range(bomb.spand-1,-1,-1):
        x,y=bomb.rect
        x=x+px*(bomb.spand-i)
        state=sameCheck(x,y,map,special,player1,player2)
        if not state:
            break
        else:
            flag1=(flag1 or state[1])
            flag2=(flag2 or state[2])
    return flag1,flag2

def checkUp(bomb:bomb.Bomb,map:block.Map,special:pygame.sprite.Group,
              player1:player.Player,player2:player.Player):
    flag1=False
    flag2=False
    for i in range(bomb.spand-1,-1,-1):
        x,y=bomb.rect
        y=y-px*(bomb.spand-i)
        state=sameCheck(x,y,map,special,player1,player2)
        if not state:
            break
        else:
            flag1=(flag1 or state[1])
            flag2=(flag2 or state[2])
    return flag1,flag2

def checkDown(bomb:bomb.Bomb,map:block.Map,special:pygame.sprite.Group,
              player1:player.Player,player2:player.Player):
    flag1=False
    flag2=False
    for i in range(bomb.spand-1,-1,-1):
        x,y=bomb.rect
        y=y+px*(bomb.spand-i)
        state=sameCheck(x,y,map,special,player1,player2)
        if not state:
            break
        else:
            flag1=(flag1 or state[1])
            flag2=(flag2 or state[2])
    return flag1,flag2

#type[2,5]
def createSpecial(pos,type):
    img="img/tool"+str(type)+".png"
    spe=block.Block(img,pos,type)
    return spe
#上下左右检测中相同的部分，从而代码复用
def sameCheck(x,y,map:block.Map,special:pygame.sprite.Group,
              player1:player.Player,player2:player.Player):
    if not inBox((x,y)):
        return False
    for block in map.blocks:
        if block.rect[0]==x and block.rect[1]==y and block.type==1:
            map.blocks.remove(block)
            type=randint(2,21)
            # type为宝物类型
            if type<=5:
                spe=createSpecial((x,y),type)
                special.add(spe)
    flag1=False
    flag2=False
    if collision(x,y,player1):
        flag1=True
    if collision(x,y,player2):
        flag2=True
    return True,flag1,flag2
#宝物检测
def checkSpecial(special:pygame.sprite.Group,
               player1:player.Player,player2:player.Player):
    for spe in special:
        spe:block.Block
        x,y=spe.rect
        if collision(x,y,player1):
            #判断宝物类型
            if spe.type==2:
                player1.moreSpeed+=1
            if spe.type==3:
                player1.bombSpand+=1
            if spe.type==4:
                player1.bombMaxNum+=1
            if spe.type==5:
                player1.HP+=1
            special.remove(spe)
        if collision(x,y,player2):
            if spe.type==2:
                player2.moreSpeed+=1
            if spe.type==3:
                player2.bombSpand+=1
            if spe.type==4:
                player2.bombMaxNum+=1
            if spe.type==5:
                player2.HP+=1
            special.remove(spe)