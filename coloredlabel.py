from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class ColoredLabel(Label):
    """
    55881 Eduardo Carvalho
    55738 Joao Milagaia
    
    ColoredLabel is a subclass of Label that permits the definition of a 
    background color easily.
    """
    def __init__(self, background_color=(0,0,0,1), color=(1,1,1,1), **kwargs):
        """
        __init__ : ColoredLabel class constructor

        Args:
            background_color (tuple, optional): Color of the Label's background. Defaults to (0,0,0,1) aka Black.
            color (tuple, optional): Color of the Label's text. Defaults to (1,1,1,1) aka White.
        """
        super().__init__(**kwargs)
        self.color = color
        self.italic = True
        with self.canvas.before:
            Color(*background_color)
            self.rect = Rectangle()
            self.rect.pos = self.pos
            self.rect.size = self.size
        self.bind(pos=self.__update_rect, size=self.__update_rect)

    @staticmethod
    def __update_rect(instance, value):
        """
        __update_rect : updates the rectangles

        Args:
            instance (ColoredLabel): ColoredLabel instance
            value (value): value of the rectangle
        """
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size