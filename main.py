from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import MagicBehavior, RectangularElevationBehavior
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.snackbar import Snackbar

from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
import kivy.metrics
from kivy.utils import platform
from kivy.clock import Clock

import plyer
from jnius import autoclass
import os
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
        self.settings_button.bind(on_press = partial(MenuScreen.Settings_screen_str_anim, self))
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
        try:
            plyer.vibrator.vibrate(0.03)
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
        except:
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
        try:
            plyer.vibrator.vibrate(0.03)
            Mainscreenvar = sm.get_screen('MainScreen')
            anim1 = Animation(size_hint = (0.38,0.22), duration = .1, t='in_out_circ')
            anim1 += Animation(pos_hint = {'center_x':.5, "center_y":2}, duration = .3, t='in_out_circ')
            anim1.bind(on_complete = partial(SenderScreen.load_ui,self))

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
                anim1.start(caller.parent.parent)
                anim2.start(caller.parent.parent.parent.children[1])
                anim3.start(caller.parent.parent.parent.children[0])
                anim4.start(Mainscreenvar)
                anim5.start(Mainscreenvar.ids.b_card.parent)
                anim6.start(Mainscreenvar.ids.b_card)
        except:
            Mainscreenvar = sm.get_screen('MainScreen')
            anim1 = Animation(size_hint = (0.38,0.22), duration = .1, t='in_out_circ')
            anim1 += Animation(pos_hint = {'center_x':.5, "center_y":2}, duration = .3, t='in_out_circ')
            anim1.bind(on_complete = partial(SenderScreen.load_ui,self))

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
                anim1.start(caller.parent.parent)
                anim2.start(caller.parent.parent.parent.children[1])
                anim3.start(caller.parent.parent.parent.children[0])
                anim4.start(Mainscreenvar)
                anim5.start(Mainscreenvar.ids.b_card.parent)
                anim6.start(Mainscreenvar.ids.b_card)

    def Settings_screen_str_anim(self,caller, *args):
        Mainscreenvar = sm.get_screen('MainScreen')
        anim1 = Animation(angle = 0, duration = .4, t='in_out_circ')
        anim2 = Animation(size =Window.size, duration = .4, t='in_out_circ')
        anim3 = Animation(pos_hint = {'center_x':0.5, "center_y":0.5}, duration = .4, t='in_out_circ')
        anim4 = Animation(pos_hint = {'center_x':0.5, "center_y":2}, duration = .4, t='in_out_circ')
        anim5 = Animation(pos_hint = {'center_x':0.5, "center_y":-2}, duration = .4, t='in_out_circ')
        anim1.start(Mainscreenvar)
        anim2.start(Mainscreenvar.ids.b_card)
        anim3.start(Mainscreenvar.ids.container.children[-1])
        anim4.start(Mainscreenvar.ids.container.children[2])
        anim5.start(Mainscreenvar.ids.container.children[1])
        # print(Mainscreenvar.ids.container.children)


