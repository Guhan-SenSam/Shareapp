from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import MagicBehavior, RectangularElevationBehavior
from kivymd.uix.button import MDIconButton,MDFillRoundFlatButton

from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.graphics.texture import Texture
import kivy.metrics

from functools import partial

class MenuScreen():

    def Menuscreenloader(self):
        Mainscreenvar = sm.get_screen('MainScreen')
        self.sender_button = SenderButton()
        self.sender_button.bind(on_release = partial(MenuScreen.Sending_sreen_str_anim, self, identifier=0))
        self.sender_button.ids.layout.children[0].bind(on_release = partial(MenuScreen.Sending_sreen_str_anim, self, identifier=1))
        self.receiver_button = ReceiverButton()
        self.receiver_button.bind(on_release = partial(MenuScreen.Receiving_screen_str_anim, self, identifier=0))
        self.receiver_button.ids.layout.children[0].bind(on_release = partial(MenuScreen.Receiving_screen_str_anim, self, identifier=1))
        self.settings_button = SettingsButton()
        Mainscreenvar.ids.container.add_widget(self.sender_button)
        Mainscreenvar.ids.container.add_widget(self.receiver_button)
        Mainscreenvar.ids.container.add_widget(self.settings_button)
        anim1 = Animation(opacity = 1, duration = .25)
        anim2 = Animation(pos_hint = {'center_x':.5, "center_y":.75}, duration = .3, t='in_out_circ')
        anim3 = Animation(pos_hint = {'center_x':.5, "center_y":.25}, duration = .3, t='in_out_circ')
        anim1.start(self.sender_button)
        anim2.start(self.sender_button)
        anim1.start(self.receiver_button)
        anim3.start(self.receiver_button)
        anim1.start(self.settings_button)


    def Receiving_screen_str_anim(self, caller, *args, identifier):
        Mainscreenvar = sm.get_screen('MainScreen')
        anim1 = Animation(size_hint = (0.38,0.22), duration = .1, t='in_out_circ')
        anim1 += Animation(pos_hint = {'center_x':.5, "center_y":-1}, duration = .3, t='in_out_circ')

        anim2 = Animation(size_hint = (0.38,0.22), duration = .1, t='in_out_circ')
        anim2 += Animation(pos_hint = {'center_x':.5, "center_y":2}, duration = .3, t='in_out_circ')

        anim3 = Animation(opacity = 0, duration = .2)

        anim4 = Animation(angle = 180, duration = .4, t='in_out_circ')

        anim5 = Animation(pos_hint = {'center_x':1.5, 'center_y':.5}, duration = .4, t='in_out_circ')


        if identifier == 0:
            anim2.start(caller.parent.children[2])
            anim1.start(caller)
            anim3.start(caller.parent.children[0])
            anim4.start(Mainscreenvar)
            anim5.start(Mainscreenvar.ids.b_card.parent)

        elif identifier == 1:
            anim2.start(caller.parent.parent.parent.children[2])
            anim1.start(caller.parent.parent)
            anim3.start(caller.parent.parent.parent.children[0])
            anim4.start(Mainscreenvar)
            anim5.start(Mainscreenvar.ids.b_card.parent)

    def Sending_sreen_str_anim(self,caller,*args,identifier):
        Mainscreenvar = sm.get_screen('MainScreen')
        anim1 = Animation(size_hint = (0.38,0.22), duration = .1, t='in_out_circ')
        anim1 += Animation(pos_hint = {'center_x':.5, "center_y":2}, duration = .3, t='in_out_circ')
        anim1.bind(on_complete = partial(MenuScreen.Back_button_appearer,self))

        anim2 = Animation(size_hint = (0.38,0.22), duration = .1, t='in_out_circ')
        anim2 += Animation(pos_hint = {'center_x':.5, "center_y":-1}, duration = .3, t='in_out_circ')

        anim3 = Animation(opacity = 0, duration = .2)

        anim4 = Animation(angle = 0, duration = .4, t='in_out_circ')

        anim5 = Animation(pos_hint = {'center_x':.525, 'center_y':.525}, duration = .4, t='in_out_circ')

        anim6 = Animation(size = (Window.width - Window.width/20, Window.height-Window.height/20),duration = .2)

        if identifier == 0:
            anim2.start(caller.parent.children[1])
            anim1.start(caller)
            anim3.start(caller.parent.children[0])
            anim4.start(Mainscreenvar)
            anim5.start(Mainscreenvar.ids.container.children[3])
            anim6.start(Mainscreenvar.ids.b_card)


        elif identifier == 1:
            print(caller)
            print(caller.parent)
            print(caller.parent.parent)
            print(caller.parent.parent.parent.children)
            anim1.start(caller.parent.parent)
            anim2.start(caller.parent.parent.parent.children[1])
            anim3.start(caller.parent.parent.parent.children[0])
            anim4.start(Mainscreenvar)
            anim5.start(Mainscreenvar.ids.b_card.parent)
            anim6.start(Mainscreenvar.ids.b_card)


    def Back_button_appearer(self,*args):
        self.back_button = MDIconButton(icon = 'arrow-left',
                                        pos_hint = {'center_x':.1, "center_y":.95},
                                        user_font_size = '25sp',
                                        theme_text_color = "Custom",
                                        text_color = (1,1,1,1),
                                        opacity = 0)
        self.back_button.bind(on_release = partial(SenderScreen.back_op,self))
        Mainscreenvar = sm.get_screen('MainScreen')
        Mainscreenvar.ids.container.add_widget(self.back_button)
        anim1 = Animation(opacity = 1, duration = .1)
        anim1.bind(on_complete=partial(SenderScreen.load_ui,self))
        anim1.start(self.back_button)
        for a in range(3):
            Mainscreenvar.ids.container.remove_widget(Mainscreenvar.ids.container.children[1])


