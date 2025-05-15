
# All Live Asset

## Structure

`AllLiveAsset`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | - |
| `stream_key` | `str` | Optional | - |
| `live_asset_id` | `str` | Optional | - |
| `live_video_source_id` | `str` | Optional | - |
| `input` | [`Input4`](../../doc/models/input-4.md) | Optional | - |
| `stream_url` | `str` | Optional | - |
| `output` | [`Output4`](../../doc/models/output-4.md) | Optional | - |
| `created_at` | `int` | Optional | **Default**: `0` |
| `updated_at` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "status": "created",
  "stream_key": "619231610822a81d955d22f4",
  "live_asset_id": "619231610822a81d955d22f3",
  "live_video_source_id": "6165247368d80232d28d4379",
  "stream_url": "rtmp://livestream-ingest.gumlet.io:1935/app/619231610822a81d955d22f4",
  "created_at": 1636970849188,
  "updated_at": 1636970849188,
  "input": {
    "resolution": [
      "resolution9",
      "resolution0",
      "resolution1"
    ]
  }
}
```

