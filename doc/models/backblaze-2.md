
# Backblaze 2

This is a required field if source type is backblaze.

## Structure

`Backblaze2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket_name` | `str` | Required | - |
| `bucket_region` | `str` | Optional | bucket_region or endpoint |
| `endpoint` | `str` | Optional | bucket_region or endpoint |
| `access_key` | `str` | Required | - |
| `secret` | `str` | Required | - |
| `base_path` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "bucket_name": "bucket_name0",
  "bucket_region": "bucket_region0",
  "endpoint": "endpoint4",
  "access_key": "access_key4",
  "secret": "secret2",
  "base_path": "base_path2"
}
```

