
# Sort

Sort the response data according to key or value

## Structure

`Sort`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `by` | [`ByEnum`](../../doc/models/by-enum.md) | Required | **Default**: `'key'` |
| `order` | [`OrderEnum`](../../doc/models/order-enum.md) | Required | **Default**: `'asc'` |

## Example (as JSON)

```json
{
  "by": "key",
  "order": "asc"
}
```

