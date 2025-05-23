# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper
from gumletrestapis.models.transformations_6 import Transformations6


class VideoProfilesResponse2(object):

    """Implementation of the 'Video Profiles Response2' model.

    Attributes:
        profile_id (str): The model property of type str.
        name (str): The model property of type str.
        transformations (Transformations6): The model property of type
            Transformations6.
        created_at (int): The model property of type int.
        updated_at (int): The model property of type int.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "profile_id": 'profile_id',
        "name": 'name',
        "transformations": 'transformations',
        "created_at": 'created_at',
        "updated_at": 'updated_at'
    }

    _optionals = [
        'profile_id',
        'name',
        'transformations',
        'created_at',
        'updated_at',
    ]

    def __init__(self,
                 profile_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 transformations=APIHelper.SKIP,
                 created_at=0,
                 updated_at=0):
        """Constructor for the VideoProfilesResponse2 class"""

        # Initialize members of the class
        if profile_id is not APIHelper.SKIP:
            self.profile_id = profile_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if transformations is not APIHelper.SKIP:
            self.transformations = transformations 
        self.created_at = created_at 
        self.updated_at = updated_at 

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
        profile_id = dictionary.get("profile_id") if dictionary.get("profile_id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        transformations = Transformations6.from_dictionary(dictionary.get('transformations')) if 'transformations' in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else 0
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else 0
        # Return an object of this model
        return cls(profile_id,
                   name,
                   transformations,
                   created_at,
                   updated_at)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'profile_id={(self.profile_id if hasattr(self, "profile_id") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'transformations={(self.transformations if hasattr(self, "transformations") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'profile_id={(self.profile_id if hasattr(self, "profile_id") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'transformations={(self.transformations if hasattr(self, "transformations") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s})')
