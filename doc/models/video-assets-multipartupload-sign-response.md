
# Video Assets Multipartupload Sign Response

## Structure

`VideoAssetsMultipartuploadSignResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_id` | `str` | Optional | - |
| `part_number` | `str` | Optional | - |
| `part_upload_url` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "asset_id": "642db9d6cc21a55eb474a0b2",
  "part_number": "1",
  "part_upload_url": "https://gumlet-video-user-uploads.s3.us-west-2.amazonaws.com/gumlet-user-uploads-prod/600e2eccc1be42e7a5b29427/642db9d6cc21c21eb474a0c1/origin-642db9d6cc21a55eb474a0c1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA4WNLTXWDOHE3WKEQ%2F20230405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230405T181136Z&X-Amz-Expires=3600&X-Amz-Signature=23d23ca56dceab55ba16349609af7d0921361ced905dde848b6206aa3de0205a&X-Amz-SignedHeaders=host&partNumber=1&uploadId=rkY.tbFdsN14Obcdh.VpVvGdtVxipAa2dyKszL2g7ETT38TXucloiyJLtz9Ff79OgvM3tdsFdenolTgdaIy_jo7GyArbApbueZZ9oLM3k7tuHkX9wXyOMDbGRQ3V0q4W&x-id=UploadPart"
}
```