class SenderScreen():

    def back_op(self, caller):
        Mainscreenvar = sm.get_screen('MainScreen')
        anim1 = Animation(angle = 45, duration = .4, t='in_out_circ')

        anim2 = Animation(pos_hint = {'center_x':1, 'center_y':.55}, duration = .4, t='in_out_circ')

        anim3 = Animation(size = (kivy.metrics.dp(600), kivy.metrics.dp(900)), duration = .4, t='in_out_circ')

        anim1.start(Mainscreenvar)
        anim2.start(Mainscreenvar.ids.container.children[2])
        anim3.start(Mainscreenvar.ids.b_card)
        self.layout_object.parent.remove_widget(self.layout_object)
        Mainscreenvar.ids.container.remove_widget(self.back_button)
        MenuScreen.Menuscreenloader(self)

    def load_ui(self, caller, *args):
        Mainscreenvar = sm.get_screen('MainScreen')
        self.back_button = MDIconButton(icon = 'arrow-left',
                                        pos_hint = {'center_x':.12, "center_y":.925},
                                        user_font_size = '25sp',
                                        theme_text_color = "Custom",
                                        text_color = (1,1,1,1),
                                        opacity = 0)
        self.back_button.bind(on_release = partial(SenderScreen.back_op,self))

        Mainscreenvar.ids.container.add_widget(self.back_button)
        anim1 = Animation(opacity = 1, duration = .1)
        anim1.start(self.back_button)
        for a in range(3):
            Mainscreenvar.ids.container.remove_widget(Mainscreenvar.ids.container.children[1])


        self.layout_object = FloatLayout(size = Window.size, pos = (0,0))
        self.select_button = SelectButton()
        self.select_button.center_x , self.select_button.center_y = Window.center[0], Window.center[1]
        self.text = Label(text = "Select the files that you \n want to send",
                          pos_hint = {'center_x':.5, "center_y":.5},
                          color = (1,1,1,1),
                          font_name = 'Roboto-Bold',
                          font_size = '25sp',
                          halign = 'center',
                          opacity = 0)
        self.layout_object.add_widget(self.select_button)
        self.layout_object.add_widget(self.text)
        Mainscreenvar.ids.container.add_widget(self.layout_object)
        anim2 = Animation(opacity = 1, pos_hint={'center_x':.5, "center_y":.65}, duration = .3, t='in_out_circ')
        anim3 = Animation(opacity = 1, pos_hint={'center_x':.5, "center_y":.5}, duration = .3, t='in_out_circ')
        anim2.start(self.text)
        anim3.start(self.select_button)


    def ready_files_ui(self, files, *args):
        Mainscreenvar = sm.get_screen('MainScreen')
        self.layout_object.clear_widgets()
        self.file_count = len(files)
        self.total_size = 0
        for path in files:
            val = os.stat(path).st_size
            self.total_size +=val
        self.total_size = round(self.total_size /1000000000, 2)
        self.files_ready_card = FileReadyCard()
        self.files_ready_card.children[1].text = str(self.file_count) + " files"
        self.files_ready_card.children[0].text = str(self.total_size) + "GB"
        self.layout_object.add_widget(self.files_ready_card)

        anim1 = Animation(opacity = 1, duration = .4, t='in_out_circ')
        anim2 = Animation(pos_hint={'center_x':.5, "center_y":.06}, duration = .2)
        anim1.start(self.files_ready_card)
        anim2.start(self.files_ready_card)
        self.animation_object = SearchingAnimation()
        self.animation_object.object_pos1 = Window.center
        self.animation_object.object_pos2 = Window.center
        self.animation_object.object_pos3 = Window.center
        self.animation_object.object_pos4 = Window.center
        self.layout_object.add_widget(self.animation_object)
        self.searching_object = SearchingObject()
        self.layout_object.add_widget(self.searching_object)
        self.started_sending_procedure = 0
        SenderScreen.searcher_animation_1(self, 0)
        Clock.schedule_interval(partial(SenderScreen.searcher_animation_1, self), 2)

    def searcher_animation_1(self, elapsed_time):
        final_size_outer = (Window.size[0]/1.1, Window.size[0]/1.1)
        final_size_inner = (Window.size[0]/1.1, Window.size[0]/1.1)
        final_pos_outer = (Window.center[0]-final_size_outer[0]/2, Window.center[1]-final_size_outer[0]/2)
        final_pos_inner = (Window.center[0]-final_size_inner[0]/2, Window.center[1]-final_size_inner[0]/2)
        anim1 = Animation(object_size1 = final_size_outer, object_pos1= final_pos_outer, duration=1, t='out_circ')
        anim2 = Animation(object_size2 = final_size_inner, object_pos2= final_pos_inner, duration=1.2, t='out_circ')
        anim3 = Animation(duration = .5)
        anim3 += Animation(object_size3 = final_size_outer, object_pos3= final_pos_outer, duration=1, t='out_circ')
        anim4 = Animation(duration = .5)
        anim4 += Animation(object_size4 = final_size_outer, object_pos4= final_pos_outer, duration=1.2, t='out_circ')
        anim5 = Animation(size_hint = (0.3, 0.15), elevation = 14,duration=1.2, t='in_out_circ')
        anim1.start(self.animation_object)
        anim2.start(self.animation_object)
        anim3.start(self.animation_object)
        anim4.start(self.animation_object)
        anim5.start(self.searching_object)
        anim4.bind(on_complete = partial(SenderScreen.size_reset, self))
        if self.started_sending_procedure == 0:
            Senderlogic.sending(self)

    def size_reset(self, a, caller):
        anim3 = Animation(object_size1 = (0,0), object_pos1 = Window.center,
                        object_size2 = (0,0), object_pos2 = Window.center,
                        object_size3 = (0,0), object_pos3 = Window.center,
                        object_size4 = (0,0), object_pos4 = Window.center,
                        duration = .1)
        anim4 = Animation(size_hint=(0.25,0.1), elevation = 10,duration = .2)
        anim3.start(self.animation_object)
        anim4.start(self.searching_object)



class Senderlogic():

    def sending(self):
        pass












class BackgroundCard(MDCard):
    pass

class SenderButton(MDCard):
    pass


class ReceiverButton(MDCard):
    pass

class SettingsButton(MDIconButton, MagicBehavior):
    pass

class SelectButton(MagicBehavior, MDFloatingActionButton):

    def open_filemanager(caller, self):
        self.files = plyer.filechooser.open_file(on_selection = partial(caller.android_selected_files,self), multiple = True)

    def android_selected_files(caller,self,selection):
        anim1 = Animation(opacity = 0, duration = .3)
        anim2 = Animation(opacity = 0, duration = .3)
        anim1.bind(on_complete = partial(SenderScreen.ready_files_ui,self, selection))
        anim1.start(self.text)
        anim2.start(self.select_button)

class FileReadyCard(MDCard):
    pass

class SearchingObject(MDCard):
    pass

class SearchingAnimation(FloatLayout):
    pass
class MainScreen(Screen):
    angle = NumericProperty(45)


class SettingsScreen(Screen):
    pass


sm = ScreenManager()

class Mainapp(MDApp):
    def build(self):
        self.gradient = Texture.create(size=(1, 2), colorfmt='rgb')
        color1 =[45,40,80,1]
        color2 =[45,75,90,1]
        buf = bytes(color1+color2)
        self.gradient.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

        Builder.load_file('shareapp.kv')
        sm.add_widget(MainScreen(name='MainScreen'))
        return sm

    def on_start(self):
        MenuScreen.Menuscreenloader(self)

if kivy.utils.platform != 'android':
    Window.size = (360,640)

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.ACCESS_FINE_LOCATION,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE,
        Permission.INTERNET,
    ])
Mainapp().run()
