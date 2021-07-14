from kivy.uix.boxlayout import BoxLayout
from squarebutton import SquareButton

class ButtonsBar(BoxLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    ButtonsBar : Class that represents the app's left bar with the following buttons:
        - buttonSettings: shows settings popup
        - buttonNext: shows next page of images
        - buttonPrevious: shows previous page of images
        - buttonTags: shows TagsPanel to create new tags
        - buttonBack: shows PictureGrid
        - buttonNewTag: shows popup to insert the name of the new tag
        - buttonAddTag: shows TagsPanel to add tags to selected images
        - buttonAddTagConfirm: adds selected tags to selected images
        - buttonRemoveTag: shows TagsPanel to remove tags from selected images
        - buttonRemoveTagConfirm: removes selected tags from selected images
        - buttonDate: shows popup to insert a new date for the selected image
        - buttonSearch: shows TagsPanel to make a search by tags
        - buttonSearchConfirm: shows PictureGrid, showing the search results
        - buttonSearchClear: clears the search, showing all images
        - buttonRotate: rotates the selected image 90 degrees clockwise
        - buttonZip: shows popup to insert the path and name of the zip file
        
    The binding of the buttons to methods is done in the classes that have those methods
    The button widgets are added to the ButtonsBar layout in the class associated with those buttons
    Button disabling and enabling are done in the classes who have the necessary attributes
    to make the necessary verifications
    """
    def __init__(self, **kwargs):
        """
        __init__ : ButtonsBar class constructor
        """
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_x = None
        self.width = 100

        self.buttonSettings = SquareButton(text = u"\u2699", font_name='DejaVuSans', font_size=45)
                                                # u"\u2699" is a GEAR unicode symbol
        self.buttonNext = SquareButton(text = 'Next')
        self.buttonPrevious = SquareButton(text = 'Previous')
        self.buttonTags = SquareButton(text = 'Tags')
        self.buttonBack = SquareButton(text = 'Back')
        self.buttonNewTag = SquareButton(text = 'New Tag')
        self.buttonAddTag = SquareButton(text = 'Add Tag')
        self.buttonAddTagConfirm = SquareButton(text = 'Add')
        self.buttonRemoveTag = SquareButton(text = 'Remove\nTag')
        self.buttonRemoveTagConfirm = SquareButton(text = 'Remove')
        self.buttonDate = SquareButton(text = 'Change\nDate')
        self.buttonSearch = SquareButton(text = 'Search')
        self.buttonSearchConfirm = SquareButton(text = 'Confirm\nSearch')
        self.buttonSearchClear = SquareButton(text = 'Clear\nSearch')
        self.buttonRotate = SquareButton(text = 'Rotate')
        self.buttonZip = SquareButton(text = 'Zip')