import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChildApp(GridLayout):
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__(**kwargs)
        self.cols = 2
        

        # Student Name
        self.add_widget(Label(text='Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        
        # Student Marks
        self.add_widget(Label(text='Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)
        
        # Student Gender
        self.add_widget(Label(text='Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = 'click me')
        self.press.bind(on_press = self.on_click)
        self.add_widget( self.press)

    def on_click(self, instance):
        print("Name of the student :"+self.s_name.text )
        print("marks:"+self.s_marks.text)
        print("gender of the student :"+ self.s_gender.text )
        print("")
        

class PyanaApp(App):
    def build(self):
        return ChildApp()

if __name__ == "__main__":
    PyanaApp().run()