class SenderScreen():

    def back_op(self, caller):
        Mainscreenvar = sm.get_screen('MainScreen')
        anim1 = Animation(angle = 45, duration = .4, t='in_out_circ')

        anim2 = Animation(pos_hint = {'center_x':1, 'center_y':.55}, duration = .4, t='in_out_circ')

        anim3 = Animation(size = (kivy.metrics.dp(600), kivy.metrics.dp(900)), duration = .4, t='in_out_circ')

        anim1.start(Mainscreenvar)
        anim2.start(Mainscreenvar.ids.container.children[1])
        anim3.start(Mainscreenvar.ids.b_card)
        Mainscreenvar.ids.container.remove_widget(self.back_button)
        MenuScreen.Menuscreenloader(self)

    def load_ui(self, caller, *args):
        Mainscreenvar = sm.get_screen('MainScreen')
        self.layout_object = FloatLayout()
        self.select_button = SelectButton()
        self.layout_object.add_widget(self.select_button)
        Mainscreenvar.ids.container.children[1].add_widget(self.layout_object)






class BackgroundCard(MDCard):
    pass

class SenderButton(MDCard):
    pass


class ReceiverButton(MDCard):
    pass

class SettingsButton(MDIconButton, MagicBehavior):
    pass

class SelectButton(MDFillRoundFlatButton, RectangularElevationBehavior):
    pass

class MainScreen(Screen):
    angle = NumericProperty(45)



class SettingsScreen(Screen):
    pass


sm = ScreenManager()

class Mainapp(MDApp):
    def build(self):
        self.gradient = Texture.create(size=(1, 2), colorfmt='rgb')
        color1 =[40,35,75,1]
        color2 =[35,60,75,1]
        buf = bytes(color1+color2)
        self.gradient.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

        Builder.load_file('shareapp.kv')
        sm.add_widget(MainScreen(name='MainScreen'))
        return sm

    def on_start(self):
        MenuScreen.Menuscreenloader(self)

Window.size = (360,640)
Mainapp().run()
