import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,img,pos):
        super().__init__()
        self.image=pygame.image.load(img)
        self.rect=pos

    def draw(self,screen:pygame.surface.Surface):
        screen.blit(self.image,self.rect)
    #判断是否鼠标是否在按钮上方
    def on_it(self):
        px,py=pygame.mouse.get_pos()
        x,y=self.rect
        w,h=self.image.get_size()
        ans = ( px>x and px<x+w ) and (py>y and py<y+h )
        return ans
    #判断是否点击
    def click(self):
        if self.on_it():
            press=pygame.mouse.get_pressed()
            if press[0]:
                return True
            else :
                return False
        return False

    