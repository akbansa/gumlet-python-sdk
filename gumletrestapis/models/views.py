# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper
from gumletrestapis.models.datum_1 import Datum1


class Views(object):

    """Implementation of the 'Views' model.

    Attributes:
        data (List[Datum1]): The model property of type List[Datum1].
        has_next_page (bool): The model property of type bool.
        current_page (int): The model property of type int.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "has_next_page": 'has_next_page',
        "current_page": 'current_page'
    }

    _optionals = [
        'data',
        'has_next_page',
        'current_page',
    ]

    def __init__(self,
                 data=APIHelper.SKIP,
                 has_next_page=True,
                 current_page=0):
        """Constructor for the Views class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 
        self.has_next_page = has_next_page 
        self.current_page = current_page 

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
        data = None
        if dictionary.get('data') is not None:
            data = [Datum1.from_dictionary(x) for x in dictionary.get('data')]
        else:
            data = APIHelper.SKIP
        has_next_page = dictionary.get("has_next_page") if dictionary.get("has_next_page") else True
        current_page = dictionary.get("current_page") if dictionary.get("current_page") else 0
        # Return an object of this model
        return cls(data,
                   has_next_page,
                   current_page)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'data={(self.data if hasattr(self, "data") else None)!r}, '
                f'has_next_page={(self.has_next_page if hasattr(self, "has_next_page") else None)!r}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'data={(self.data if hasattr(self, "data") else None)!s}, '
                f'has_next_page={(self.has_next_page if hasattr(self, "has_next_page") else None)!s}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!s})')
