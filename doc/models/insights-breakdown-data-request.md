
# Insights Breakdown Data Request

## Structure

`InsightsBreakdownDataRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `breakdowns` | [`List[Breakdown]`](../../doc/models/breakdown.md) | Required | Gumlet API supports response for multiple breakdowns in a single API request. |
| `property_id` | `str` | Required | The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard. |
| `timeframe` | [`Timeframe1`](../../doc/models/timeframe-1.md) | Required | The timeframe to get the data for. Currently we only support maximum difference between `start_at` and `end_at` to be *60 days*. |
| `filters` | [`List[Filters1]`](../../doc/models/filters-1.md) | Optional | Drill down data in breakdowns with multiple filters, `value` should be an exact match |

## Example (as JSON)

```json
{
  "breakdowns": [
    {
      "name": "custom_data_7",
      "metric": "average_bitrate",
      "page": 1,
      "page_size": 10,
      "search": "search2",
      "sort": {
        "by": "key",
        "order": "asc"
      }
    }
  ],
  "property_id": "property_id6",
  "timeframe": {
    "start_at": "2016-03-13T12:52:32.123Z",
    "end_at": "2016-03-13T12:52:32.123Z"
  },
  "filters": [
    {
      "name": "meta_operating_system_version",
      "value": "value2",
      "operator": "contains"
    }
  ]
}
```

