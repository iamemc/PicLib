import os
from imagecollection import ImageCollection
from tagcollection import TagCollection

class AppModule:
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
     AppModule : Creates root folder, image collection and tag collection
    """
    def __init__(self):
        """
        __init__ AppModule class constructor
        """
        # self.collectionsRootFolder (String): root folder path
        self.collectionsRootFolder = "./PicLib/"

        # os.makedirs() allows to create the root folder if it doesn't exist
        os.makedirs(os.path.dirname(self.collectionsRootFolder), exist_ok = True)

        self.imgCollection = ImageCollection("mainImgCollection", self)

        # If the collection's json file exists, it is loaded
        try:
            self.imgCollection.loadCollection()
        # If it doesn't exist, the collection remains empty
        except FileNotFoundError:
            pass
        
        # The same process for the tag collection
        self.tagCollection = TagCollection("mainTagCollection", self)
        try:
            self.tagCollection.loadCollection()
        except FileNotFoundError:
            pass

    def getCollectionsRootFolder(self):
        """
        getCollectionsRootFolder : self.collectionsRootFolder getter

        Returns:
            string: root folder path
        """
        return self.collectionsRootFolder
    
    def getImgCollection(self):
        """
        getImgCollection : self.imgCollection getter

        Returns:
            ImageCollection: ImageCollection instance
        """
        return self.imgCollection
    
    def getTagCollection(self):
        """
        getTagCollection : self.tagCollection getter

        Returns:
            TagCollection: TagCollection instance
        """
        return self.tagCollection