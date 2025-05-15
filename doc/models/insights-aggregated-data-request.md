
# Insights Aggregated Data Request

## Structure

`InsightsAggregatedDataRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aggregate` | [`List[Aggregate]`](../../doc/models/aggregate.md) | Required | Aggregate multiple metrics at the same time |
| `property_id` | `str` | Required | The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard. |
| `timeframe` | [`Timeframe2`](../../doc/models/timeframe-2.md) | Required | The timeframe to get the data for. Currently we only support maximum difference between `start_at` and `end_at` to be *60 days* |
| `filters` | [`List[Filters1]`](../../doc/models/filters-1.md) | Optional | Get aggregations for metrics with multiple filters, `value` should be an exact match |

## Example (as JSON)

```json
{
  "aggregate": [
    {
      "metric": "average_bitrate",
      "function": "sum"
    }
  ],
  "property_id": "property_id8",
  "timeframe": {
    "start_at": "2016-03-13",
    "end_at": "2016-03-13"
  },
  "filters": [
    {
      "name": "meta_operating_system_version",
      "value": "value2",
      "operator": "contains"
    },
    {
      "name": "meta_operating_system_version",
      "value": "value2",
      "operator": "contains"
    }
  ]
}
```

