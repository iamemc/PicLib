from kivy.uix.boxlayout import BoxLayout
from coloredlabel import ColoredLabel

class BottomRow(BoxLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia

    BottomRow : Class that represents the bottom row of the aplication, which contains the following labels:
        - labelPage: current and last page
        - labelItems: number of selected images
        - labelDateTags: date and tags of selected image
        - labelTagsSelected: number of selected tags
        - labelTagsAvailable: number of available tags
    """
    def __init__(self, **kwargs):
        """
        __init__ : BottomRow class constructor
        """
        
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        self.padding = 10
        
        # Label definition:
        self.labelPage = ColoredLabel(text = '', size_hint_x = None, width = 100)
        self.labelItems = ColoredLabel(text = '')
        self.labelDateTags = ColoredLabel(text = '')
        self.labelTagsSelected = ColoredLabel(text = 'Selected tags: ' + str(0))
        self.labelTagsAvailable = ColoredLabel(text = '')
        
        self.add_widget(self.labelPage)
        self.add_widget(self.labelItems)
        self.add_widget(self.labelDateTags)

    def displaySelectedItems(self, n):
        """
        displaySelectedItems : updates the text in labelItems

        Args:
            n (int): number of selected images
        """
        self.labelItems.text = 'Selected items: ' + str(n)
    
    def updateInfo(self, selectedImgs):
        """
        updateInfo : updates the text in labelItems and labelDateTags

        Args:
            selectedImgs (list): list of selected CPImage objects
        """
        n = len(selectedImgs)
        self.displaySelectedItems(n)
        if n == 1:
            img = selectedImgs[0]
            # If only one image is selected, its date and tags are showed
            # The list of tags is converted into string and the parentheses are removed with [1:-1]
            self.labelDateTags.text = img.getDate() + " " + str(img.getTags())[1:-1]
        else:
            self.labelDateTags.text = ""
    
    def updateLabelPage(self, current, last):
        """
        updateLabelPage : updates the text in labelPage

        Args:
            current (int): current page (the first is 0, so 1 is added)
            last (int): last page
        """
        self.labelPage.text = "Page {}/{}".format(current + 1, last)
    
    def imgLabels(self):
        """
        imgLabels : updates the widgets to show information relative to images
        """
        self.clear_widgets()
        self.add_widget(self.labelPage)
        self.add_widget(self.labelItems)
        self.add_widget(self.labelDateTags)
    
    def tagLabels(self, n):
        """
        tagLabels : updates the widgets to show information relative to tags

        Args:
            n (int): number of available tags
        """
        self.clear_widgets()
        self.add_widget(self.labelTagsSelected)
        self.labelTagsAvailable.text = "Available Tags: " + str(n)
        self.add_widget(self.labelTagsAvailable)
    
    def updateSelectedTags(self, n):
        """
        updateSelectedTags : updates the text in labelTagsSelected

        Args:
            n (int): number of selected tags
        """
        self.labelTagsSelected.text = "Selected tags: " + str(n)