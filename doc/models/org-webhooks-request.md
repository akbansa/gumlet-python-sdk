
# Org Webhooks Request

## Structure

`OrgWebhooksRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | URL from the application you want to send data to. |
| `secret_token` | `str` | Required | Authentication token to ensure legitimacy of Gumlet Webhook request on your application. |
| `triggers` | `List[str]` | Required | Triggers for the invocation of webhookos, supported option is `status`. |
| `sources` | `List[str]` | Required | List of video collection identifiers for which webhooks are needed to be invoked. |

## Example (as JSON)

```json
{
  "url": "url2",
  "secret_token": "secret_token4",
  "triggers": [
    "triggers2",
    "triggers3"
  ],
  "sources": [
    "sources0",
    "sources1"
  ]
}
```

