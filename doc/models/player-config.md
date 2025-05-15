
# Player Config

## Structure

`PlayerConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `preload` | `bool` | Optional | **Default**: `True` |
| `autoplay` | `bool` | Optional | **Default**: `True` |
| `disable_seek` | `bool` | Optional | **Default**: `True` |
| `disable_player_controls` | `bool` | Optional | **Default**: `True` |
| `powered_by_gumlet_overlay` | `bool` | Optional | **Default**: `True` |
| `allow_drm_protected_videos` | `bool` | Optional | **Default**: `True` |
| `loop` | `bool` | Optional | **Default**: `True` |
| `player_color` | `str` | Optional | - |
| `include_seo` | `bool` | Optional | **Default**: `True` |
| `subtitle_enabled` | `bool` | Optional | **Default**: `True` |
| `pixel_tags` | `Any` | Optional | - |
| `logo_width` | `int` | Optional | **Default**: `0` |
| `logo_height` | `int` | Optional | **Default**: `0` |
| `dynamic_watermark` | `bool` | Optional | **Default**: `True` |
| `watermark_font_size` | `int` | Optional | **Default**: `0` |
| `watermark_font_color` | `str` | Optional | - |
| `watermark_bg_color` | `str` | Optional | - |
| `watermark_interval` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "preload": false,
  "autoplay": false,
  "disable_seek": false,
  "disable_player_controls": false,
  "powered_by_gumlet_overlay": false,
  "allow_drm_protected_videos": false,
  "loop": false,
  "player_color": "#6658ea",
  "include_seo": true,
  "subtitle_enabled": false,
  "logo_width": 100,
  "logo_height": 100,
  "dynamic_watermark": false,
  "watermark_font_size": 20,
  "watermark_font_color": "#ff0000",
  "watermark_bg_color": "transparent",
  "watermark_interval": 1000
}
```

