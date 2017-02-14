import pygame
from pygame.locals import *
import math
import sys

#画笔类
class Brush:
    def __init__(self,screen):
        #画笔所在窗口
        self.screen=screen
        #画笔颜色
        self.color=(0,0,0)
        #画笔大小
        self.size=1
        #是否正在绘制
        self.drawing=False
        #开始点
        self.last_pos=None
        #画笔类型
        self.style=True
        #笔刷图片
        self.brush=pygame.image.load('images/brush.png').convert_alpha()
        #当前笔刷图（截图片上一块，从（0，0）开始，长宽（1，1）的地方）
        self.brush_now=self.brush.subsurface((0,0),(1,1))
        
    def start_draw(self,pos):
        #开始绘制时，将笔刷drawing设置为True
        self.drawing=True
        #
        self.last_pos=pos
        
    def end_draw(self):
        #结束绘制时，将笔刷drawing设置为True
        self.drawing=False
        
    def set_brush_style(self,style):
        #设置笔刷样式
        print('* set brush style to',style)
        self.style=style
        
    def get_brush_style(self):
        #获取笔刷样式
        return self.style
    
    def get_current_brush(self):
        #获取当前笔刷
        return self.brush_now
    
    def set_size(self,size):
        #设置画笔大小 1-32
        if size<1:
            size=1
        elif size>32:
            size=32
        print('* set brush size to',size)
        self.size=size
        #设置笔刷为笔刷图的（0，0）开始，长宽（size*2,size*2）的大小
        self.brush_now=self.brush.subsurface((0,0),(size*2,size*2))
        
    def get_size(self):
        #获取画笔大小
        return self.size
    
    def set_color(self,color):
        #设置画笔颜色
        self.color=color 
        for i in range(self.brush.get_width()):
            for j in range(self.brush.get_height()):
                #循环设置笔刷图片每个点的颜色 （i,j）为点，color为颜色，self.brush.get_at((i,j)).a应该是这个点的一个变量
                self.brush.set_at((i,j),color+(self.brush.get_at((i,j)).a,))
                                
    def get_color(self):
        #获取笔刷颜色
        return self.color
    
    def draw(self,pos):
        if self.drawing:
            #正在绘制时，循环每个需要绘制的点，如果用png笔刷，用self.brush_now填充
            #用铅笔画，则画circle
            for p in self._get_points(pos):
                if self.style:
                    self.screen.blit(self.brush_now,p)
                else:
                    pygame.draw.circle(self.screen,self.color,p,self.size)
            #结束后将last_pos设置为当前pos
            self.last_pos=pos
        
    def _get_points(self,pos):
        #将开始绘制的点转为[(x,y)]格式
        points=[(self.last_pos[0],self.last_pos[1])]
        #当前点与开始点之间的x,y差值
        len_x=pos[0]-self.last_pos[0]
        len_y=pos[1]-self.last_pos[1]
        #两点连线的长度：平方相加开平方
        length=math.sqrt(len_x**2+len_y**2)
        #平均每个length x,y增长数
        step_x=len_x/length
        step_y=len_y/length
        for i in range(int(length)):
            #将需要填充的点放入points
            points.append((points[-1][0]+step_x,points[-1][1]+step_y))
        #points中每个点加0.5像素
        points=map(lambda x: (int(0.5+x[0]),int(0.5+x[1])),points)
        #去重返回
        return list(set(points))
    
