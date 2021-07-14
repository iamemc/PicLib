from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from tagbutton import TagButton
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TagsPanel(StackLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    TagsPanel : Class that represents the panel of tags to be displayed in CentralPanel
    """
    def __init__(self, centralPanel, **kwargs):
        """
        __init__ : TagsPanel class constructor

        Args:
            centralPanel (CentralPanel): TagsPanel's parent widget
        """
        super().__init__(**kwargs)
        self.spacing = 7.5

        self.centralPanel = centralPanel
        self.tagCollection = centralPanel.getPicLib().getTagCollection()
        self.bottomRow = centralPanel.getBottomRow()
        self.buttonsBar = centralPanel.getMiddleRow().getButtonsBar()

        self.buttonsBar.buttonBack.bind(on_press = self.centralPanel.displayPictureGrid)
        
        self.defaultTags()

        [self.add_widget(TagButton(centralPanel, text = tag.getname(), background_color=(0.25,0.25,0.25,1), font_size = 35)) for tag in self.tagCollection.getItems()]

        self.createNewTagPopup()
    
    def defaultTags(self):
        """
        defaultTags : creates 7 default tags to be used by the user and adds them to the tag collection
        """
        tags = ["Pessoa", "Pessoas", "Plantas", "Paisagem", "Monumento", "Animal", "Veiculo"]
        [self.tagCollection.addTag(tag) for tag in tags]
    
    def updateDisplay(self):
        """
        updateDisplay : updates the bottom row with the size of the tag collection and
        updates the buttons to be displayed in ButtonsBar:
            - buttonBack: always added, leads to PictureGrid
            - buttonNewTag: always added, opens the popup that allows to input the name of a new tag
            - buttonAddTagConfirm: added and disabled if the previous button is buttonAddTag
            - buttonRemoveTagConfirm: added and disabled if the previous button is buttonRemoveTag
            - buttonSearchConfirm: added and disabled if the previous button is buttonSearch
        These last 3 buttons are automatically disabled because they need at least one tag to be selected
        """
        self.buttonsBar.clear_widgets()
        self.buttonsBar.add_widget(self.buttonsBar.buttonBack)
        self.buttonsBar.add_widget(self.buttonsBar.buttonNewTag)
        if self.centralPanel.previousButton == self.buttonsBar.buttonAddTag.text:
            self.buttonsBar.add_widget(self.buttonsBar.buttonAddTagConfirm)
            self.buttonsBar.buttonAddTagConfirm.disable()
        elif self.centralPanel.previousButton == self.buttonsBar.buttonRemoveTag.text:
            self.buttonsBar.add_widget(self.buttonsBar.buttonRemoveTagConfirm)
            self.buttonsBar.buttonRemoveTagConfirm.disable()
        elif self.centralPanel.previousButton == self.buttonsBar.buttonSearch.text:
            self.buttonsBar.add_widget(self.buttonsBar.buttonSearchConfirm)
            self.buttonsBar.buttonSearchConfirm.disable()
        
        self.bottomRow.tagLabels(self.tagCollection.size())
    
    def createNewTagPopup(self):
        """
        createNewTagPopup : creates a popup that allows the user to input the name of a new tag
        """
        box = BoxLayout(orientation='vertical')
        self.newtag = TextInput(multiline=False)
        box.add_widget(self.newtag)

        btnTagEnter = Button(text="Enter",size_hint=(0.5, 0.5))
        btnTagCancel = Button(text="Cancel",size_hint=(0.5, 0.5))
        box2 = BoxLayout(orientation = 'horizontal')
        box2.add_widget(btnTagEnter)
        box2.add_widget(btnTagCancel)
        box.add_widget(box2)

        self.popup = Popup(title='Write New Tag:',content=box,size_hint=(None, None), size=(500, 250), auto_dismiss=False)
        
        btnTagEnter.bind(on_press = self.createNewTag)
        btnTagCancel.bind(on_press = self.cancelNewTag)
        
        self.buttonsBar.buttonNewTag.bind(on_press = self.popup.open)
    
    def createNewTag(self, button):
        """
        createNewTag : given the tag name input by the user, creates the new tag,
        adds it to the tag collection,
        adds the corresponding TagButton to the TagsPanel,
        updates the information in the bottom row and
        closes the NewTag popup
        """
        tag = self.newtag.text
        self.tagCollection.addTag(tag)
        self.add_widget(TagButton(self.centralPanel, text = tag, background_color=(0.25,0.25,0.25,1), font_size = 35))
        self.bottomRow.tagLabels(self.tagCollection.size())
        self.cancelNewTag(button)
    
    def cancelNewTag(self, button):
        """
        cancelNewTag : closes the NewTag popup and resets the text in the TextInput
        """
        self.newtag.text = ''
        self.popup.dismiss()