
# All Asset

## Structure

`AllAsset`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_id` | `str` | Optional | - |
| `progress` | `int` | Optional | **Default**: `0` |
| `created_at` | `int` | Optional | **Default**: `0` |
| `status` | `str` | Optional | - |
| `tag` | `str` | Optional | - |
| `source_id` | `str` | Optional | - |
| `input` | [`Input3`](../../doc/models/input-3.md) | Optional | - |
| `output` | [`Output`](../../doc/models/output.md) | Optional | - |

## Example (as JSON)

```json
{
  "asset_id": "6192269e0822a81d955d1a4b",
  "progress": 0,
  "created_at": 1636968094594,
  "status": "optimizing",
  "source_id": "5f462c1561cf8a766464ffc4",
  "tag": "tag0"
}
```

