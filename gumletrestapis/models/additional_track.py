# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class AdditionalTrack(object):

    """Implementation of the 'AdditionalTrack' model.

    Attributes:
        url (str): URL or web address of a file that Gumlet should download to
            add a stream.
        mtype (str): Type of additional track. Value can be either audio or
            subtitle.
        language_code (str): The language code value represents BCP 47
            specification compliant value. For example, en for English.
        name (str): The name of the track containing a human-readable
            description.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url',
        "mtype": 'type',
        "language_code": 'language_code',
        "name": 'name'
    }

    _optionals = [
        'name',
    ]

    def __init__(self,
                 url=None,
                 mtype=None,
                 language_code=None,
                 name=APIHelper.SKIP):
        """Constructor for the AdditionalTrack class"""

        # Initialize members of the class
        self.url = url 
        self.mtype = mtype 
        self.language_code = language_code 
        if name is not APIHelper.SKIP:
            self.name = name 

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
        url = dictionary.get("url") if dictionary.get("url") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        language_code = dictionary.get("language_code") if dictionary.get("language_code") else None
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(url,
                   mtype,
                   language_code,
                   name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'url={self.url!r}, '
                f'mtype={self.mtype!r}, '
                f'language_code={self.language_code!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'url={self.url!s}, '
                f'mtype={self.mtype!s}, '
                f'language_code={self.language_code!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s})')
