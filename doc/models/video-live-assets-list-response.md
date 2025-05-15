
# Video Live Assets List Response

## Structure

`VideoLiveAssetsListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `all_live_assets` | [`List[AllLiveAsset]`](../../doc/models/all-live-asset.md) | Optional | - |
| `total_live_asset_count` | `int` | Optional | **Default**: `0` |
| `current_offset` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "total_live_asset_count": 5,
  "current_offset": 5,
  "all_live_assets": [
    {
      "status": "status4",
      "stream_key": "stream_key2",
      "live_asset_id": "live_asset_id6",
      "live_video_source_id": "live_video_source_id6",
      "input": {
        "resolution": [
          "resolution9",
          "resolution0",
          "resolution1"
        ]
      }
    },
    {
      "status": "status4",
      "stream_key": "stream_key2",
      "live_asset_id": "live_asset_id6",
      "live_video_source_id": "live_video_source_id6",
      "input": {
        "resolution": [
          "resolution9",
          "resolution0",
          "resolution1"
        ]
      }
    },
    {
      "status": "status4",
      "stream_key": "stream_key2",
      "live_asset_id": "live_asset_id6",
      "live_video_source_id": "live_video_source_id6",
      "input": {
        "resolution": [
          "resolution9",
          "resolution0",
          "resolution1"
        ]
      }
    }
  ]
}
```

