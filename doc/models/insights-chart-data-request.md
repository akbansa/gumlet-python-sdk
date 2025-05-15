
# Insights Chart Data Request

## Structure

`InsightsChartDataRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metrics` | `List[str]` | Required | Get data for one or more `metrics` in the same request. Please add any of these metrics. `views`, `unique_views`, `downscale_percentage`,`upscale_percentage`, `rebuffer_percentage`, `startup_time`, `player_startup_time`, `seek_latency`, `exits_before_startup`, `playback_failure_percentage`, `completion_percent`, `completion_percent_by_views`, `rebuffer_duration`, `playing_time`, `rebuffer_count`, `rebuffer_frequency`, `average_bitrate`, `concurrent_users`, `playback_rate` |
| `property_id` | `str` | Required | The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard. |
| `timeframe` | [`Timeframe`](../../doc/models/timeframe.md) | Required | The timeframe to get the data for. Currently we only support a maximum of *60 days* between `start_at` and `end_at`. If `group_by` parameter is set as `hourly` then maximum difference between `start_at` and `end_at` can be *seven days*. |
| `filters` | [`List[Filters1]`](../../doc/models/filters-1.md) | Optional | Build *segments* of users using multiple filters on the data, `value` should be an *exact match* |
| `group_by` | [`GroupByEnum`](../../doc/models/group-by-enum.md) | Optional | Data can be grouped by `daily` or `hourly`. Metrics with histogram response (`completion_percent`, `completion_percent_by_views`) can not be grouped hourly<br><br>**Default**: `'daily'` |

## Example (as JSON)

```json
{
  "metrics": [
    "metrics0",
    "metrics1"
  ],
  "property_id": "property_id2",
  "timeframe": {
    "start_at": "2016-03-13T12:52:32.123Z",
    "end_at": "2016-03-13T12:52:32.123Z"
  },
  "group_by": "daily",
  "filters": [
    {
      "name": "meta_operating_system_version",
      "value": "value2",
      "operator": "contains"
    },
    {
      "name": "meta_operating_system_version",
      "value": "value2",
      "operator": "contains"
    }
  ]
}
```

