from kivy.uix.button import Button

class SquareButton(Button):
    """
    55881 Eduardo Carvalho
    55738 Joao Milagaia
    
    SquareButton is a subclass of class Button that implements a square button 
    to be used in the ButtonsBar widget.
    """
    def __init__(self, **kwargs):
        """
        __init__ : SquareButton class constructor
        """
        super().__init__(**kwargs)
        self.name = self.text
        self.color = (1,1,1,1)
        self.bold = True
        #self.height = 70
        self.height = 50
        self.size_hint_y = None
        self.width = 70
        self.size_hint_x = None
        self.disabled = False

    def disable(self):
        """
        disable : changes the state of the button to «disabled»
        """
        self.disabled = True

    def enable(self):
        """
        disable : changes the state of the button to «enabled» 
        (not disabled)
        """
        self.disabled = False

    def __str__(self):
        """
        __str__ : toString method

        Returns:
            str: string representation of SquareButton instance
        """
        return 'SquareButton-' + self.text