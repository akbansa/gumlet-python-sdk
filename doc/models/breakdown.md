
# Breakdown

## Structure

`Breakdown`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`Name1Enum`](../../doc/models/name-1-enum.md) | Required | The name of a breakdown to get the data for. |
| `metric` | [`MetricEnum`](../../doc/models/metric-enum.md) | Required | Metric for the breakdown data. |
| `page` | `int` | Optional | Request a particular page number for the response.<br><br>**Default**: `1` |
| `search` | `str` | Optional | The API supports partially matching strings. |
| `sort` | [`Sort`](../../doc/models/sort.md) | Optional | Sort the response data according to key or value |
| `page_size` | `int` | Optional | The number of items returned in a single page. Maximum value can be 100<br><br>**Default**: `10` |

## Example (as JSON)

```json
{
  "name": "user_country",
  "metric": "rebuffer_count",
  "page": 1,
  "page_size": 10,
  "search": "search6",
  "sort": {
    "by": "key",
    "order": "asc"
  }
}
```

