
# Video Assets Response 1

## Structure

`VideoAssetsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_id` | `str` | Optional | - |
| `progress` | `int` | Optional | **Default**: `0` |
| `created_at` | `int` | Optional | **Default**: `0` |
| `updated_at` | `int` | Optional | **Default**: `0` |
| `status` | `str` | Optional | - |
| `tag` | `List[str]` | Optional | - |
| `source_id` | `str` | Optional | - |
| `collection_id` | `str` | Optional | - |
| `input` | [`Input2`](../../doc/models/input-2.md) | Optional | - |
| `output` | [`Output2`](../../doc/models/output-2.md) | Optional | - |
| `processed_at` | `int` | Optional | **Default**: `0` |
| `folder` | `str` | Optional | - |
| `playlists` | `List[Any]` | Optional | - |

## Example (as JSON)

```json
{
  "asset_id": "67e4ece9403562dbea654261",
  "progress": 100,
  "created_at": 1743056105661,
  "updated_at": 1743056105661,
  "status": "ready",
  "source_id": "67e4ece9403562dbea65425f",
  "collection_id": "67e4ece9403562dbea65425f",
  "processed_at": 1743056105661,
  "folder": "Demo Folder"
}
```

