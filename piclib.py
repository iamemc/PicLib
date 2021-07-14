from kivy.uix.boxlayout import BoxLayout
from toprow import TopRow
from middlerow import MiddleRow
from bottomrow import BottomRow
from appmodule import AppModule

class PicLib(BoxLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    PicLib : top widget class
    """
    def __init__(self, **kwargs):
        """
        __init__ : PicLib class constructor
        """
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.appModule = AppModule()
        self.imgCollection = self.appModule.getImgCollection()
        self.tagCollection = self.appModule.getTagCollection()
        self.topRow = TopRow()
        self.bottomRow = BottomRow()
        self.middleRow = MiddleRow(self)

        self.add_widget(self.topRow)
        self.add_widget(self.middleRow)
        self.add_widget(self.bottomRow)

    def getBottomRow(self):
        """
        getBottomRow : self.bottomRow getter

        Returns:
            BottomRow: Class that represents the bottom row of the aplication
        """
        return self.bottomRow
    
    def getImgCollection(self):
        """
        getImgCollection : self.imgCollection getter

        Returns:
            ImageCollection: Class that represents an image collection
        """
        return self.imgCollection
    
    def getTagCollection(self):
        """
        getTagCollection : self.tagCollection

        Returns:
            TagCollection: Class that represents a tag collection
        """
        return self.tagCollection