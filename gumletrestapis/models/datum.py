# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class Datum(object):

    """Implementation of the 'Datum' model.

    Attributes:
        asset_id (str): The model property of type str.
        units (int): The model property of type int.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "asset_id": 'asset_id',
        "units": 'units'
    }

    _optionals = [
        'asset_id',
        'units',
    ]

    def __init__(self,
                 asset_id=APIHelper.SKIP,
                 units=0):
        """Constructor for the Datum class"""

        # Initialize members of the class
        if asset_id is not APIHelper.SKIP:
            self.asset_id = asset_id 
        self.units = units 

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
        asset_id = dictionary.get("asset_id") if dictionary.get("asset_id") else APIHelper.SKIP
        units = dictionary.get("units") if dictionary.get("units") else 0
        # Return an object of this model
        return cls(asset_id,
                   units)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'asset_id={(self.asset_id if hasattr(self, "asset_id") else None)!r}, '
                f'units={(self.units if hasattr(self, "units") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'asset_id={(self.asset_id if hasattr(self, "asset_id") else None)!s}, '
                f'units={(self.units if hasattr(self, "units") else None)!s})')
