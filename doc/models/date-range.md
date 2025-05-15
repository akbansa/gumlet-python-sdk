
# Date Range

The timeframe to get the data for. Currently we only support a maximum of 60 days between `start_at` and `end_at`.

## Structure

`DateRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_at` | `date` | Optional | The starting date to consider |
| `end_at` | `date` | Optional | The ending date to consider |

## Example (as JSON)

```json
{
  "start_at": "2016-03-13",
  "end_at": "2016-03-13"
}
```

