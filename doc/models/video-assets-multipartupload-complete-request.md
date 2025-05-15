
# Video Assets Multipartupload Complete Request

## Structure

`VideoAssetsMultipartuploadCompleteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `parts` | [`List[Part]`](../../doc/models/part.md) | Optional | List of object containing part number with ETag received as a response header while uploading each part |

## Example (as JSON)

```json
{
  "parts": [
    {
      "PartNumber": 20,
      "ETag": "ETag8"
    },
    {
      "PartNumber": 20,
      "ETag": "ETag8"
    },
    {
      "PartNumber": 20,
      "ETag": "ETag8"
    }
  ]
}
```

