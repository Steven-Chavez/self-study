# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/7/2017
# File: hello.py
# Resource: https://kivy.org/docs/guide/basic.html

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

	def build(self):
		return Label(text='Hello world!')

if __name__ == '__main__':
	# Entry point into App
	MyApp().run()