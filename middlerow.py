from kivy.uix.boxlayout import BoxLayout
from buttonsbar import ButtonsBar
from centralpanel import CentralPanel

class MiddleRow(BoxLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    MiddleRow : class that represents the middle row of the application
    """
    def __init__(self, picLib, **kwargs):
        """
        __init__ : MiddleRow class constructor

        Args:
            picLib (PicLib): top widget class
        """
        super().__init__(**kwargs)
        self.orientation = 'horizontal'

        self.picLib = picLib

        self.buttonsBar = ButtonsBar()
        self.centralPanel = CentralPanel(self)

        self.add_widget(self.buttonsBar)
        self.add_widget(self.centralPanel)
    
    def getPicLib(self):
        """
        getPicLib : self.picLib getter

        Returns:
            PicLib: top widget class
        """
        return self.picLib

    def getButtonsBar(self):
        """
        getButtonsBar : self.buttonsBar getter

        Returns:
            ButtonsBar: Class that represents the app's buttons bar
        """
        return self.buttonsBar