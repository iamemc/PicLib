from serializable import Serializable
import json

class CPCollection(Serializable):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia

    CPCollection collection of items
    Super class of all classes that represent collections (ImageCollection and TagCollection)
    Contais almost all functionalities that allow saving and loading of the elements of a collection

    """

    def __init__(self, filename, module):
        """
        __init__ construtor

        Args:
            filename (String): name of the file where the collection will be stored
            module (AppModule): AppModule instance, allows usage of its methods
        """
        self.items = set()
        self.filename = filename
        self.module = module
        self.path = module.getCollectionsRootFolder() + self.filename + ".json"
    
    def registerItem(self, item):
        """
        registerItem adds an item to the collection

        Args:
            item (CPImage/Tag): element to be added
        """
        self.items.add(item)
    
    def saveCollection(self):
        """
        saveCollection saves the collection
        """
        
        with open(self.path, 'w') as outfile:
            json.dump(self.toJson(), outfile, sort_keys=True, indent=4,  default=str)
    
    def loadCollection(self):
        """
        loadCollection loads a file and reads its content
        """
        with open(self.path, 'r') as readfile:
            data = json.load(readfile)
            self.filename = data["filename"]
            self.items = set([self.elementFromJson(x, self.module) for x in data["items"]])
    
    def size(self):
        """
        size returns the size of the collection

        Returns:
            int: number of elements in the collection
        """
        return len(self.items)
    
    def toJson(self):
        """
        toJson redefinition of the ToJson method

        Returns:
            Dict: dictionary where the "items" key corresponds to a list of dictionaries. One per item.
        """
        return {"filename":self.filename, "items":list(map(lambda x: x.toJson(), self.items))}
    
    @staticmethod
    def elementFromJson(json):
        """
        elementFromJson abstract and static method
        given a dictionary, returns an object of the correct type

        Args:
            json (Dict): dictionary
        """
        raise NotImplementedError("Returns instance")
    
    def getItems(self):
        """
        getItems self.items getter

        Returns:
            set: set of items in the collection
        """
        return self.items