from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    def printing_msg(self):
        print('hello gamba')


class FirstApp(App):
    pass


FirstApp().run()
