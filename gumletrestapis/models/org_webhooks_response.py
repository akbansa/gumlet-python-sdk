# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class OrgWebhooksResponse(object):

    """Implementation of the 'Org Webhooks Response' model.

    Attributes:
        id (str): The model property of type str.
        url (str): The model property of type str.
        triggers (List[str]): The model property of type List[str].
        created_at (str): The model property of type str.
        updated_at (str): The model property of type str.
        sources (List[str]): The model property of type List[str].
        secret_token (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "url": 'url',
        "triggers": 'triggers',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "sources": 'sources',
        "secret_token": 'secret_token'
    }

    _optionals = [
        'id',
        'url',
        'triggers',
        'created_at',
        'updated_at',
        'sources',
        'secret_token',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 triggers=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 sources=APIHelper.SKIP,
                 secret_token=APIHelper.SKIP):
        """Constructor for the OrgWebhooksResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if url is not APIHelper.SKIP:
            self.url = url 
        if triggers is not APIHelper.SKIP:
            self.triggers = triggers 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if sources is not APIHelper.SKIP:
            self.sources = sources 
        if secret_token is not APIHelper.SKIP:
            self.secret_token = secret_token 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        triggers = dictionary.get("triggers") if dictionary.get("triggers") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        sources = dictionary.get("sources") if dictionary.get("sources") else APIHelper.SKIP
        secret_token = dictionary.get("secret_token") if dictionary.get("secret_token") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   url,
                   triggers,
                   created_at,
                   updated_at,
                   sources,
                   secret_token)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'url={(self.url if hasattr(self, "url") else None)!r}, '
                f'triggers={(self.triggers if hasattr(self, "triggers") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'sources={(self.sources if hasattr(self, "sources") else None)!r}, '
                f'secret_token={(self.secret_token if hasattr(self, "secret_token") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'url={(self.url if hasattr(self, "url") else None)!s}, '
                f'triggers={(self.triggers if hasattr(self, "triggers") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'sources={(self.sources if hasattr(self, "sources") else None)!s}, '
                f'secret_token={(self.secret_token if hasattr(self, "secret_token") else None)!s})')
