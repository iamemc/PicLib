from kivy.uix.boxlayout import BoxLayout
from coloredlabel import ColoredLabel

class TopRow(BoxLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    TopRow : class that represents the top row of the app, which displays the name of the app
    """
    def __init__(self, **kwargs):
        """
        __init__ : TopRow class constructor
        """
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        self.padding = 10

        self.label = ColoredLabel(text='PicLib', font_size=60)

        self.add_widget(self.label)