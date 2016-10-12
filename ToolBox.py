#Keep Coding And change the world and do not forget anything... Not Again..
import kivy

import math
from kivy.uix.togglebutton import ToggleButton
from Style import NewLine as Line
from ComicWidgets import StickMan,DraggableWidget
from kivy.graphics import Color

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state=='down' and ds.parent.collide_point(touch.x,touch.y):
            x,y = ds.to_widget(touch.x,touch.y)
            self.draw(ds,x,y)
            return True
        return super(ToolButton,self).on_touch_down(touch)

    def draw(self,ds,x,y):
        pass

class ToolStickMan(ToolButton):
    def draw(self,ds,x,y):
        sm = StickMan(width=48,height=48)
        sm.center=(x,y)
        screen_manager = self.parent.comic_creator.manager
        color_picker = screen_manager.color_picker
        sm.canvas.before.add(Color(*color_picker.color))
        ds.add_widget(sm)

class ToolFigure(ToolButton):
    def draw(self,ds,x,y):
        self.ix,self.iy = (x,y)
        screen_manager = self.parent.comic_creator.manager
        color_picker = screen_manager.color_picker
        with ds.canvas:
            Color(*color_picker.color)
            self.figure = self.create_figure(x,y,x+1,y+1)
        ds.bind(on_touch_move=self.update_figure)
        ds.bind(on_touch_up=self.end_figure)

    def update_figure(self,ds,touch):
        ds.canvas.remove(self.figure)
        with ds.canvas:
            self.figure=self.create_figure(self.ix,self.iy,touch.x,touch.y)

    def end_figure(self,ds,touch):
        ds.unbind(on_touch_move=self.update_figure)
        ds.unbind(on_touch_up=self.end_figure)
        ds.canvas.remove(self.figure)
        self.widgetize(ds,self.ix,self.iy,touch.x,touch.y)

    def widgetize(self,ds,ix,iy,fx,fy):
        widget=self.create_widget(ix,iy,fx,fy)
        (ix,iy) = widget.to_local(ix,iy,relative=True)
        (fx, fy) = widget.to_local(fx, fy, relative=True)
        screen_manager = self.parent.comic_creator.manager
        color_picker = screen_manager.color_picker
        widget.canvas.add(Color(*color_picker.color))
        widget.canvas.add(self.create_figure(ix,iy,fx,fy))
        ds.add_widget(widget)

    def create_figure(self,ix,iy,fx,fy):
        pass

    def create_widget(self,ix,iy,fx,fy):
        pass

class ToolLine(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(points=[ix,iy,fx,fy])

    def create_widget(self,ix,iy,fx,fy):
        pos=(min(ix,fx),min(iy,fy))
        size=(abs(fx-ix),abs(fy-iy))
        return DraggableWidget(pos=pos,size=size)

class ToolCircle(ToolFigure):
    def create_figure(self,ix,iy,fx,fy):
        return Line(circle=[ix,iy,math.hypot(ix-fx,iy-fy)])

    def create_widget(self,ix,iy,fx,fy):
        r = math.hypot(ix-fx,iy-fy)
        pos=(ix-r,iy-r)
        size=(2*r,2*r)
        return DraggableWidget(pos=pos,size=size)
