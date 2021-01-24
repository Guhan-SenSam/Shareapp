from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color
from kivy.animation import Animation

from kivy.uix.floatlayout import FloatLayout

class Test_Loader(FloatLayout):

    def __init__(self, **kwargs):
        super(Test_Loader, self).__init__(**kwargs)
        self.starting_angle = 0
        self.ending_angle = 360


        with self.canvas:
            Color(0,1,1,1)
            Ellipse(angle_start = self.starting_angle,
                    angle_end = self.ending_angle)
        for a in range(360):
            self.starting_angle = a
            print(self.starting)

class CircleApp(MDApp):
    def build(self):
        return Test_Loader()

CircleApp().run()
