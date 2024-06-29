import pygame

def draw(screen:pygame.surface.Surface):
    # 设置字体
    font=pygame.font.SysFont("FangSong", 25)
    str1="游戏说明"
    str2="玩家1:(英文输入法下)"
    str3="W:上 A:左 S:下 D:右 空格:放炸弹"
    str4="玩家2:(英文输入法下)"
    str5="↑:上 ←:左 ↓:下 →:右 小键盘0:放炸弹"
    strlist=[str1,str2,str3,str4,str5]
    y=287
    # 绘制渲染
    for i,s in enumerate(strlist):
        text=font.render(str(s),True,(0,0,0))
        screen.blit(text,(135,y+i*50))