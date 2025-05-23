# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Zoom(object):

    """Implementation of the 'Zoom' model.

    This is a required field if collection type is zoom.

    Attributes:
        secret (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "secret": 'secret'
    }

    def __init__(self,
                 secret=None):
        """Constructor for the Zoom class"""

        # Initialize members of the class
        self.secret = secret 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        secret = dictionary.get("secret") if dictionary.get("secret") else None
        # Return an object of this model
        return cls(secret)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'secret={self.secret!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'secret={self.secret!s})')
