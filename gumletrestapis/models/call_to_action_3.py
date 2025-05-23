# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class CallToAction3(object):

    """Implementation of the 'CallToAction3' model.

    Attributes:
        start_time (int): The model property of type int.
        end_time (int): The model property of type int.
        text (str): The model property of type str.
        url (str): The model property of type str.
        html_target (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_time": 'start_time',
        "end_time": 'end_time',
        "text": 'text',
        "url": 'url',
        "html_target": 'html_target'
    }

    _optionals = [
        'start_time',
        'end_time',
        'text',
        'url',
        'html_target',
    ]

    def __init__(self,
                 start_time=0,
                 end_time=0,
                 text=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 html_target=APIHelper.SKIP):
        """Constructor for the CallToAction3 class"""

        # Initialize members of the class
        self.start_time = start_time 
        self.end_time = end_time 
        if text is not APIHelper.SKIP:
            self.text = text 
        if url is not APIHelper.SKIP:
            self.url = url 
        if html_target is not APIHelper.SKIP:
            self.html_target = html_target 

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
        start_time = dictionary.get("start_time") if dictionary.get("start_time") else 0
        end_time = dictionary.get("end_time") if dictionary.get("end_time") else 0
        text = dictionary.get("text") if dictionary.get("text") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        html_target = dictionary.get("html_target") if dictionary.get("html_target") else APIHelper.SKIP
        # Return an object of this model
        return cls(start_time,
                   end_time,
                   text,
                   url,
                   html_target)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'start_time={(self.start_time if hasattr(self, "start_time") else None)!r}, '
                f'end_time={(self.end_time if hasattr(self, "end_time") else None)!r}, '
                f'text={(self.text if hasattr(self, "text") else None)!r}, '
                f'url={(self.url if hasattr(self, "url") else None)!r}, '
                f'html_target={(self.html_target if hasattr(self, "html_target") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'start_time={(self.start_time if hasattr(self, "start_time") else None)!s}, '
                f'end_time={(self.end_time if hasattr(self, "end_time") else None)!s}, '
                f'text={(self.text if hasattr(self, "text") else None)!s}, '
                f'url={(self.url if hasattr(self, "url") else None)!s}, '
                f'html_target={(self.html_target if hasattr(self, "html_target") else None)!s})')
