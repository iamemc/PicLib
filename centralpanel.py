from kivy.uix.popup import Popup
from imagebox import ImageBox
from kivy.uix.boxlayout import BoxLayout
from picturegrid import PictureGrid
from tagspanel import TagsPanel
from kivy.uix.label import Label
from zipfile import ZipFile
import os
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CentralPanel(BoxLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    CentralPanel : class that represents the app's central panel
    """
    def __init__(self, middleRow, **kwargs):
        """
        __init__ : CentralPanel class constructor

        Args:
            middleRow (MiddleRow): CentralPanel's parent widget
        """        
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        
        self.middleRow = middleRow
        self.picLib = middleRow.getPicLib()
        self.bottomRow = self.picLib.getBottomRow()
        self.buttonsBar = middleRow.getButtonsBar()

        self.pictureGrid = PictureGrid(self)
        self.tagsPanel = TagsPanel(self)

        self.buttonsBar.buttonAddTagConfirm.bind(on_press = self.addTags)
        self.buttonsBar.buttonRemoveTagConfirm.bind(on_press = self.removeTags)
        self.buttonsBar.buttonSearchConfirm.bind(on_press = self.searchTags)
        
        # Creation of popup that allows to insert the path and name of the zip file
        self.createZipPopup()

        # List of selected images and tags
        self.selectedImgs = []
        self.selectedTags = []

        self.add_widget(self.pictureGrid)
    
    def getSelectedImgs(self):
        """
        getSelectedImgs : self.selectedImgs getter

        Returns:
            list: list of selected CPImage objects
        """
        return self.selectedImgs
    
    def getMiddleRow(self):
        """
        getMiddleRow : self.middleRow getter

        Returns:
            MiddleRow: CentralPanel's parent widget
        """
        return self.middleRow
    
    def getBottomRow(self):
        """
        getBottomRow : self.bottomRow getter

        Returns:
            BottomRow: class that is used to update the information in the bottom row
        """
        return self.bottomRow
    
    def getPicLib(self):
        """
        getPicLib : self.picLib getter

        Returns:
            PicLib: top widget class
        """
        return self.picLib
    
    def displayPictureGrid(self, button):
        """
        displayPictureGrid : updates the CentralPanel to show the PictureGrid,
        clearing all previously selected images and updating the buttons displayed
        """
        self.clear_widgets()
        self.clearSelectedImgs()
        self.pictureGrid.updateDisplay()
        self.add_widget(self.pictureGrid)
    
    def displayTagsPanel(self, button, buttonName):
        """
        displayTagsPanel : updates the CentralPanel to show the TagsPanel,
        clearing all previously selected tags and updating the buttons displayed

        Args:
            buttonName (str): name of the button that called this method
            (used to decide which buttons to display in the TagsPanel)
        """
        self.clear_widgets()
        self.clearSelectedTags()
        self.previousButton = buttonName
        self.tagsPanel.updateDisplay()
        self.add_widget(self.tagsPanel)

    def updateSelectedImgs(self, imgBox):
        """
        updateSelectedImgs : updates the list of selected images, information displayed in BottomRow and
        the buttons displayed in ButtonsBar:
            - buttons enabled if there is one or more selected images:
                - buttonAddTag
                - buttonRemoveTag
                - buttonZip
            - buttons enabled if there is only one selected image:
                - buttonDate
                - buttonRotate

        Args:
            imgBox (ImageBox): class that implements a selectable image
        """
        if imgBox.isSelected():
            self.selectedImgs.append(imgBox.getCPImage())
        else:
            self.selectedImgs.remove(imgBox.getCPImage())
        self.bottomRow.updateInfo(self.selectedImgs)
        
        if len(self.selectedImgs) > 0:
            self.buttonsBar.buttonAddTag.enable()
            self.buttonsBar.buttonRemoveTag.enable()
            self.buttonsBar.buttonZip.enable()
            if len(self.selectedImgs) == 1:
                self.buttonsBar.buttonDate.enable()
                self.buttonsBar.buttonRotate.enable()
            else:
                self.buttonsBar.buttonDate.disable()
                self.buttonsBar.buttonRotate.disable()
        else:
            self.buttonsBar.buttonAddTag.disable()
            self.buttonsBar.buttonRemoveTag.disable()
            self.buttonsBar.buttonDate.disable()
            self.buttonsBar.buttonRotate.disable()
            self.buttonsBar.buttonZip.disable()
    
    def updateSelectedTags(self, tagButton):
        """
        updateSelectedTags : updates the list of selected tags, information displayed in BottomRow and
        the buttons displayed in ButtonsBar:
            - buttons enabled if there is one or more selected tags:
                - buttonAddTagConfirm
                - buttonRemoveTagConfirm
                - buttonSearchConfirm

        Args:
            tagButton (TagButton): class that represents a button for tags
        """
        if tagButton.isSelected():
            self.selectedTags.append(tagButton)
        else:
            self.selectedTags.remove(tagButton)
        self.bottomRow.updateSelectedTags(len(self.selectedTags))

        if len(self.selectedTags) > 0:
            self.buttonsBar.buttonAddTagConfirm.enable()
            self.buttonsBar.buttonRemoveTagConfirm.enable()
            self.buttonsBar.buttonSearchConfirm.enable()
        else:
            self.buttonsBar.buttonAddTagConfirm.disable()
            self.buttonsBar.buttonRemoveTagConfirm.disable()
            self.buttonsBar.buttonSearchConfirm.disable()
    
    def clearSelectedImgs(self):
        """
        clearSelectedImgs : unselects all images in self.selectedImgs, empties this list and
        updates the info in BottomRow
        """
        [ImageBox.makeImageBox(img, self).select() for img in self.selectedImgs]
        self.selectedImgs = []
        self.bottomRow.updateInfo(self.selectedImgs)
    
    def clearSelectedTags(self):
        """
        clearSelectedTags : unselects all tag buttons in self.selectedTags, empties this list and
        updates the info in BottomRow
        """
        for tag in self.selectedTags:
            tag.on_press()
            tag.unSelect()
        self.selectedTags = []
        self.bottomRow.updateSelectedTags(len(self.selectedTags))
    
    def addTags(self, button):
        """
        addTags : adds the selected tags to the selected images and displays the PictureGrid
        """
        for img in self.selectedImgs:
            for tag in self.selectedTags:
                img.addTag(tag.getText())
        self.displayPictureGrid(button)
    
    def removeTags(self, button):
        """
        removeTags : removes the selected tags from the selected images and displays the PictureGrid
        """
        for img in self.selectedImgs:
            for tag in self.selectedTags:
                img.removeTag(tag.getText())
        self.displayPictureGrid(button)
    
    def searchTags(self, button):
        """
        searchTags : searches for images with at least one of the selected tags creating an
        ImageCollection with the search result:
            - If this collection has at least one image, it is loaded as the current collection in PictureGrid and
            the buttonSearchClear is added to the ButtonsBar;
            - If this collection has no images, a warning popup is created and opened.
        """
        tags = [tag.getText() for tag in self.selectedTags]
        searchCollection = self.picLib.getImgCollection().findWithTags(tags)
        if searchCollection.size() > 0:
            self.pictureGrid.updateCurrentCollection(searchCollection)
            self.displayPictureGrid(button)
            # NEW search clear isn't added when a search is done but when picture grid is displaying a search
            #self.buttonsBar.add_widget(self.buttonsBar.buttonSearchClear)
        else:
            message = "The following tags found no results:\n" +  str(tags)[1:-1]
            self.createWarningPopup(message)
    
    def createWarningPopup(self, message):
        """
        createWarningPopup : creates and opens a warning popup with the given message

        Args:
            message (str): message to be displayed in the warning popup
        """
        Popup(title='Warning', content = Label(text = u"\u26A0 " + message, font_name='DejaVuSans'),
                size_hint = (None, None), size=(500, 100)).open()
    
    def createZipPopup(self):
        """
        createZipPopup : creates a popup that allows to insert the path and name of the zip file
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text="Zip save directory:"))
        self.zipfolder = TextInput(multiline=False)
        box.add_widget(self.zipfolder)

        box.add_widget(Label(text = "Zip file name:"))
        self.zipname = TextInput(multiline=False)
        box.add_widget(self.zipname)
        
        btnZip = Button(text="Zip",size_hint=(0.5, 0.5))
        btnCancel = Button(text="Cancel",size_hint=(0.5, 0.5))
        box2 = BoxLayout(orientation = 'horizontal')
        box2.add_widget(btnZip)
        box2.add_widget(btnCancel)
        box.add_widget(box2)

        self.zip = Popup(title='Zip selected images',content=box,size_hint=(None, None), size=(500, 250), auto_dismiss=False)

        btnZip.bind(on_press = self.createZip)
        btnCancel.bind(on_press = self.cancelZip)

        self.buttonsBar.buttonZip.bind(on_press = self.zip.open)
    
    def createZip(self, button):
        """
        createZip : takes the path and name input by the user to create the zip file containing
        all selected images
        """
        zipInput = os.path.join(self.zipfolder.text, self.zipname.text)
        with ZipFile(zipInput + '.zip', 'w') as zip:
            for img in self.selectedImgs:
                zip.write(img.getImageFile(), os.path.basename(img.getImageFile()))
        self.cancelZip(button)
    
    def cancelZip(self, button):
        """
        cancelZip : resets the input boxes of the zip popup and closes it
        """
        self.zipfolder.text = ''
        self.zipname.text = ''
        self.zip.dismiss()