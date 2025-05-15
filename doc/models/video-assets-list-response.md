
# Video Assets List Response

## Structure

`VideoAssetsListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `all_assets` | [`List[AllAsset]`](../../doc/models/all-asset.md) | Optional | - |
| `total_asset_count` | `int` | Optional | **Default**: `0` |
| `current_offset` | `int` | Optional | **Default**: `0` |
| `distinct_tags` | `List[str]` | Optional | - |

## Example (as JSON)

```json
{
  "total_asset_count": 2159,
  "current_offset": 1,
  "all_assets": [
    {
      "asset_id": "asset_id2",
      "progress": 192,
      "created_at": 66,
      "status": "status8",
      "tag": "tag0"
    },
    {
      "asset_id": "asset_id2",
      "progress": 192,
      "created_at": 66,
      "status": "status8",
      "tag": "tag0"
    }
  ],
  "distinct_tags": [
    "distinct_tags2"
  ]
}
```

