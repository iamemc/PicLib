from cpcollection import CPCollection
from tag import Tag

class TagCollection(CPCollection):
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia

    Class that represents a Tag Collection
    """

    @staticmethod
    def elementFromJson(json, module):
        """
        elementFromJson using a dictionary entry, returns the Tag instance

        Args:
            json (Dict): dictionary
            module (AppModule): AppModule instance

        Returns:
            Tag: instance
        """
        return Tag.fromJson(json)

    def addTag(self, tag):
        """
        addTag adds a tag to the collection and saves it in a json file

        Args:
            tag (str): name of the tag to be added
        """
        if tag not in [tagInstance.getname() for tagInstance in self.items]:
            self.registerItem(Tag(tag))
        self.saveCollection()
    
    def removeTag(self, tag):
        """
        removeTag removes a tag from the collection and saves it in a json file

        Args:
            tag (str): name of the tag to be removed
        """
        self.items.discard(tag)
        self.saveCollection()