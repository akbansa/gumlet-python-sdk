
# Filters 1

## Structure

`Filters1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`NameEnum`](../../doc/models/name-enum.md) | Required | Name of the breakdown to filter data on. |
| `value` | `str` | Required | Value to be matched for the given filter name. Currently we support exact matches. |
| `operator` | [`OperatorEnum`](../../doc/models/operator-enum.md) | Optional | Operator to be used while filtering the data<br><br>**Default**: `'equals'` |

## Example (as JSON)

```json
{
  "name": "custom_video_id",
  "value": "value8",
  "operator": "equals"
}
```

