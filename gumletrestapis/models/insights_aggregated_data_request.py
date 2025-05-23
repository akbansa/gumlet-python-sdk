# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper
from gumletrestapis.models.aggregate import Aggregate
from gumletrestapis.models.filters_1 import Filters1
from gumletrestapis.models.timeframe_2 import Timeframe2


class InsightsAggregatedDataRequest(object):

    """Implementation of the 'Insights Aggregated Data Request' model.

    Attributes:
        aggregate (List[Aggregate]): Aggregate multiple metrics at the same
            time
        property_id (str): The five to ten character unique identifier of the
            Gumlet Insight Property available on the dashboard.
        timeframe (Timeframe2): The timeframe to get the data for. Currently
            we only support maximum difference between `start_at` and `end_at`
            to be *60 days*
        filters (List[Filters1]): Get aggregations for metrics with multiple
            filters, `value` should be an exact match

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aggregate": 'aggregate',
        "property_id": 'property_id',
        "timeframe": 'timeframe',
        "filters": 'filters'
    }

    _optionals = [
        'filters',
    ]

    def __init__(self,
                 aggregate=None,
                 property_id=None,
                 timeframe=None,
                 filters=APIHelper.SKIP):
        """Constructor for the InsightsAggregatedDataRequest class"""

        # Initialize members of the class
        self.aggregate = aggregate 
        self.property_id = property_id 
        self.timeframe = timeframe 
        if filters is not APIHelper.SKIP:
            self.filters = filters 

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
        aggregate = None
        if dictionary.get('aggregate') is not None:
            aggregate = [Aggregate.from_dictionary(x) for x in dictionary.get('aggregate')]
        property_id = dictionary.get("property_id") if dictionary.get("property_id") else None
        timeframe = Timeframe2.from_dictionary(dictionary.get('timeframe')) if dictionary.get('timeframe') else None
        filters = None
        if dictionary.get('filters') is not None:
            filters = [Filters1.from_dictionary(x) for x in dictionary.get('filters')]
        else:
            filters = APIHelper.SKIP
        # Return an object of this model
        return cls(aggregate,
                   property_id,
                   timeframe,
                   filters)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'aggregate={self.aggregate!r}, '
                f'property_id={self.property_id!r}, '
                f'timeframe={self.timeframe!r}, '
                f'filters={(self.filters if hasattr(self, "filters") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'aggregate={self.aggregate!s}, '
                f'property_id={self.property_id!s}, '
                f'timeframe={self.timeframe!s}, '
                f'filters={(self.filters if hasattr(self, "filters") else None)!s})')
