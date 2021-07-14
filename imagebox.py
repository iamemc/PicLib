from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class ImageBox(RelativeLayout):
    """
    55881 Eduardo Carvalho
    55738 Joao Milagaia
    
    ImageBox is a classe that implements a selectable image. The image 
    is drawn in a white frame. When the image is selected, the frame becomes red. 
    An ImageBox instance contain an instance of CPImage. 
    """
    # a class attribute that contain a dictionary of ImageBoxes created. The 
    # objective is to speed up the application by avoiding the creation of 
    # new objects each time a image is shown in the UI.
    imb_dict = dict()

    def __init__(self, cpimage, centralPanel, **kwargs):
        """
        __init__ : ImageBox class constructor

        Args:
            cpimage (CPImage): CPImage instance associated with the ImageBox instance
            centralPanel (CentralPanel): CentralPanel layout used to update the selected images
        """
        super().__init__(**kwargs)
        self.selected = False
        self.size_hint = (None, None)
        #self.height = 300
        self.height = 150
        self.image = Image(source=cpimage.getImageFile())
        self.cpImage = cpimage
        self.add_widget(self.image)
        #self.image.allow_stretch = True
        self.image.allow_stretch = False
        self.image.keep_ratio = False
        self.image.size_hint_x = None
        self.image.size_hint_y = None
        imageratio = self.image.get_image_ratio()
        #self.width = 290 * imageratio + 10
        self.width = 140 * imageratio + 10
        #self.image.size = (290 * imageratio,290)
        self.image.size = (140 * imageratio,140)
        self.image.pos = (5, 5)
        with self.canvas.before:
            Color(1,1,1,1)
            self.rect = Rectangle(size=self.size, pos=(0,0))
        self.bind(pos=ImageBox.__update_rect, size=ImageBox.__update_rect)

        self.centralPanel = centralPanel

    @staticmethod    
    def __update_rect(instance, value):
        """
        __update_rect : updates the rectangle

        Args:
            instance (ImageBox): ImageBox instance
            value (value): value of the rectangle
        """
        instance.rect.pos = (0,0)
        instance.rect.size = instance.size

    @classmethod
    def makeImageBox(cls, cpimage, centralPanel):
        """
        makeImageBox : given a CPImage instance, returns the associated ImageBox instance if there is one,
        or creates a new one if there isn't

        Args:
            cpimage (CPImage): CPImage instance associated with the ImageBox instance
            centralPanel (CentralPanel): CentralPanel layout used to update the selected images

        Returns:
            ImageBox: ImageBox instance
        """
        imfile = cpimage.getImageFile()
        if imfile in ImageBox.imb_dict:
            return ImageBox.imb_dict[imfile]
        imb = ImageBox(cpimage, centralPanel)
        ImageBox.imb_dict[imfile] = imb
        return imb

    def on_touch_down(self, touch):
        """
        on_touch_down : Provides instructions for when the ImageBox is clicked by the user
        """
        if self.collide_point(*touch.pos):
            print(self.image.source + ' pressed')
            #*******************
            # add code below to do something
            self.select()
            self.centralPanel.updateSelectedImgs(self)
            
    def select(self):
        """
        select : updates the color of the border and the self.selected atribute
        """
        if self.selected:
            with self.canvas.before:
                Color(1,1,1,1)
                self.rect = Rectangle(size=self.size, pos=(0,0))
            self.selected = False
        else:
            with self.canvas.before:
                Color(1,0,0,1)
                self.rect = Rectangle(size=self.size, pos=(0,0))
            self.selected = True

    def isSelected(self):
        """
        isSelected : self.selected getter (used to know if ImageBox is selected)

        Returns:
            bool: True if ImageBox is selected
        """
        return self.selected
    
    def getCPImage(self):
        """
        getCPImage : self.cpImage getter

        Returns:
            CPImage: CPImage instance associated with the ImageBox instance
        """
        return self.cpImage
    
    def rotate(self):
        """
        rotate : rotates the image associated with the ImageBox instance and updates its width and image size
        """
        self.cpImage.rotate()
        self.image.reload()
        imageratio = self.image.get_image_ratio()
        #self.width = 290 * imageratio + 10
        self.width = 140 * imageratio + 10
        #self.image.size = (290 * imageratio,290)
        self.image.size = (140 * imageratio,140)