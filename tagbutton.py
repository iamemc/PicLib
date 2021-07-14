from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from coloredlabel import ColoredLabel

class TagButton(Button):
    """
    55881 Eduardo Carvalho
    55738 Joao Milagaia
    
    TagButton class represent a button for tags. It has square corners and two 
    states: selected and unselected. The size (width) of the button is adjusted 
    according to the text of the button.  
    """
    def __init__(self, centralPanel, background_color=(0,0,0,1), color=(1,1,1,1), **kwargs):
        """
        __init__ : TagButton class constructor

        Args:
            centralPanel (CentralPanel): CentralPanel layout used to update the selected tags
            background_color (tuple, optional): Color of the TagButton's background. Defaults to (0,0,0,1) aka Black.
            color (tuple, optional): Color of the TagButton's text. Defaults to (1,1,1,1) aka White.
        """
        super().__init__(**kwargs)
        self.selected = False
        # the dot symbolize the hole in a label.
        self.text = self.text + ' •'
        # ' ◎' 
        # ' \u25C9'
        # ' •'
        self.button_color = background_color # used when button is pressed
        self.text_color = color
        self.background_color = background_color
        self.background_normal = ''
        self.padding_x = 10
        self.size_hint = (None, None)
        self.height = self.font_size * 1.7
        with self.canvas.before:
            Color(*background_color)
            self.background_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.__update_rect, size=self.__update_rect)
        self.texture_update()
        
        self.centralPanel = centralPanel

    def __setText(self, text):
        """
        __setText : sets the text of the button

        Args:
            text (str): text to be displayed in the TagButton
        """
        self.text = text
        self.texture_update()
        TagButton.__update_rect(self,None)

    def getText(self):
        """
        getText : self.text getter (removes added hole symbol)

        Returns:
            str: text associated with TagButton
        """
        return self.text[0:-2]

    def on_press(self):
        """
        on_press : When pressed, changes the color scheme of the TagButton depending on whether it has been selected or deselected
        """
        if self.selected:
            color = self.text_color
            bcolor = self.button_color
        else:
            color = self.button_color
            bcolor = self.text_color 
        print('select: ' + str(self.selected) + ' t ' +
            str(color) + ' b ' + str(bcolor))
        self.background_color = bcolor
        self.color = color            
        self.texture_update()

    def on_release(self):
        """
        on_release : Updates the selected state of the TagButton and updates the list of selected tags
        """
        if self.selected:
            self.selected = False
        else:
            self.selected = True
        #*********************
        # add code to do something
        self.centralPanel.updateSelectedTags(self)

    def isSelected(self):
        """
        isSelected : self.selected getter (used to know if TagButton is selected)

        Returns:
            bool: True if TagButton is selected
        """
        return self.selected

    def unSelect(self):
        """
        unSelect : sets self.selected to false
        """
        self.selected = False

    def getLabel(self):
        """
        getLabel : May be used to obtain a Label that corresponds to the tag, to 
        be used elsewhere in the UI

        Returns:
            ColoredLabel: an instance of ColoredLabel with same text as 
            the button instance
        """
        label = ColoredLabel(text=self.text[0:-2], background_color=self.button_color, color=self.text_color)
        label.size_hint_y = None
        label.height = 35
        label.font_size = 20
        return label

    @staticmethod
    def __update_rect(instance, value):
        """
        __update_rect : updates rectangles

        Args:
            instance (TagButton): TagButton instance
            value (value): value of the rectangle
        """
        instance.background_rect.pos = instance.pos
        instance.background_rect.size = instance.size
        instance.width = instance.texture_size[0]
