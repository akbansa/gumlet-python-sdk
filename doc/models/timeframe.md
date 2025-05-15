
# Timeframe

The timeframe to get the data for. Currently we only support a maximum of *60 days* between `start_at` and `end_at`. If `group_by` parameter is set as `hourly` then maximum difference between `start_at` and `end_at` can be *seven days*.

## Structure

`Timeframe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_at` | `datetime` | Required | Use <b>yyyy-MM-ddThh:mm:ss</b> format |
| `end_at` | `datetime` | Required | Use <b>yyyy-MM-ddThh:mm:ss</b> format |

## Example (as JSON)

```json
{
  "start_at": "2016-03-13T12:52:32.123Z",
  "end_at": "2016-03-13T12:52:32.123Z"
}
```

