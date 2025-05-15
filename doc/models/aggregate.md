
# Aggregate

## Structure

`Aggregate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metric` | [`Metric1Enum`](../../doc/models/metric-1-enum.md) | Required | The metric to be aggregated for this request. |
| `function` | [`FunctionEnum`](../../doc/models/function-enum.md) | Required | Aggregation function which is to be used. |

## Example (as JSON)

```json
{
  "metric": "upscale_percentage",
  "function": "sum"
}
```

