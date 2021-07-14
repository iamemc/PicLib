from serializable import Serializable

class Tag(Serializable):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia

    This class represents a tag that can be used to categorize an image
    """
    def __init__(self, name):
        """
        Tag class constructor

        Args:
            name (String): name of the Tag
        """
        self.name = name
    
    def __hash__(self):
        """
        hash creates an Hash of the tag

        Returns:
            int: hash value
        """
        return hash((self.name))
    
    def __eq__(self,p):
        """
        __eq__ function to implement the equality notation between two tags

        Args:
            p (Tag): another instance

        Returns:
            bool: if the two tags are equal or not
        """
        return isinstance(p, Tag) and self.__hash__ == p.__hash__
    
    def getname(self):
        """
        getname returns the name of the tag
        
        """
        return self.name

    def toJson(self):
        """
        toJson allows the Tag to be saved in the specified format of a Json file

        """
        return {"tagname":self.getname()}
    
    @staticmethod
    def fromJson(dict):
        """
        fromJson creates an instance of a tag from a dictionary

        """
        return Tag(dict["tagname"])