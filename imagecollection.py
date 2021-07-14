from cpcollection import CPCollection
from cpimage import CPImage
import os

class ImageCollection(CPCollection):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
     Represents a collection of images.
    """

    def scanFolder(self, folder = "./fotos/"):
        """
        scanFolder used to import a set of images.

        Args:
            folder (String): folder with images to scan
        """
        img_list = ImageCollection.allJPGFiles(folder)
        paths = map(lambda x: x.path, img_list)
        cpimg = [CPImage.makeCPImage(x, self.module) for x in paths]
        list(map(self.registerItem, cpimg))
        self.saveCollection()
    
    @staticmethod
    def allJPGFiles(folder):
        """
        allJPGFiles uses the allFiles function, uses a filter to only obtain the wanted files.

        Args:
            folder (String): folder with images to scan

        Returns:
            list: List of wanted files
        """
        img = ImageCollection.allFiles(folder)
        format = (".jpg", ".jpeg", ".JPG", ".JPEG")
        return list(filter(lambda x: x.name.endswith(format), img))
    
    @staticmethod
    def splitIf(func, l):
        """
        splitIf given a function, divdes the elements of a list in two tuples.
        the first element of the tuple has the elements of which the function returned True
        the second element of the tuple has the elements of which the function returned False

        Args:
            func: function that returns True or False
            l (list): list to split
        """
        def _splitIf(func, l, result):
                if l == []: return result
                if func(l[0]):
                    result[0].append(l[0])
                else:
                    result[1].append(l[0])
                return _splitIf(func, l[1:], result)
        return _splitIf(func, l, ([], []))

    @staticmethod
    def allFiles(folder):
        """
        allFiles scans a folder to find all files

        Args:
            folder (String): folder with images to scan
        """
        def _allFiles(folder):
            it1 = list(os.scandir(folder))
            folders, files = ImageCollection.splitIf(lambda x: x.is_dir(), it1)
            for f in folders:
                files.extend(_allFiles(f))
            return files
        return _allFiles(folder)
    
    @staticmethod
    def elementFromJson(json, module):
        """
        elementFromJson from a dictionary, returns an instance of CPImage

        Args:
            json (Dict): Dictionary
            module (AppModule): AppModule instance

        Returns:
            CPImage: Instance
        """
        return CPImage.fromJson(json, module)
    
    def findWithTags(self, tags):
        """
        findWithTags : finds all images in the collection that have one of the given tags

        Args:
            tags (list): list of tags (str) to search

        Returns:
            ImageCollection: new instance of ImageCollection with the results of the search
        """
        searchColl = ImageCollection("search", self.module)
        list(map(searchColl.registerItem,filter(lambda img: any(searchtag in img.metadata["tags"] for searchtag in tags), self.items)))
        return searchColl