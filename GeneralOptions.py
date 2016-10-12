#Keep Coding And change the world and do not forget anything... Not Again..
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,ListProperty

class GeneralOptions(BoxLayout):
    group_mode=False
    translation=ListProperty(None)
    rotation=NumericProperty(0)
    scale = NumericProperty(0)

    def clear(self,instance):
        self.drawing_space.clear_widgets()

    def remove(self,instance):
        ds = self.drawing_space
        if len(ds.children)>0:
            ds.remove_widget(ds.children[0])

    def group(self,instance,value):
        if value=='down':
            self.group_mode=True
        else:
            self.group_mode=False
            self.unselect_all()

    def color(self,instance):
        self.comic_creator.manager.current = 'colorscreen'

    def gesture(self,instance,value):
        if value=='down':
            self.drawing_space.activate()
        else:
            self.drawing_space.deactivate()

    def unselect_all(self):
        for child in self.drawing_space.children:
                child.unselect()

    def on_translation(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
                child.translate(*self.translation)

    def on_rotation(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
                child.rotation=value

    def on_scale(self, instance, value):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
                child.scale = value
