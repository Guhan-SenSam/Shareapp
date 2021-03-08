from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

from functools import partial

class Test_Loader(FloatLayout):

    def __init__(self, **kwargs):
        super(Test_Loader, self).__init__(**kwargs)
        self.starting_angle = 0
        self.ending_angle = 0


        with self.canvas:
            Color(0,1,1,1)
            Ellipse(angle_start = 0,
                    angle_end = 0)
        Clock.schedule_once(partial(Test_Loader.animator, self))


    def animator(self, *args):
        anim1 = Animation(ending_angle = 360, duration = 2)
        anim1.start(self)

class CircleApp(MDApp):
    def build(self):
        return Test_Loader()

CircleApp().run()
