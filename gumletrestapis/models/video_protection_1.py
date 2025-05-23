# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class VideoProtection1(object):

    """Implementation of the 'VideoProtection1' model.

    Gumlet provides multiple options for securing your video playback.

    Attributes:
        signed_url (bool): The model property of type bool.
        signed_url_secret (str): The model property of type str.
        blacklisted_countries (List[str]): Example: ["IN","USA"]
        whitelisted_referrers (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signed_url": 'signed_url',
        "signed_url_secret": 'signed_url_secret',
        "blacklisted_countries": 'blacklisted_countries',
        "whitelisted_referrers": 'whitelisted_referrers'
    }

    _optionals = [
        'signed_url',
        'signed_url_secret',
        'blacklisted_countries',
        'whitelisted_referrers',
    ]

    def __init__(self,
                 signed_url=False,
                 signed_url_secret=APIHelper.SKIP,
                 blacklisted_countries=APIHelper.SKIP,
                 whitelisted_referrers=APIHelper.SKIP):
        """Constructor for the VideoProtection1 class"""

        # Initialize members of the class
        self.signed_url = signed_url 
        if signed_url_secret is not APIHelper.SKIP:
            self.signed_url_secret = signed_url_secret 
        if blacklisted_countries is not APIHelper.SKIP:
            self.blacklisted_countries = blacklisted_countries 
        if whitelisted_referrers is not APIHelper.SKIP:
            self.whitelisted_referrers = whitelisted_referrers 

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
        signed_url = dictionary.get("signed_url") if dictionary.get("signed_url") else False
        signed_url_secret = dictionary.get("signed_url_secret") if dictionary.get("signed_url_secret") else APIHelper.SKIP
        blacklisted_countries = dictionary.get("blacklisted_countries") if dictionary.get("blacklisted_countries") else APIHelper.SKIP
        whitelisted_referrers = dictionary.get("whitelisted_referrers") if dictionary.get("whitelisted_referrers") else APIHelper.SKIP
        # Return an object of this model
        return cls(signed_url,
                   signed_url_secret,
                   blacklisted_countries,
                   whitelisted_referrers)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'signed_url={(self.signed_url if hasattr(self, "signed_url") else None)!r}, '
                f'signed_url_secret={(self.signed_url_secret if hasattr(self, "signed_url_secret") else None)!r}, '
                f'blacklisted_countries={(self.blacklisted_countries if hasattr(self, "blacklisted_countries") else None)!r}, '
                f'whitelisted_referrers={(self.whitelisted_referrers if hasattr(self, "whitelisted_referrers") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'signed_url={(self.signed_url if hasattr(self, "signed_url") else None)!s}, '
                f'signed_url_secret={(self.signed_url_secret if hasattr(self, "signed_url_secret") else None)!s}, '
                f'blacklisted_countries={(self.blacklisted_countries if hasattr(self, "blacklisted_countries") else None)!s}, '
                f'whitelisted_referrers={(self.whitelisted_referrers if hasattr(self, "whitelisted_referrers") else None)!s})')
