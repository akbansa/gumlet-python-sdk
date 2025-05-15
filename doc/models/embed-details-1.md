
# Embed Details 1

## Structure

`EmbedDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `powered_by_gumlet_overlay` | `bool` | Optional | **Default**: `True` |
| `allow_drm_protected_videos` | `bool` | Optional | **Default**: `True` |
| `preload` | `bool` | Optional | **Default**: `True` |
| `autoplay` | `bool` | Optional | **Default**: `True` |
| `logo_width` | `int` | Optional | **Default**: `0` |
| `logo_height` | `int` | Optional | **Default**: `0` |
| `player_color` | `str` | Optional | - |
| `is_seo` | `bool` | Optional | **Default**: `True` |
| `dynamic_watermark` | `bool` | Optional | **Default**: `True` |
| `watermark_font_size` | `int` | Optional | **Default**: `0` |
| `watermark_font_color` | `str` | Optional | - |
| `watermark_bg_color` | `str` | Optional | - |
| `watermark_interval` | `int` | Optional | **Default**: `0` |
| `disable_seek` | `bool` | Optional | **Default**: `True` |
| `disable_player_controls` | `bool` | Optional | **Default**: `True` |
| `loop` | `bool` | Optional | **Default**: `True` |
| `subtitle_enabled` | `bool` | Optional | **Default**: `True` |

## Example (as JSON)

```json
{
  "powered_by_gumlet_overlay": true,
  "allow_drm_protected_videos": true,
  "preload": true,
  "autoplay": false,
  "logo_width": 100,
  "logo_height": 100,
  "player_color": "#6658ea",
  "is_seo": true,
  "dynamic_watermark": false,
  "watermark_font_size": 20,
  "watermark_font_color": "#ff0000",
  "watermark_bg_color": "transparent",
  "watermark_interval": 1000,
  "disable_seek": false,
  "disable_player_controls": false,
  "loop": false,
  "subtitle_enabled": false
}
```

