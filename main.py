from kivy.app import App
from kivy.core.window import Window
from piclib import PicLib

Window.size = (1000, 600)
Window.minimum_width, Window.minimum_height = Window.size

class MyApp(App):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    MyApp : PicLib app class
    """
    def build(self):
        """
        build : Builds the application

        Returns:
            PicLib: App layout
        """
        return PicLib()

if __name__ == '__main__':
    MyApp().run()