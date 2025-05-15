
# Player Config 2

Configure player settings for this playlist, it overrides the setting set on collection.

## Structure

`PlayerConfig2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `preload` | `bool` | Optional | - |
| `autoplay` | `bool` | Optional | - |
| `disable_seek` | `bool` | Optional | - |
| `disable_player_controls` | `bool` | Optional | - |
| `powered_by_gumlet_overlay` | `bool` | Optional | - |
| `allow_drm_protected_videos` | `bool` | Optional | - |
| `loop` | `bool` | Optional | - |
| `player_color` | `str` | Optional | - |
| `include_seo` | `bool` | Optional | - |
| `subtitle_enabled` | `bool` | Optional | - |
| `pixel_tags` | `Any` | Optional | - |
| `logo_width` | `int` | Optional | - |
| `logo_height` | `int` | Optional | - |
| `dynamic_watermark` | `bool` | Optional | - |
| `watermark_font_size` | `int` | Optional | - |
| `watermark_font_color` | `str` | Optional | - |
| `watermark_bg_color` | `str` | Optional | - |
| `watermark_interval` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "preload": false,
  "autoplay": false,
  "disable_seek": false,
  "disable_player_controls": false,
  "powered_by_gumlet_overlay": false
}
```

