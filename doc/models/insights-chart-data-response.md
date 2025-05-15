
# Insights Chart Data Response

## Structure

`InsightsChartDataResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `views` | [`List[View]`](../../doc/models/view.md) | Optional | - |
| `unique_views` | [`List[UniqueView]`](../../doc/models/unique-view.md) | Optional | - |

## Example (as JSON)

```json
{
  "views": [
    {
      "x": 136,
      "y": {
        "key1": "val1",
        "key2": "val2"
      },
      "unit": "unit0"
    }
  ],
  "unique_views": [
    {
      "x": 228,
      "y": {
        "key1": "val1",
        "key2": "val2"
      },
      "unit": "unit8"
    },
    {
      "x": 228,
      "y": {
        "key1": "val1",
        "key2": "val2"
      },
      "unit": "unit8"
    }
  ]
}
```

