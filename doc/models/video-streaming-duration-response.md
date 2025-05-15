
# Video Streaming Duration Response

## Structure

`VideoStreamingDurationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[Datum]`](../../doc/models/datum.md) | Optional | - |
| `has_next_page` | `bool` | Optional | **Default**: `True` |

## Example (as JSON)

```json
{
  "has_next_page": false,
  "data": [
    {
      "asset_id": "asset_id6",
      "units": 140
    },
    {
      "asset_id": "asset_id6",
      "units": 140
    }
  ]
}
```

