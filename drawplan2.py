import pygame
import math

class Brush(object):
    def __init__(self,screen):
        self.screen=screen
        self.size=1
        self.color=(0,0,0)
        self.style=True
        self.drawing=False
        self.last_pos=None
        self.brush=pygame.image.load('images/brush.png').convert_alpha()
        self.brush_now=self.brush.subsurface((0,0),(1,1))

    def start_draw(self,pos):
        self.drawing=True
        self.last_pos=pos

    def end_draw(self):
        self.drawing=False

    def set_style(self,style):
        self.style=style
        print('* set brush style to ',style) 

    def get_style(self):
        return self.style

    def set_size(self,size):
        if size<=1:
            size=1
        elif size>=32:
            size=32
        self.size=size
        print('* set brush size to ',size)
        self.brush_now=self.brush.subsurface((0,0),(size*2,size*2))

    def get_size(self):
        return self.size

    def set_color(self,color):
        self.color=color
        for i in self.brush.get_width():
            for j in self.brush.get_height():
                self.brush.set_at((i,j), color+(self.brush.get_at((i,j)).a,))

    def get_color(self):
        return self.color

    def draw(self,pos):
        if self.drawing:
            for p in self._get_points(pos):
                if self.style:
                    self.screen.blit(self.brush_now,p)
                else:
                    pygame.draw.circle(self.screen,self.color,p,self.size)

    def _get_points(self,pos):
        points=[(self.last_pos[0],self.last_pos[1])]
        len_x=self.pos[0]-self.last_pos[0]
        len_y=self.pos[1]-self.last_pos[1]

        length=math.sqrt(len_x**2+len_y**2)
        step_x=len_x/length
        step_y=len_y/length

        for i in range(length):
            points.append((points[-1][0]+step_x,points[-1][1]+step_y))

        points=[lambda x:(int(x[0]+0.5),int(x[1]+0.5)),points]
        return list(set(points))
        
if __name__=='__main__':
    screen=pygame.display.set_mode((480,800))
    brush=Brush(screen)
    
