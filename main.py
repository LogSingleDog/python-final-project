import pygame
import button
import player
import block
import bomb
import time
import helps
from public import *
from check import *

mapSize=mapWidth,mapHeight=780,600

def init(screen):
    bombs=bomb.AllBomb(screen)
    bombs.empty()
    comMap=block.Map(screen)
    comMap.build()
    player1=player.Player((15,15),1)
    player2=player.Player((555,555),2)
    special=pygame.sprite.Group()
    special.empty()
    return bombs,comMap,player1,player2,special

def main():
    pygame.init()
    # 生成屏幕
    screen=pygame.display.set_mode(mapSize)
    #设置标题
    pygame.display.set_caption("经典泡泡堂")
    #背景等图片的加载
    index=pygame.image.load("img/index.png")
    bg=pygame.image.load("img/background.png")
    state=pygame.image.load("img/state.png")
    pause_choose=pygame.image.load("img/pause_choose.png")
    helpboard=pygame.image.load("img/help_board.png")
    win1=pygame.image.load("img/player1_win.png")
    win2=pygame.image.load("img/player2_win.png")
    title=pygame.image.load("img/title.png")
    #首页，帮助页的按钮
    start=button.Button("img/play.png",(150,430))
    help=button.Button("img/help.png",(450,430))
    close=button.Button("img/close.png",(688,250))
    #游戏页的按钮
    resume=button.Button("img/resume.png",(210,155))
    restart=button.Button("img/restart.png",(210,265))
    end=button.Button("img/exit.png",(210,375))
    pause=button.Button("img/pause.png",(737,555))
    #背景音乐
    pygame.mixer.music.load('bgm/bgm.mp3')
    pygame.mixer.music.play(loops=-1)
    #状态设置，用来判断现在处于何种游戏状态
    is_play=False
    is_pause=False
    is_index=True
    is_help=False
    #初始化炸弹组，地图，两个玩家
    bombs,comMap,player1,player2,special=init(screen)
    #是否结束游戏，关闭进程
    exit = False
    # 游戏循环
    while not exit:
        # 检测到关闭，则退出
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
        # 检测各种键盘事件，并更新
        check_keyboard(is_play,is_pause,comMap,bombs,player1,player2)
        # 以下是对于鼠标事件的检测
        # 在首页
        if is_index:
            if start.click():
                is_play=True
                is_index=False
            if help.click():
                is_help=True
                is_index=False
        # 在游玩页
        if is_play :
            bombs.update(player1,player2,is_pause)
            # 爆炸检测
            check_explode(bombs,comMap,special,player1,player2)
            # 宝物检测，判断玩家是否获取宝物
            checkSpecial(special,player1,player2)
            if pause.click():
                is_pause=True
        # 在暂停页
        if is_pause:
            # 回到游戏
            if resume.click():
                is_pause=False
            # 重新开始游戏
            if restart.click():
                is_pause=False
                bombs,comMap,player1,player2,special=init(screen)
            # 退出游戏
            if end.click():
                is_play=False
                is_index=True
                is_pause=False
        # 在帮助页
        if is_help:
            if close.click():
                is_help=False
                is_index=True
        #以下是画面更新部分
        if is_index :
            screen.fill((170,85,85))
            screen.blit(index,(0,0))
            screen.blit(title,(88,80))
            start.draw(screen)
            help.draw(screen)
        if is_help:
            screen.fill((170,85,85))
            screen.blit(index,(0,0))
            screen.blit(title,(88,80))
            screen.blit(helpboard,(88,250))
            helps.draw(screen)
            close.draw(screen)
        if is_play:
            screen.blit(bg,(0,0))
            screen.blit(state,(600,0))
            pause.draw(screen)
            comMap.draw()
            special.draw(screen)
            bombs.draw()
            player1.draw(screen)
            player2.draw(screen)  
        if is_pause:
            screen.blit(pause_choose,(100,100))
            resume.draw(screen)
            restart.draw(screen)
            end.draw(screen)
        # 画布更新
        pygame.display.update()
        # 判断是否有玩家的HP小于等于0，则判断游戏结束
        if is_play:
            if player1.HP<=0:
                screen.blit(win2,(88.5,150))
            if player2.HP<=0:
                screen.blit(win1,(88.5,150))
            if player1.HP<=0 or player2.HP<=0:
                pygame.display.update()
                is_play=False
                is_index=True
                time.sleep(2)
                bombs,comMap,player1,player2,special=init(screen)
#运行主函数
if __name__ == "__main__":
    main()