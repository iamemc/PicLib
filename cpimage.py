from serializable import Serializable
from PIL import Image, ExifTags
import time
import os
from shutil import copy, move
import json
import hashlib

class CPImage(Serializable):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia

     Represents an image.
    """

    def __init__(self, imageFile, module):
        """
        __init__ construtor

        Args:
            imageFile (String): path to the image's folder
            module (AppModule): AppModule instance, allows the usage of its methods
        """
        self.module = module
        self.imageFile = imageFile
        self.exif = CPImage.loadExif(imageFile)
        self.jsonfile = ".".join(imageFile.split(".")[:-1]) + ".json"
        self.metadata = self.getMetaData()
    
    @staticmethod
    def loadExif(imageFile):
        """
        loadExif loads the exif information of an image from the image file

        Args:
            imageFile (String): path to the image's folder

        Returns:
            exif: Dictionary
        """
        im = Image.open(imageFile)
        exif = {}
        for k,v in im.getexif().items():
            if k in ExifTags.TAGS:
                exif[ExifTags.TAGS[k]] = v
        im.close()
        return exif
    
    def getMetaData(self):
        """
        getMetaData loads the metadata information of an image from a Json file if it exists,
        if not it creates one

        Returns:
            exif: Dictionary
        """
        if os.path.exists(self.jsonfile):
            with open(self.jsonfile, 'r') as readfile:
                metadata = json.load(readfile)
                #metadata = {"date": data["date"], "tags": data["tags"]}
        else:
            metadata = {"date": self.getDateFromFile(), "tags":[]}
        return metadata
    
    def getDate(self):
        """
        getDate returns the date information from an image

        """
        return self.metadata["date"]

    def getDateFromFile(self):
        """
        getDateFromFile returns the date in which the image was created, in case of a photograph, when it was taken.
        If no date exists, the system's date will be returned

        Returns:
            String: date
        """
        if 'DateTime' in self.exif.keys() and self.exif['DateTime'] != None:
            return self.exif['DateTime'].replace(":","/")[:10]
        else:
            return time.strftime('%Y/%m/%d', time.gmtime(os.path.getmtime(self.getImageFile())))
    
    def setDate(self, date):
        """
        setDate allows the date to be overwritten using the user's input and saves it.

        Args:
            date (String): date
        """
        self.metadata["date"] = date
        collectionsRootFolder = self.module.getCollectionsRootFolder()
        folder = os.path.join(collectionsRootFolder, date)
        os.makedirs(folder, exist_ok = True)
        move(self.getImageFile(), folder)
        move(self.jsonfile, folder)
        self.setImageFile(folder + "/" + os.path.basename(self.imageFile))
        self.saveMetadata()

    def getDimensions(self):
        """
        getDimensions returns a tuple with the height and width of an image

        Returns:
            tuple: width and height
        """
        return (self.exif['ExifImageWidth'], self.exif['ExifImageHeight'])
    
    def getImageFile(self):
        """
        getImageFile returns the path to the image's folder

        Returns:
            String: path to the image's folder
        """
        return self.imageFile

    def setImageFile(self, path):
        """
        setImageFile allows the file path to be overwritten

        Args:
            path (String): image path
        """
        self.imageFile = path
        self.jsonfile = ".".join(self.imageFile.split(".")[:-1]) + ".json"
    
    def toJson(self):
        """
        toJson transforms an image into a dictionary

        Returns:
            Dict: dictionary that contains the values of the attributes of an object
        """
        return {"imageFile":self.getImageFile()}
    
    @staticmethod
    def fromJson(json, module):
        """
        fromJson creates an instance of an image from a dictionary

        Args:
            json (Dict): dictionary
            module (AppModule): AppModule instance

        Returns:
            CPImage: instance
        """
        return CPImage(json["imageFile"], module)
    
    def copyToFolder(self, folder):
        """
        copyToFolder copies a file from an origin folder to a destination folder and saves its metadata

        Args:
            folder (String): selected folder
        """
        copy(self.getImageFile(), folder)
        # NEW
        # self.setImageFile(folder + "/" + os.path.basename(self.imageFile))
        self.setImageFile(os.path.join(folder, os.path.basename(self.imageFile)))
        self.saveMetadata()
    
    def __hash__(self):
        """
        __hash__ creates an hash of an image, in bytes, using MD5

        Returns:
            int: hash value
        """
        im = Image.open(self.imageFile)
        h = int(hashlib.md5(im.tobytes()).hexdigest(), 16)
        im.close()
        return h
    
    def __eq__(self,p):
        """
        __eq__ function to implement the equality notation between two images

        Args:
            p (CPImage): another instance

        Returns:
            bool: if the two images are equal or not
        """
        return isinstance(p, CPImage) and self.__hash__() == p.__hash__()
        
    @staticmethod
    def makeCPImage(filename, module):
        """
        makeCPImage obtains the date in which the image was taken/saved.
        Creates a sub-folder in the root folder of the app using getDateFromFile()
            ex: root_folder/YYYY/MM/DD/

        Copies a file to a folder
        Returns an instance of CPImage

        Args:
            filename (String): name of the file
            module (AppModule): AppModule instance
        """
        img = CPImage(filename, module)
        date = img.getDateFromFile()
        collectionsRootFolder = module.getCollectionsRootFolder()
        path = os.path.join(collectionsRootFolder, date)
        os.makedirs(path, exist_ok = True)
        img.copyToFolder(path)
        return img
    
    def saveMetadata(self):
        """
        saveMetadata saves the metadata to a Json file
        """
        with open(self.jsonfile, 'w') as json_file:
            json.dump(self.metadata, json_file, sort_keys=True, indent=4,  default=str)
    
    def addTag(self, tag):
        """
        addTag saves the assigned Tag to an image's metadata

        Args:
            tag (String): name of the Tag
        """
        if tag not in self.metadata["tags"]:
            self.metadata["tags"].append(tag)
            self.saveMetadata()
    
    def removeTag(self, tag):
        """
        removeTag removes the assigned Tag from an image's metadata

        Args:
            tag (String): name of the Tag
        """
        if tag in self.metadata["tags"]:
            self.metadata["tags"].remove(tag)
            self.saveMetadata()
    
    def hasTag(self, tag):
        """
        hasTag checks if an image already has the given Tag

        Args:
            tag (String): name of the Tag
        
        Returns:
            true or false
        """
        return tag in self.metadata["tags"]
    
    def getTags(self):
        """
        getTags returns the Tags of an image

        """
        return self.metadata["tags"]
    
    def rotate(self):
        """
        rotate rotates an image by 90 degrees, clockwise

        """
        img = Image.open(self.imageFile)
        rotated = img.rotate(-90, expand = True)
        rotated.save(self.imageFile)