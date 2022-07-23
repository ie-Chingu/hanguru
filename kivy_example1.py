from ast import Nonlocal, Str
from os import access
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty
 
#import re
 
####日本語対応用コード
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('/System/Library/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')  # 追加分
####日本語対応ここまで
 
class SampleWidget(Widget): #クラスの実装を追記
   text = StringProperty("変化するラベルの例")
   number = NumericProperty(0)
 
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
   def on_press(self):             
       self.text = "ボタンを押した" 
 
class Sample1App(App):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.title = 'Sample'
 
 
if __name__ == '__main__':
   Sample1App().run()