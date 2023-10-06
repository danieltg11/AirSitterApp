from kivy.app import App
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.lang import Builder
from kivy.core.window import Window
import os
import sys
kivy.require("1.9.1")
Config.set('graphics', 'resizable', True)
Window.size = 350,600
Builder.load_string('''
<Geren>
    TelaInicial:
    Menu:
    Medidor:
    Configsair:
    Artigos:
    Artigo1:
    Artigo2:
    Artigo3:
    Apoiadores:
    Qmsomos:
    Dados:
    LuzAzul:
    LuzVerde:
    LuzAmarela:
    LuzVermelha:
    InfoLego:

<TelaInicial>
    name:'telainicial'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            size_hint:1.0,0.6
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Image:
                source:'desenho.png'
                size_hint:1.0, 0.3
        BoxLayout:
            size_hint:1.0,0.15
            pos_hint: {'center_x': .5, 'center_y': .5}
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos

            Button:
                size_hint:0.7,1.0
                background_normal:'gg.png'
                background_down:'gg.png'
                on_release: app.root.current = 'menu'
                pos_hint: {'center_x': .5, 'center_y': .5}

        BoxLayout:
            size_hint:1.0,0.35
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos

            Image:
                source:'textinho.png'
                size_hint:1.0, 0.4
<Menu>
    name:'menu'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Image:
                source:'logo.png'
                size:self.texture_size

        BoxLayout:
            padding:10
            spacing:10
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                size:self.texture_size
                background_normal:'oua1.png'
                background_down:'oua2.png'
                on_release: app.root.current = 'medidor'

            Button:
                size:self.texture_size
                background_normal:'dados1.png'
                background_down:'dados2.png'
                on_release:app.root.current = 'dados'
        BoxLayout:
            padding:10
            spacing:10
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                size:self.texture_size
                background_normal:'inf1.png'
                background_down:'inf2.png'
                on_release:app.root.current = 'artigos'
            Button:
                size:self.texture_size
                background_normal:'conf.png'
                background_down:'conf2.png'
                on_release:app.root.current = 'configsair'
<Medidor>
    name:'medidor'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:150
                width:300
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'menu'
            Image:
                source:'inst1.png'
                size:self.texture_size

        BoxLayout:
            padding:10
            spacing:10
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                size:self.texture_size
                background_normal:'azul.png'
                background_down:'azul2.png'
                on_release:app.root.current = 'a'

            Button:
                size:self.texture_size
                background_normal:'verde.png'
                background_down:'verde1.png'
                on_release:app.root.current = 'luzverde'

        BoxLayout:
            padding:10
            spacing:10
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                size:self.texture_size
                background_normal:'amarelo2.png'
                background_down:'amarelo (1).png'
                on_release:app.root.current = 'luzamarela'

            Button:
                size:self.texture_size
                background_normal:'vermelho.png'
                background_down:'vermelho2.png'
                on_release:app.root.current = 'luzvermelha'

<Configsair>
    name:'configsair'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos

            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:150
                width:300
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'menu'
            Image:
                source:'inst2.png'
                size:self.texture_size


        BoxLayout:
            padding:10
            spacing:10
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                size:self.texture_size
                background_normal:'infologo.png'
                background_down:'infologo2.png'
                on_release:app.root.current='infolego'
            Button:
                size:self.texture_size
                background_normal:'leb.png'
                background_down:'leb2.png'
                on_release:app.root.current='qmsomos'
        BoxLayout:
            padding:10
            spacing:10
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                size:self.texture_size
                background_normal:'patroc1.png'
                background_down:'patroc2.png'
                on_release:app.root.current = 'apoiadores'
            Button:
                size:self.texture_size
                background_normal:'sair1.png'
                background_down:'sair2.png'
                on_release:app_close()

<Artigos>
    name:'artigos'
    orientation:'vertical'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            padding:10
            spacing:10
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'menu'
            Button:
                size:self.texture_size
                background_normal:'not1.png'
                background_down:'not2.png'
                on_release:app.root.current = 'artigo1'
            Button:
                size:self.texture_size
                background_normal:'gee1.png'
                background_down:'gee2.png'
                on_release:app.root.current = 'artigo2'
            Button:
                size:self.texture_size
                background_normal:'emi1.png'
                background_down:'emi2.png'
                on_release:app.root.current = 'artigo3'

<Artigo1>
    name:'artigo1'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'artigos'
            Image:
                source:'artigo1.png'
                size:self.texture_size
<Artigo2>
    name:'artigo2'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'artigos'
            Image:
                source:'artigo2.png'
                size:self.texture_size
<Artigo3>
    name:'artigo3'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'artigos'
            Image:
                source:'artigo3.png'
                size:self.texture_size
<Apoiadores>
    name:'apoiadores'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'configsair'
            Image:
                source:'apoi.png'
                size:self.texture_size
<Qmsomos>
    name:'qmsomos'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'configsair'
            Image:
                source:'qmsomos.png'
                size:self.texture_size
<Dados>
    name:'dados'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'menu'
            Image:
                source:'dados.png'
                size:self.texture_size
<LuzAzul>
    name:'a'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'medidor'
            Image:
                source:'luzazul.png'
                size:self.texture_size

<LuzVerde>
    name:'luzverde'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'medidor'
            Image:
                source:'luzverde.png'
                size:self.texture_size
<LuzAmarela>
    name:'luzamarela'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'medidor'
            Image:
                source:'luzamarela.png'
                size:self.texture_size
<LuzVermelha>
    name:'luzvermelha'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'medidor'
            Image:
                source:'luzvermelha.png'
                size:self.texture_size
<InfoLego>
    name:'infolego'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    source:'fundo.png'
                    size: self.size
                    pos: self.pos
            Button:
                pos_hint: {"x":0.05,"y":0.0}
                pos_hint_y:None
                pos_hint_x:None
                size_hint_y:None
                size_hint_x:None
                height:50
                width:100
                background_normal:'voltar.png'
                background_down:'voltar.png'
                on_release:app.root.current = 'configsair'
            Image:
                source:'infolego.png'
                size:self.texture_size


''')




class Geren(ScreenManager):
    def addWidget(self):
        texto = self.ids.texto.text

    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


class Menu(Screen):
    def telamenu(self):
       def __init__(self, **kwargs):
           super(self).__init__(**kwargs)





class PasssTela(Screen):
    pass

class TelaMenu(Screen):
    pass

class Test(App):
    def build(self):
        return Geren()

class Medidor(Screen):
    def medidor(self):
        def __init__(self, **kwargs):
            super(self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)
class Artigos(Screen):
    pass
class Configsair(Screen):
    pass
class Artigo1(Screen):
    pass
class Artigo2(Screen):
    pass
class Artigo3(Screen):
    pass
class Apoiadores(Screen):
    pass
class Qmsomos(Screen):
    pass
class Dados(Screen):
    pass
class LuzAzul(Screen):
    pass
class LuzVerde(Screen):
    pass
class LuzAmarela(Screen):
    pass
class LuzVermelha(Screen):
    pass
class InfoLego(Screen):
    pass
class TelaInicial(Screen):
    pass

Test().run()