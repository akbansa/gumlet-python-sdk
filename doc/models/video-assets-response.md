
# Video Assets Response

## Structure

`VideoAssetsResponse`

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
| `input` | [`Input`](../../doc/models/input.md) | Optional | - |
| `output` | [`Output`](../../doc/models/output.md) | Optional | - |
| `playlists` | `List[str]` | Optional | - |

## Example (as JSON)

```json
{
  "asset_id": "65b168a6e99b77f116c0e488",
  "progress": 0,
  "created_at": 1706125479006,
  "updated_at": 1706125479006,
  "status": "pre-queued",
  "source_id": "646df1c9173a4a2fcac180b4",
  "collection_id": "646df1c9173a4a2fcac180b4"
}
```

