#Keep Coding And change the world and do not forget anything... Not Again..
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.label import Label
class StatusBar(ButtonBehavior,BoxLayout):
    counter = NumericProperty(0)
    previous_counter=0

    def on_counter(self,instance,value):
        if value==0:
            self.msg_label.text = "Drawing space cleared"
        elif value-1 == self.__class__.previous_counter:
            self.msg_label.text = "Widget added"
        elif value+1== StatusBar.previous_counter:
            self.msg_label.text = "Widget removed"

        self.__class__.previous_counter=value

    def on_press(self):
        the_content = Label(text="HNMN3")
        the_content.color = (1,1,1,1)
        popup = Popup(title='The Comic Creator',
                      content=the_content,size_hint=(None,None),
                      size=(350,150))
        popup.open()