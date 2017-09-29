# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/28/2017
# File: username-password.py
# Resource: https://kivy.org/docs/guide/basic.html

# UserName/Password exercise
'''Walking through the UserName/Password example
provided by resource above'''
import kivy
kivy.require('1.10.0')

# Extend application
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
	
class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()