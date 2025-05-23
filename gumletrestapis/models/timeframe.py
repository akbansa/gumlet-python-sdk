# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class Timeframe(object):

    """Implementation of the 'Timeframe' model.

    The timeframe to get the data for. Currently we only support a maximum of
    *60 days* between `start_at` and `end_at`. If `group_by` parameter is set
    as `hourly` then maximum difference between `start_at` and `end_at` can be
    *seven days*.

    Attributes:
        start_at (datetime): Use <b>yyyy-MM-ddThh:mm:ss</b> format
        end_at (datetime): Use <b>yyyy-MM-ddThh:mm:ss</b> format

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_at": 'start_at',
        "end_at": 'end_at'
    }

    def __init__(self,
                 start_at=None,
                 end_at=None):
        """Constructor for the Timeframe class"""

        # Initialize members of the class
        self.start_at = APIHelper.apply_datetime_converter(start_at, APIHelper.RFC3339DateTime) if start_at else None 
        self.end_at = APIHelper.apply_datetime_converter(end_at, APIHelper.RFC3339DateTime) if end_at else None 

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
        start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None
        end_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_at")).datetime if dictionary.get("end_at") else None
        # Return an object of this model
        return cls(start_at,
                   end_at)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'start_at={self.start_at!r}, '
                f'end_at={self.end_at!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'start_at={self.start_at!s}, '
                f'end_at={self.end_at!s})')
