
# Views

## Structure

`Views`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Datum1]`](../../doc/models/datum-1.md) | Optional | - |
| `has_next_page` | `bool` | Optional | **Default**: `True` |
| `current_page` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "has_next_page": false,
  "current_page": 1,
  "data": [
    {
      "key": "key0",
      "value": 90,
      "unit": "unit8"
    },
    {
      "key": "key0",
      "value": 90,
      "unit": "unit8"
    }
  ]
}
```