class Menu:
    def __init__(self,screen):
        self.screen=screen
        #画笔
        self.brush=None
        #颜色
        self.colors=[
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff),
            (0x00, 0x00, 0x00), (0x80, 0x80, 0x80)
            ]
        
        self.colors_rect=[]
        #循环所有颜色，将颜色所占矩形放入colors_rect
        for (i,rgb) in enumerate(self.colors):
            rect=pygame.Rect(10+i%2*32,254+i//2*32,32,32)
            self.colors_rect.append(rect)
        #加载画笔图
        self.pens=[
            pygame.image.load('images/pen1.png').convert_alpha(),
            pygame.image.load('images/pen2.png').convert_alpha()
        ]
        self.pens_rect=[]
        #循环画笔图，将画笔图所占矩形放入pens_rect
        for (i,img) in enumerate(self.pens):
            rect=pygame.Rect(10,10+i*64,64,64)
            self.pens_rect.append(rect)
        #加载调整大小的按钮图
        self.sizes=[
            pygame.image.load('images/big.png').convert_alpha(),
            pygame.image.load('images/small.png').convert_alpha()
        ]

        self.sizes_rect=[]
        #循环将调整大小按钮图放入sizes_rect
        for (i,img) in enumerate(self.sizes):
            rect=pygame.Rect(10+i*32,138,32,32)
            self.sizes_rect.append(rect)
            
    def set_brush(self,brush):
        #设置画笔
        self.brush=brush
        
    def draw(self):
        #绘制画笔按钮
        for (i,img) in enumerate(self.pens):
            self.screen.blit(img,self.pens_rect[i].topleft)
        #绘制调整大小按钮
        for (i,img) in enumerate(self.sizes):
            self.screen.blit(img,self.sizes_rect[i].topleft)
        #绘制一个矩形区域，边框为黑色
        self.screen.fill((255,255,255),(10,180,64,64))
        pygame.draw.rect(self.screen,(0,0,0),(10,180,64,64),1)
        size=self.brush.get_size()
        #矩形区域中点
        x=10+32
        y=180+32
        #在矩形区域绘制笔刷大小
        if self.brush.get_brush_style():
            x=x-size
            y-=size
            self.screen.blit(self.brush.get_current_brush(),(x,y))
        else:
            pygame.draw.circle(self.screen,self.brush.get_color(),(x,y),size)
        #绘制调色板
        for (i,rgb) in enumerate(self.colors):
            pygame.draw.rect(self.screen,rgb,self.colors_rect[i])
            
    def click_button(self,pos): 
        for (i,rect) in enumerate(self.pens_rect):
            #检测pos点是否在rect内
            if rect.collidepoint(pos):
                self.brush.set_brush_style(bool(i))
                return True
        #检测是否点击调整笔刷大小按钮
        for (i,rect) in enumerate(self.sizes_rect):
            if rect.collidepoint(pos):
                if i:
                    self.brush.set_size(self.brush.get_size()-1)
                else:
                    self.brush.set_size(self.brush.get_size()+1)
                return True
        #检测是否点击调色板
        for (i,rect) in enumerate(self.colors_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.colors[i])
                return True
        
        return False
    

class Painter:
    def __init__(self):
        #创建画布
        self.screen=pygame.display.set_mode((800,600))
        pygame.display.set_caption('Painter')

        self.clock=pygame.time.Clock()
        #创建画笔
        self.brush=Brush(self.screen)
        #创建菜单
        self.menu=Menu(self.screen)
        #设置菜单的画笔对象
        self.menu.set_brush(self.brush)

    def run(self):
        #白色填充画布
        self.screen.fill((255,255,255))
        while True:
            #设置帧数
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    return
                elif event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        self.screen.fill((255,255,255))
                elif event.type==MOUSEBUTTONDOWN:
                    #event.pos[0]<=74时不在有效区域，检测是否点击菜单
                    if event.pos[0]<=74 and self.menu.click_button(event.pos):
                        pass
                    elif event.pos[0]>74:
                        #开始绘制
                        self.brush.start_draw(event.pos)
                elif event.type==MOUSEMOTION:
                    #鼠标移动时调用画笔draw方法
                    self.brush.draw(event.pos)
                elif event.type==MOUSEBUTTONUP:
                    #鼠标抬起调用结束绘制方法
                    self.brush.end_draw()
            #绘制菜单
            self.menu.draw()
            #更新画布
            pygame.display.update()

def main():
    app=Painter()
    app.run()

if __name__=='__main__':
    main()

 
