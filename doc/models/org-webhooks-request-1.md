
# Org Webhooks Request 1

## Structure

`OrgWebhooksRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | URL from the application you want to send data to. |
| `secret_token` | `str` | Optional | Authentication token to ensure legitimacy of Gumlet Webhook request on your application. |
| `triggers` | `str` | Optional | Triggers for the invocation of webhookos, supported option is `status`. |
| `sources` | `str` | Optional | List of video collection identifiers for which webhooks are needed to be invoked. |

## Example (as JSON)

```json
{
  "url": "url2",
  "secret_token": "secret_token4",
  "triggers": "triggers2",
  "sources": "sources8"
}
```

