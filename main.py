# Keep Coding And change the world and do not forget anything... Not Again..
import kivy

kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
import ComicWidgets, ToolBox, GeneralOptions, DrawingSpace, StatusBar
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#1DE9B6")

Builder.load_file('style.kv')
Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('comicwidgets.kv')
Builder.load_file('comiccreater.kv')


class ComicScreenManager(ScreenManager):
    pass


class ComicScreenManagerApp(App):
    def build(self):
        return ComicScreenManager()


if __name__ == "__main__":
    ComicScreenManagerApp().run()
