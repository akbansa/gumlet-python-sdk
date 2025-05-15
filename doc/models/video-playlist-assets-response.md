
# Video Playlist Assets Response

## Structure

`VideoPlaylistAssetsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_list` | [`List[AssetList1]`](../../doc/models/asset-list-1.md) | Optional | - |
| `has_next_page` | `bool` | Optional | **Default**: `True` |
| `next_page` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "has_next_page": true,
  "next_page": 2,
  "asset_list": [
    {
      "id": "id4",
      "title": "title0",
      "description": "description4",
      "status": "status6",
      "created_at": "created_at2"
    },
    {
      "id": "id4",
      "title": "title0",
      "description": "description4",
      "status": "status6",
      "created_at": "created_at2"
    },
    {
      "id": "id4",
      "title": "title0",
      "description": "description4",
      "status": "status6",
      "created_at": "created_at2"
    }
  ]
}
```

