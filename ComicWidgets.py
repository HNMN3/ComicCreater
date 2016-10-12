#Keep Coding And change the world and do not forget anything... Not Again..
from kivy.uix.scatter import Scatter
from kivy.graphics import Line

class DraggableWidget(Scatter):
    def __init__(self,**kwargs):
        self.selected=None
        self.touched=False
        super(DraggableWidget,self).__init__(**kwargs)
    def on_touch_down(self, touch):
        if self.collide_point(touch.x,touch.y):
            self.touched=True
            self.select()
            super(DraggableWidget,self).on_touch_down(touch)
            return True
        return super(DraggableWidget, self).on_touch_down(touch)
    def select(self):
        if not self.selected:
            self.ix=self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line(rectangle=(0,0,self.width,self.height),dash_offset=2)

    def on_pos(self,instance,value):
        if self.selected and self.touched:
            if self.parent is None or type(self.parent) != DraggableWidget:
                return

            go = self.parent.general_options
            go.translation = (self.center_x-self.ix,self.center_y-self.iy)
            self.ix = self.center_x
            self.iy = self.center_y

    def on_rotation(self, instance, value):
        if self.parent is None:
            return
        if self.selected and self.touched:
            go = self.parent.general_options
            go.rotation = value

    def on_scale(self, instance, value):
        if self.parent is None:
            return
        if self.selected and self.touched:
            go = self.parent.general_options
            go.scale = value

    def translate(self,x,y):
        self.center_x = self.ix = self.ix+x
        self.center_y = self.iy = self.iy+y

    def on_touch_up(self, touch):
        if self.selected:
            self.unselect()
            return True
        return super(DraggableWidget, self).on_touch_up(touch)
    def unselect(self):
        self.canvas.remove(self.selected)
        self.selected=None

class StickMan(DraggableWidget):
    pass

