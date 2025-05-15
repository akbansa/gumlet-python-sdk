
# Org Webhooks Response

## Structure

`OrgWebhooksResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `url` | `str` | Optional | - |
| `triggers` | `List[str]` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `sources` | `List[str]` | Optional | - |
| `secret_token` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": "65eed75eadeea8478f14ebd4",
  "url": "https://webhook.site/16df065a-b398-48bc-b825-b0804979c5f1",
  "created_at": "03/11/2024 10:05:18",
  "updated_at": "03/11/2024 10:05:18",
  "secret_token": "rnVNfIKgnH",
  "triggers": [
    "triggers8",
    "triggers7",
    "triggers6"
  ]
}
```

