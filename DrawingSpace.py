#Keep Coding And change the world and do not forget anything... Not Again..
from kivy.uix.stencilview import StencilView
from kivy.gesture import Gesture,GestureDatabase
from GestureRecorder import line45_str,cross_str,circle_str

class DrawingSpace(StencilView):
    points=[]
    ix,iy,fx,fy=[0]*4
    def __init__(self,*args,**kwargs):
        super(DrawingSpace,self).__init__()
        self.gdb = GestureDatabase()
        self.line_45 = self.gdb.str_to_gesture(line45_str)
        self.circle = self.gdb.str_to_gesture(circle_str)
        self.cross = self.gdb.str_to_gesture(cross_str)
        self.line_135 = self.line_45.rotate(90)
        self.line_225 = self.line_45.rotate(180)
        self.line_315 = self.line_45.rotate(270)
        self.gdb.add_gesture(self.line_45)
        self.gdb.add_gesture(self.line_135)
        self.gdb.add_gesture(self.line_225)
        self.gdb.add_gesture(self.line_315)
        self.gdb.add_gesture(self.circle)
        self.gdb.add_gesture(self.cross)

    def activate(self):
        self.tool_box.disabled=True
        self.bind(on_touch_down=self.down,on_touch_move=self.move,on_touch_up=self.up)

    def deactivate(self):
        self.tool_box.disabled = False
        self.unbind(on_touch_down=self.down, on_touch_move=self.move, on_touch_up=self.up)

    def down(self,ds,touch):
        if self.collide_point(*touch.pos):
            self.points=[touch.pos]
            self.ix=self.fx=touch.x
            self.iy=self.fy=touch.y
        return True

    def move(self,ds,touch):
        if self.collide_point(*touch.pos):
            self.points+=[touch.pos]
            self.min_and_max(touch.x,touch.y)
        return True

    def up(self,ds,touch):
        if self.collide_point(*touch.pos):
            self.points+=[touch.pos]
            self.min_and_max(touch.x,touch.y)
            gesture = self.gesturize()
            recognized = self.gdb.find(gesture,minscore=0.5)
            if recognized:
                self.discriminate(recognized)

        return True

    def gesturize(self):
        gesture = Gesture()
        gesture.add_stroke(self.points)
        gesture.normalize()
        return gesture

    def min_and_max(self,x,y):
        self.ix = min(self.ix,x)
        self.iy = min(self.iy,y)
        self.fx = max(self.fx,x)
        self.fy = max(self.fy,y)

    def discriminate(self,recog):
        if recog[1] == self.cross:
            self.add_stickman()
        elif recog[1] == self.circle:
            self.add_circle()
        elif recog[1] == self.line_45:
            self.add_line(self.ix, self.iy, self.fx, self.fy)
        elif recog[1] == self.line_135:
            self.add_line(self.ix, self.fy, self.fx, self.iy)
        elif recog[1] == self.line_225:
            self.add_line(self.fx, self.fy, self.ix, self.iy)
        elif recog[1] == self.line_315:
            self.add_line(self.fx,self.iy,self.ix,self.fy)

    def add_circle(self):
        cx = (self.ix+self.fx)/2.0
        cy = (self.iy+self.fy)/2.0
        self.tool_box.tool_circle.widgetize(self,cx,cy,self.fx,self.fy)

    def add_line(self,ix,iy,fx,fy):
        self.tool_box.tool_line.widgetize(self,ix,iy,fx,fy)

    def add_stickman(self):
        cx = (self.ix + self.fx) / 2.0
        cy = (self.iy + self.fy) / 2.0
        self.tool_box.tool_stickman.draw(self,cx,cy)
    def on_children(self,instance,value):
        self.status_bar.counter=len(self.children)

