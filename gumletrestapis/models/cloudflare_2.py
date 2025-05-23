# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class Cloudflare2(object):

    """Implementation of the 'Cloudflare2' model.

    This is a required field if source type is cloudflare.

    Attributes:
        bucket_name (str): The model property of type str.
        access_key (str): The model property of type str.
        account_id (str): The model property of type str.
        secret (str): The model property of type str.
        base_path (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bucket_name": 'bucket_name',
        "access_key": 'access_key',
        "account_id": 'account_id',
        "secret": 'secret',
        "base_path": 'base_path'
    }

    _optionals = [
        'base_path',
    ]

    def __init__(self,
                 bucket_name=None,
                 access_key=None,
                 account_id=None,
                 secret=None,
                 base_path=APIHelper.SKIP):
        """Constructor for the Cloudflare2 class"""

        # Initialize members of the class
        self.bucket_name = bucket_name 
        self.access_key = access_key 
        self.account_id = account_id 
        self.secret = secret 
        if base_path is not APIHelper.SKIP:
            self.base_path = base_path 

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
        bucket_name = dictionary.get("bucket_name") if dictionary.get("bucket_name") else None
        access_key = dictionary.get("access_key") if dictionary.get("access_key") else None
        account_id = dictionary.get("account_id") if dictionary.get("account_id") else None
        secret = dictionary.get("secret") if dictionary.get("secret") else None
        base_path = dictionary.get("base_path") if dictionary.get("base_path") else APIHelper.SKIP
        # Return an object of this model
        return cls(bucket_name,
                   access_key,
                   account_id,
                   secret,
                   base_path)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'bucket_name={self.bucket_name!r}, '
                f'access_key={self.access_key!r}, '
                f'account_id={self.account_id!r}, '
                f'secret={self.secret!r}, '
                f'base_path={(self.base_path if hasattr(self, "base_path") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'bucket_name={self.bucket_name!s}, '
                f'access_key={self.access_key!s}, '
                f'account_id={self.account_id!s}, '
                f'secret={self.secret!s}, '
                f'base_path={(self.base_path if hasattr(self, "base_path") else None)!s})')
