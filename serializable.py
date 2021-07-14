class Serializable:
    """
    Author: 55881 Eduardo Carvalho
    Author: 55738 Joao Milagaia
    
     This Class allows two methods to be called to transform the objects so they can be written and read from and to a file.
     
     The Super class of all classes that will be saved to files
    """

    def toJson(self):
        """
        toJson transforms an instance into a dictionary

        Returns:
            Dict: dictionary that contains the values of the attributes of an object
        """
        return self.__dict__
    
    @staticmethod
    def fromJson(json):
        """
        fromJson abstract and static method

        Args:
            json (Dict): dictionary obtained by the json.loads() method

        Raises:
            NotImplementedError: must return an instance
        """
        raise NotImplementedError("Returns instance")