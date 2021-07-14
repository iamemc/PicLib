from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from imagebox import ImageBox
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from math import ceil
from kivy.uix.label import Label

class PictureGrid(StackLayout):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
    PictureGrid : Class that represents the grid of images to be displayed in CentralPanel
    """
    def __init__(self, centralPanel, **kwargs):
        """
        __init__ : PictureGrid class constructor

        Args:
            centralPanel (CentralPanel): PictureGrid's parent widget
        """
        super().__init__(**kwargs)
        self.spacing = 7.5

        self.centralPanel = centralPanel
        self.imgsPerPage = 9
        self.imgCollection = centralPanel.getPicLib().getImgCollection()
        self.currentCollection = self.imgCollection
        self.buttonsBar = centralPanel.getMiddleRow().getButtonsBar()
        self.bottomRow = self.centralPanel.getBottomRow()

        self.buttonsBar.buttonNext.bind(on_press = self.displayNextImgs)
        self.buttonsBar.buttonPrevious.bind(on_press = self.displayPreviousImgs)
        self.buttonsBar.buttonSearchClear.bind(on_press = self.clearSearch)
        self.buttonsBar.buttonRotate.bind(on_press = self.rotateImg)

        self.buttonsBar.buttonTags.bind(on_press = lambda instance: self.centralPanel.displayTagsPanel(instance, self.buttonsBar.buttonTags.text))
        self.buttonsBar.buttonAddTag.bind(on_press = lambda instance: self.centralPanel.displayTagsPanel(instance, self.buttonsBar.buttonAddTag.text))
        self.buttonsBar.buttonRemoveTag.bind(on_press = lambda instance: self.centralPanel.displayTagsPanel(instance, self.buttonsBar.buttonRemoveTag.text))
        self.buttonsBar.buttonSearch.bind(on_press = lambda instance: self.centralPanel.displayTagsPanel(instance, self.buttonsBar.buttonSearch.text))

        self.createFirstScanPopup()
        self.createSettingsPopup()
        self.createDatePopup()

        self.loadImageBoxes()
        self.displayCollection()
    
    def updateCurrentCollection(self, collection):
        """
        updateCurrentCollection : updates the current displayed collection to the given collection.
        (can be used to display a searched collection or the main collection)

        Args:
            collection (ImageCollection): Class that represents a collection of images
        """
        self.currentCollection = collection
        self.displayCollection()
    
    def clearSearch(self, button):
        """
        clearSearch : clears a search by updating the current displayed collection to the main collection and
        removing the buttonSearchClear
        """
        self.updateCurrentCollection(self.imgCollection)
        self.buttonsBar.remove_widget(self.buttonsBar.buttonSearchClear)

    def getImgsPerPage(self):
        """
        getImgsPerPage : self.imgsPerPage getter

        Returns:
            int: number of images to be displayed per page
        """
        return self.imgsPerPage

    def setImgsPerPage(self, n):
        """
        setImgsPerPage : self.imgsPerPage setter

        Args:
            n (int): number of images to be displayed per page
        """
        self.imgsPerPage = n

    def loadImageBoxes(self):
        """
        loadImageBoxes : loads the image boxes for every image in the main image collection
        """
        imgs = self.imgCollection.getItems()
        [ImageBox.makeImageBox(img, self.centralPanel) for img in imgs]

    def displayCollection(self):
        """
        displayCollection : Displays the current collection if it has at least one image.
        If the collection doesn't have any images, the firstScan popup is opened.
        """
        if self.currentCollection.size() > 0:
            self.lastPage = ceil(self.currentCollection.size()/self.imgsPerPage)
            self.imgsToDisplay = list(self.currentCollection.getItems())
            self.currentPage = 0
            self.updateDisplay()
            self.displayImageBoxes()
        else:
            self.firstScan.open()
    
    def updateDisplay(self):
        """
        updateDisplay : updates the buttons and bottomRow information to be displayed.
        (Used when displaying the PictureGrid)
        """
        self.buttonsBar.clear_widgets()
        self.buttonsBar.add_widget(self.buttonsBar.buttonSettings)
        self.buttonsBar.add_widget(self.buttonsBar.buttonNext)
        self.buttonsBar.add_widget(self.buttonsBar.buttonPrevious)
        self.buttonsBar.add_widget(self.buttonsBar.buttonTags)
        self.buttonsBar.add_widget(self.buttonsBar.buttonAddTag)
        self.buttonsBar.buttonAddTag.disable()
        self.buttonsBar.add_widget(self.buttonsBar.buttonRemoveTag)
        self.buttonsBar.buttonRemoveTag.disable()
        self.buttonsBar.add_widget(self.buttonsBar.buttonDate)
        self.buttonsBar.buttonDate.disable()
        self.buttonsBar.add_widget(self.buttonsBar.buttonSearch)
        self.buttonsBar.add_widget(self.buttonsBar.buttonRotate)
        self.buttonsBar.buttonRotate.disable()
        self.buttonsBar.add_widget(self.buttonsBar.buttonZip)
        self.buttonsBar.buttonZip.disable()
        # NEW search clear button is now added everytime picgrid is showed if there is a search
        if self.currentCollection != self.imgCollection:
            self.buttonsBar.add_widget(self.buttonsBar.buttonSearchClear)

        self.bottomRow.imgLabels()

    def displayImageBoxes(self):
        """
        displayImageBoxes : given the current page and the number of images per page set in self.imgsPerPage,
        displays that number of image boxes, updates the page label with the current and last page
        """
        self.imgsDisplayed = self.imgsToDisplay[self.currentPage * self.imgsPerPage : self.currentPage * self.imgsPerPage + self.imgsPerPage]
        self.clear_widgets()
        [self.add_widget(ImageBox.makeImageBox(img, self.centralPanel)) for img in self.imgsDisplayed]
        self.bottomRow.updateLabelPage(self.currentPage, self.lastPage)
        self.pictureButtonValidator()
    
    def pictureButtonValidator(self):
        """
        pictureButtonValidator : verifies which buttons should be enabled depending on the current page:
            - buttonPrevious: disabled when on the first page
            - buttonNext: disabled when on the last page
        """
        # NEW added possibility of first page being the last and both buttons being disabled
        if self.lastPage == 1:
            self.buttonsBar.buttonPrevious.disable()
            self.buttonsBar.buttonNext.disable()
        elif self.currentPage == 0:
            self.buttonsBar.buttonPrevious.disable()
            self.buttonsBar.buttonNext.enable()
        elif self.currentPage == (self.lastPage - 1):
            self.buttonsBar.buttonPrevious.enable()
            self.buttonsBar.buttonNext.disable()
        else:
            self.buttonsBar.buttonPrevious.enable()
            self.buttonsBar.buttonNext.enable()

    def displayNextImgs(self, button):
        """
        displayNextImgs : adds one to the current page, displaying the next page of image boxes
        """
        self.currentPage += 1
        self.displayImageBoxes()

    def displayPreviousImgs(self, button):
        """
        displayPreviousImgs : subtracts one to the current page, displaying the previous page of image boxes
        """
        self.currentPage -= 1
        self.displayImageBoxes()
    
    def createFirstScanPopup(self):
        """
        createFirstScanPopup : creates the popup that allows to input the path to do the first scan
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text = "Type directory to scan:"))
        self.firstFolder = TextInput(multiline=False)
        box.add_widget(self.firstFolder)
        
        btnScan = Button(text="Scan",size_hint=(0.5, 0.5))
        box.add_widget(btnScan)

        self.firstScan = Popup(title='Startup',content=box,size_hint=(None, None), size=(500, 250), auto_dismiss=False)

        btnScan.bind(on_press = self.scanFirstFolder)
    
    def scanFirstFolder(self, button):
        """
        scanFirstFolder : scans the folder input by the user, loads the new image boxes, displays the collection and
        closes the firstScan popup
        """
        self.imgCollection.scanFolder(self.firstFolder.text)
        self.loadImageBoxes()
        self.displayCollection()
        self.closeFirstScan()

    def closeFirstScan(self):
        """
        closeFirstScan : closes the firstScan popup and resets the firstFolder TextInput's text
        """
        self.firstFolder.text = ''
        self.firstScan.dismiss()
    
    def createSettingsPopup(self):
        """
        createSettingsPopup : creates the Settings popup that allows to change the number of images to be
        displayed per page and allows to scan a given folder
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text="Images per page:"))

        btnDecrease = Button(text="-", size_hint=(0.5, 0.5))
        itemsPerPage = Label(text = str(self.getImgsPerPage()))
        btnIncrease = Button(text="+", size_hint=(0.5, 0.5))
        box2 = BoxLayout(orientation = 'horizontal')
        box2.add_widget(btnDecrease)
        box2.add_widget(itemsPerPage)
        box2.add_widget(btnIncrease)
        box.add_widget(box2)

        box.add_widget(Label(text = "Type directory to scan:"))
        self.folder = TextInput(multiline=False)
        box.add_widget(self.folder)
        
        btnScan = Button(text="Scan",size_hint=(0.5, 0.5))
        btnExit = Button(text="Exit",size_hint=(0.5, 0.5))
        box3 = BoxLayout(orientation = 'horizontal')
        box3.add_widget(btnScan)
        box3.add_widget(btnExit)
        box.add_widget(box3)

        self.settings = Popup(title='Settings',content=box,size_hint=(None, None), size=(500, 250), auto_dismiss=False)

        btnIncrease.bind(on_press = self.increaseItemsPerPage)
        btnDecrease.bind(on_press = self.decreaseItemsPerPage)
        btnScan.bind(on_press = self.scanFolder)
        btnExit.bind(on_press = self.cancelSettings)

        self.buttonsBar.buttonSettings.bind(on_press = self.settings.open)
    
    def increaseItemsPerPage(self, button):
        """
        increaseItemsPerPage : increases the number of images to be displayed per page by one,
        updates the settings popup label that indicates this number,
        displays the collection with the updated number of images per page and
        enables the btnDecrease if the number of images per page goes from 1 to 2
        (since 1 is the minimum number of images per page)
        """
        self.setImgsPerPage(self.getImgsPerPage() + 1)
        self.settings.content.children[-2].children[1].text = str(self.getImgsPerPage())
        self.displayCollection()
        if self.getImgsPerPage() == 2:
            self.settings.content.children[-2].children[2].disabled = False
    
    def decreaseItemsPerPage(self, button):
        """
        decreaseItemsPerPage : decreases the number of images to be displayed per page by one,
        updates the settings popup label that indicates this number,
        displays the collection with the updated number of images per page and
        disables the btnDecrease if the number of images per page goes from 2 to 1
        (since 1 is the minimum number of images per page)
        """
        self.setImgsPerPage(self.getImgsPerPage() - 1)
        self.settings.content.children[-2].children[1].text = str(self.getImgsPerPage())
        self.displayCollection()
        if self.getImgsPerPage() == 1:
            self.settings.content.children[-2].children[2].disabled = True
    
    def scanFolder(self, button):
        """
        scanFolder : given the folder input by the user, used the scanFolder method of the image collection to
        add new images to the collection, displays the updated collection and closes the settings popup
        """
        self.imgCollection.scanFolder(self.folder.text)
        self.loadImageBoxes()
        self.displayCollection()
        self.cancelSettings(button)

    def cancelSettings(self, button):
        """
        cancelSettings : closes the settings popup and resets the text in its TextInput
        """
        self.folder.text = ''
        self.settings.dismiss()

    def createDatePopup(self):
        """
        createDatePopup : creates a popup that allows the user to input a new date for the selected image
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text = "Type date in YYYY/MM/DD format:"))
        self.dateInput = TextInput(multiline=False)
        box.add_widget(self.dateInput)
        
        btnChange = Button(text="Change date",size_hint=(0.5, 0.5))
        btnCancel = Button(text="Cancel",size_hint=(0.5, 0.5))
        box2 = BoxLayout(orientation = 'horizontal')
        box2.add_widget(btnChange)
        box2.add_widget(btnCancel)
        box.add_widget(box2)

        self.date = Popup(title='Enter new date',content=box,size_hint=(None, None), size=(500, 250), auto_dismiss=False)

        btnChange.bind(on_press = self.changeDate)
        btnCancel.bind(on_press = self.cancelDate)

        self.buttonsBar.buttonDate.bind(on_press = self.date.open)
    
    def changeDate(self, button):
        """
        changeDate : changes the date of the selected image into the given the date input by the user,
        updates the information in the bottom row,
        saves the image collection in its json file (since one of its images path has been updated) and
        closes the date popup
        """
        selected = self.centralPanel.getSelectedImgs()
        img = selected[0]
        img.setDate(self.dateInput.text)
        self.bottomRow.updateInfo(selected)
        self.imgCollection.saveCollection()
        self.cancelDate(button)
    
    def cancelDate(self, button):
        """
        cancelDate : closes the date popup and resets the text in its TextInput
        """
        self.dateInput.text = ''
        self.date.dismiss()
    
    def rotateImg(self, button):
        """
        rotateImg : rotates the selected image in 90 degrees clockwise, updating its image box
        """
        selected = self.centralPanel.getSelectedImgs()
        img = selected[0]
        box = ImageBox.makeImageBox(img, self.centralPanel)
        box.rotate()