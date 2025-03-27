import kivy
kivy.require('1.0.7')

from kivy.app import App


class TestApp(App):
    kv_directory = 'template1'


if __name__ == '__main__':
    TestApp().run()
