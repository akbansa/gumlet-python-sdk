# -*- coding: utf-8 -*-

"""
gumletrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from gumletrestapis.api_helper import APIHelper


class PlayerConfig(object):

    """Implementation of the 'PlayerConfig' model.

    Attributes:
        preload (bool): The model property of type bool.
        autoplay (bool): The model property of type bool.
        disable_seek (bool): The model property of type bool.
        disable_player_controls (bool): The model property of type bool.
        powered_by_gumlet_overlay (bool): The model property of type bool.
        allow_drm_protected_videos (bool): The model property of type bool.
        loop (bool): The model property of type bool.
        player_color (str): The model property of type str.
        include_seo (bool): The model property of type bool.
        subtitle_enabled (bool): The model property of type bool.
        pixel_tags (Any): The model property of type Any.
        logo_width (int): The model property of type int.
        logo_height (int): The model property of type int.
        dynamic_watermark (bool): The model property of type bool.
        watermark_font_size (int): The model property of type int.
        watermark_font_color (str): The model property of type str.
        watermark_bg_color (str): The model property of type str.
        watermark_interval (int): The model property of type int.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "preload": 'preload',
        "autoplay": 'autoplay',
        "disable_seek": 'disable_seek',
        "disable_player_controls": 'disable_player_controls',
        "powered_by_gumlet_overlay": 'powered_by_gumlet_overlay',
        "allow_drm_protected_videos": 'allow_drm_protected_videos',
        "loop": 'loop',
        "player_color": 'player_color',
        "include_seo": 'include_seo',
        "subtitle_enabled": 'subtitle_enabled',
        "pixel_tags": 'pixel_tags',
        "logo_width": 'logo_width',
        "logo_height": 'logo_height',
        "dynamic_watermark": 'dynamic_watermark',
        "watermark_font_size": 'watermark_font_size',
        "watermark_font_color": 'watermark_font_color',
        "watermark_bg_color": 'watermark_bg_color',
        "watermark_interval": 'watermark_interval'
    }

    _optionals = [
        'preload',
        'autoplay',
        'disable_seek',
        'disable_player_controls',
        'powered_by_gumlet_overlay',
        'allow_drm_protected_videos',
        'loop',
        'player_color',
        'include_seo',
        'subtitle_enabled',
        'pixel_tags',
        'logo_width',
        'logo_height',
        'dynamic_watermark',
        'watermark_font_size',
        'watermark_font_color',
        'watermark_bg_color',
        'watermark_interval',
    ]

    def __init__(self,
                 preload=True,
                 autoplay=True,
                 disable_seek=True,
                 disable_player_controls=True,
                 powered_by_gumlet_overlay=True,
                 allow_drm_protected_videos=True,
                 loop=True,
                 player_color=APIHelper.SKIP,
                 include_seo=True,
                 subtitle_enabled=True,
                 pixel_tags=APIHelper.SKIP,
                 logo_width=0,
                 logo_height=0,
                 dynamic_watermark=True,
                 watermark_font_size=0,
                 watermark_font_color=APIHelper.SKIP,
                 watermark_bg_color=APIHelper.SKIP,
                 watermark_interval=0):
        """Constructor for the PlayerConfig class"""

        # Initialize members of the class
        self.preload = preload 
        self.autoplay = autoplay 
        self.disable_seek = disable_seek 
        self.disable_player_controls = disable_player_controls 
        self.powered_by_gumlet_overlay = powered_by_gumlet_overlay 
        self.allow_drm_protected_videos = allow_drm_protected_videos 
        self.loop = loop 
        if player_color is not APIHelper.SKIP:
            self.player_color = player_color 
        self.include_seo = include_seo 
        self.subtitle_enabled = subtitle_enabled 
        if pixel_tags is not APIHelper.SKIP:
            self.pixel_tags = pixel_tags 
        self.logo_width = logo_width 
        self.logo_height = logo_height 
        self.dynamic_watermark = dynamic_watermark 
        self.watermark_font_size = watermark_font_size 
        if watermark_font_color is not APIHelper.SKIP:
            self.watermark_font_color = watermark_font_color 
        if watermark_bg_color is not APIHelper.SKIP:
            self.watermark_bg_color = watermark_bg_color 
        self.watermark_interval = watermark_interval 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        preload = dictionary.get("preload") if dictionary.get("preload") else True
        autoplay = dictionary.get("autoplay") if dictionary.get("autoplay") else True
        disable_seek = dictionary.get("disable_seek") if dictionary.get("disable_seek") else True
        disable_player_controls = dictionary.get("disable_player_controls") if dictionary.get("disable_player_controls") else True
        powered_by_gumlet_overlay = dictionary.get("powered_by_gumlet_overlay") if dictionary.get("powered_by_gumlet_overlay") else True
        allow_drm_protected_videos = dictionary.get("allow_drm_protected_videos") if dictionary.get("allow_drm_protected_videos") else True
        loop = dictionary.get("loop") if dictionary.get("loop") else True
        player_color = dictionary.get("player_color") if dictionary.get("player_color") else APIHelper.SKIP
        include_seo = dictionary.get("include_seo") if dictionary.get("include_seo") else True
        subtitle_enabled = dictionary.get("subtitle_enabled") if dictionary.get("subtitle_enabled") else True
        pixel_tags = dictionary.get("pixel_tags") if dictionary.get("pixel_tags") else APIHelper.SKIP
        logo_width = dictionary.get("logo_width") if dictionary.get("logo_width") else 0
        logo_height = dictionary.get("logo_height") if dictionary.get("logo_height") else 0
        dynamic_watermark = dictionary.get("dynamic_watermark") if dictionary.get("dynamic_watermark") else True
        watermark_font_size = dictionary.get("watermark_font_size") if dictionary.get("watermark_font_size") else 0
        watermark_font_color = dictionary.get("watermark_font_color") if dictionary.get("watermark_font_color") else APIHelper.SKIP
        watermark_bg_color = dictionary.get("watermark_bg_color") if dictionary.get("watermark_bg_color") else APIHelper.SKIP
        watermark_interval = dictionary.get("watermark_interval") if dictionary.get("watermark_interval") else 0
        # Return an object of this model
        return cls(preload,
                   autoplay,
                   disable_seek,
                   disable_player_controls,
                   powered_by_gumlet_overlay,
                   allow_drm_protected_videos,
                   loop,
                   player_color,
                   include_seo,
                   subtitle_enabled,
                   pixel_tags,
                   logo_width,
                   logo_height,
                   dynamic_watermark,
                   watermark_font_size,
                   watermark_font_color,
                   watermark_bg_color,
                   watermark_interval)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'preload={(self.preload if hasattr(self, "preload") else None)!r}, '
                f'autoplay={(self.autoplay if hasattr(self, "autoplay") else None)!r}, '
                f'disable_seek={(self.disable_seek if hasattr(self, "disable_seek") else None)!r}, '
                f'disable_player_controls={(self.disable_player_controls if hasattr(self, "disable_player_controls") else None)!r}, '
                f'powered_by_gumlet_overlay={(self.powered_by_gumlet_overlay if hasattr(self, "powered_by_gumlet_overlay") else None)!r}, '
                f'allow_drm_protected_videos={(self.allow_drm_protected_videos if hasattr(self, "allow_drm_protected_videos") else None)!r}, '
                f'loop={(self.loop if hasattr(self, "loop") else None)!r}, '
                f'player_color={(self.player_color if hasattr(self, "player_color") else None)!r}, '
                f'include_seo={(self.include_seo if hasattr(self, "include_seo") else None)!r}, '
                f'subtitle_enabled={(self.subtitle_enabled if hasattr(self, "subtitle_enabled") else None)!r}, '
                f'pixel_tags={(self.pixel_tags if hasattr(self, "pixel_tags") else None)!r}, '
                f'logo_width={(self.logo_width if hasattr(self, "logo_width") else None)!r}, '
                f'logo_height={(self.logo_height if hasattr(self, "logo_height") else None)!r}, '
                f'dynamic_watermark={(self.dynamic_watermark if hasattr(self, "dynamic_watermark") else None)!r}, '
                f'watermark_font_size={(self.watermark_font_size if hasattr(self, "watermark_font_size") else None)!r}, '
                f'watermark_font_color={(self.watermark_font_color if hasattr(self, "watermark_font_color") else None)!r}, '
                f'watermark_bg_color={(self.watermark_bg_color if hasattr(self, "watermark_bg_color") else None)!r}, '
                f'watermark_interval={(self.watermark_interval if hasattr(self, "watermark_interval") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'preload={(self.preload if hasattr(self, "preload") else None)!s}, '
                f'autoplay={(self.autoplay if hasattr(self, "autoplay") else None)!s}, '
                f'disable_seek={(self.disable_seek if hasattr(self, "disable_seek") else None)!s}, '
                f'disable_player_controls={(self.disable_player_controls if hasattr(self, "disable_player_controls") else None)!s}, '
                f'powered_by_gumlet_overlay={(self.powered_by_gumlet_overlay if hasattr(self, "powered_by_gumlet_overlay") else None)!s}, '
                f'allow_drm_protected_videos={(self.allow_drm_protected_videos if hasattr(self, "allow_drm_protected_videos") else None)!s}, '
                f'loop={(self.loop if hasattr(self, "loop") else None)!s}, '
                f'player_color={(self.player_color if hasattr(self, "player_color") else None)!s}, '
                f'include_seo={(self.include_seo if hasattr(self, "include_seo") else None)!s}, '
                f'subtitle_enabled={(self.subtitle_enabled if hasattr(self, "subtitle_enabled") else None)!s}, '
                f'pixel_tags={(self.pixel_tags if hasattr(self, "pixel_tags") else None)!s}, '
                f'logo_width={(self.logo_width if hasattr(self, "logo_width") else None)!s}, '
                f'logo_height={(self.logo_height if hasattr(self, "logo_height") else None)!s}, '
                f'dynamic_watermark={(self.dynamic_watermark if hasattr(self, "dynamic_watermark") else None)!s}, '
                f'watermark_font_size={(self.watermark_font_size if hasattr(self, "watermark_font_size") else None)!s}, '
                f'watermark_font_color={(self.watermark_font_color if hasattr(self, "watermark_font_color") else None)!s}, '
                f'watermark_bg_color={(self.watermark_bg_color if hasattr(self, "watermark_bg_color") else None)!s}, '
                f'watermark_interval={(self.watermark_interval if hasattr(self, "watermark_interval") else None)!s})')
