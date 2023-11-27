from typing import Any, List, Dict, Tuple

from app.core.config import settings
from app.log import logger
from app.plugins import _PluginBase


class ConfigCenter(_PluginBase):
    # 插件名称
    plugin_name = "配置中心"
    # 插件描述
    plugin_desc = "快速调整部分系统设定。"
    # 插件图标
    plugin_icon = "setting.png"
    # 主题色
    plugin_color = "#FC6220"
    # 插件版本
    plugin_version = "1.1"
    # 插件作者
    plugin_author = "jxxghp"
    # 作者主页
    author_url = "https://github.com/jxxghp"
    # 插件配置项ID前缀
    plugin_config_prefix = "configcenter_"
    # 加载顺序
    plugin_order = 0
    # 可使用的用户级别
    auth_level = 1

    # 私有属性
    _enabled = False
    settings_attributes = [
        "GITHUB_TOKEN", "API_TOKEN", "TMDB_API_DOMAIN", "TMDB_IMAGE_DOMAIN", "WALLPAPER",
        "RECOGNIZE_SOURCE", "SCRAP_METADATA", "SCRAP_FOLLOW_TMDB", "LIBRARY_PATH",
        "LIBRARY_MOVIE_NAME", "LIBRARY_TV_NAME", "LIBRARY_ANIME_NAME", "LIBRARY_CATEGORY",
        "TRANSFER_TYPE", "OVERWRITE_MODE", "COOKIECLOUD_HOST", "COOKIECLOUD_KEY",
        "COOKIECLOUD_PASSWORD", "COOKIECLOUD_INTERVAL", "USER_AGENT", "SUBSCRIBE_MODE",
        "SUBSCRIBE_RSS_INTERVAL", "SUBSCRIBE_SEARCH", "AUTO_DOWNLOAD_USER", "OCR_HOST",
        "DOWNLOAD_PATH", "DOWNLOAD_MOVIE_PATH", "DOWNLOAD_TV_PATH",
        "DOWNLOAD_ANIME_PATH", "DOWNLOAD_CATEGORY", "DOWNLOAD_SUBTITLE", "DOWNLOADER",
        "DOWNLOADER_MONITOR", "TORRENT_TAG", "MEDIASERVER_SYNC_INTERVAL",
        "MEDIASERVER_SYNC_BLACKLIST", "PLUGIN_MARKET", "MOVIE_RENAME_FORMAT",
        "TV_RENAME_FORMAT"
    ]

    def init_plugin(self, config: dict = None):
        if config:
            self._enabled = config.get("enabled")
            if self._enabled:
                logger.info(f"正在应用配置中心配置：{config}")
                for attribute in self.settings_attributes:
                    setattr(settings, attribute, config.get(attribute) or getattr(settings, attribute))
                messagers = config.get("MESSAGER") or []
                if messagers:
                    settings.MESSAGER = ",".join(messagers)
                media_servers = config.get("MEDIASERVER") or []
                if media_servers:
                    settings.MEDIASERVER = ",".join(media_servers)

    def get_state(self) -> bool:
        return self._enabled

    @staticmethod
    def get_command() -> List[Dict[str, Any]]:
        pass

    def get_api(self) -> List[Dict[str, Any]]:
        pass

    def get_form(self) -> Tuple[List[dict], Dict[str, Any]]:
        """
        拼装插件配置页面，需要返回两块数据：1、页面配置；2、数据结构
        """
        default_settings = {
            "enabled": False,
        }
        for attribute in self.settings_attributes:
            default_settings[attribute] = getattr(settings, attribute)
        default_settings["MESSAGER"] = settings.MESSAGER.split(",")
        default_settings["MEDIASERVER"] = settings.MEDIASERVER.split(",")
        return [
            {
                "component": "VForm",
                "content": [
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "enabled",
                                            "label": "启用插件"
                                        }
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "GITHUB_TOKEN",
                                            "label": "Github Token"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "API_TOKEN",
                                            "label": "API密钥"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "TMDB_API_DOMAIN",
                                            "label": "TMDB API地址"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "TMDB_IMAGE_DOMAIN",
                                            "label": "TheMovieDb图片服务器"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "RECOGNIZE_SOURCE",
                                            "label": "媒体信息识别来源",
                                            "items": [
                                                {"title": "TheMovieDb", "value": "themoviedb"},
                                                {"title": "豆瓣", "value": "douban"}
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "SCRAP_SOURCE",
                                            "label": "刮削元数据及图片使用的数据源",
                                            "items": [
                                                {"title": "TheMovieDb", "value": "themoviedb"},
                                                {"title": "豆瓣", "value": "douban"},
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "WALLPAPER",
                                            "label": "登录首页电影海报",
                                            "items": [
                                                {"title": "TheMovieDb电影海报", "value": "tmdb"},
                                                {"title": "Bing每日壁纸", "value": "bing"}
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "LIBRARY_CATEGORY",
                                            "label": "开启媒体库二级分类"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "SCRAP_METADATA",
                                            "label": "刮削入库的媒体文件"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "LIBRARY_PATH",
                                            "label": "媒体库目录"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "LIBRARY_MOVIE_NAME",
                                            "label": "电影目录名称"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "LIBRARY_TV_NAME",
                                            "label": "电视剧目录名称"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "LIBRARY_ANIME_NAME",
                                            "label": "动漫目录名称"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "TRANSFER_TYPE",
                                            "label": "整理转移方式",
                                            "items": [
                                                {"title": "硬链接", "value": "link"},
                                                {"title": "复制", "value": "copy"},
                                                {"title": "移动", "value": "move"},
                                                {"title": "软链接", "value": "softlink"},
                                                {"title": "rclone复制", "value": "rclone_copy"},
                                                {"title": "rclone移动", "value": "rclone_move"}
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "OVERWRITE_MODE",
                                            "label": "转移覆盖模式",
                                            "items": [
                                                {"title": "从不覆盖", "value": "never"},
                                                {"title": "按大小覆盖", "value": "size"},
                                                {"title": "总是覆盖", "value": "always"},
                                                {"title": "仅保留最新版本", "value": "latest"}
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "SCRAP_FOLLOW_TMDB",
                                            "label": "新增入库跟随TMDB信息变化"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "COOKIECLOUD_HOST",
                                            "label": "CookieCloud服务器地址"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "COOKIECLOUD_KEY",
                                            "label": "CookieCloud用户KEY"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "COOKIECLOUD_PASSWORD",
                                            "label": "CookieCloud端对端加密密码"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "COOKIECLOUD_INTERVAL",
                                            "label": "CookieCloud同步间隔（分钟）"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "USER_AGENT",
                                            "label": "CookieCloud浏览器UA"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "SUBSCRIBE_MODE",
                                            "label": "订阅模式",
                                            "items": [
                                                {"title": "站点RSS", "value": "rss"},
                                                {"title": "自动", "value": "spider"}
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "SUBSCRIBE_RSS_INTERVAL",
                                            "label": "RSS订阅刷新间隔（分钟）"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "SUBSCRIBE_SEARCH",
                                            "label": "开启订阅定时搜索"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "MESSAGER",
                                            "label": "消息通知渠道",
                                            'chips': True,
                                            'multiple': True,
                                            "items": [
                                                {"title": "Telegram", "value": "telegram"},
                                                {"title": "微信", "value": "wechat"},
                                                {"title": "Slack", "value": "slack"},
                                                {"title": "SynologyChat", "value": "synologychat"}
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "AUTO_DOWNLOAD_USER",
                                            "label": "自动择优下载用户列表"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "OCR_HOST",
                                            "label": "验证码识别服务器"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "DOWNLOAD_PATH",
                                            "label": "下载保存目录"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "DOWNLOAD_MOVIE_PATH",
                                            "label": "电影下载保存目录"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "DOWNLOAD_TV_PATH",
                                            "label": "电视剧下载保存目录"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "DOWNLOAD_ANIME_PATH",
                                            "label": "动漫下载保存目录"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "DOWNLOADER_MONITOR",
                                            "label": "开启下载器监控"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "DOWNLOAD_CATEGORY",
                                            "label": "开启下载二级分类"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "DOWNLOADER",
                                            "label": "下载器",
                                            "items": [
                                                {"title": "Qbittorrent", "value": "qbittorrent"},
                                                {"title": "Transmission", "value": "transmission"}
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "TORRENT_TAG",
                                            "label": "下载器种子标签"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "DOWNLOAD_SUBTITLE",
                                            "label": "自动下载站点字幕"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSelect",
                                        "props": {
                                            "model": "MEDIASERVER",
                                            "label": "媒体服务器",
                                            'chips': True,
                                            'multiple': True,
                                            "items": [
                                                {"title": "Emby", "value": "emby"},
                                                {"title": "Jellyfin", "value": "jellyfin"},
                                                {"title": "Plex", "value": "plex"}
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "MEDIASERVER_SYNC_INTERVAL",
                                            "label": "媒体服务器同步间隔（小时）"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "MEDIASERVER_SYNC_BLACKLIST",
                                            "label": "媒体服务器同步黑名单"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                },
                                "content": [
                                    {
                                        "component": "VTextarea",
                                        "props": {
                                            "model": "MOVIE_RENAME_FORMAT",
                                            "label": "电影重命名格式"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                },
                                "content": [
                                    {
                                        "component": "VTextarea",
                                        "props": {
                                            "model": "TV_RENAME_FORMAT",
                                            "label": "电视剧重命名格式"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                },
                                "content": [
                                    {
                                        "component": "VTextarea",
                                        "props": {
                                            "model": "PLUGIN_MARKET",
                                            "label": "插件市场",
                                            "placeholder": "多个地址使用,分隔"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                'component': 'VCol',
                                'props': {
                                    'cols': 12,
                                },
                                'content': [
                                    {
                                        'component': 'VAlert',
                                        'props': {
                                            'type': 'info',
                                            'variant': 'tonal',
                                            'text': '注意：本插件只是运行时临时修改生效系统配置，并不会实际改变环境变量或app.env中的配置值。'
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ], default_settings

    def get_page(self) -> List[dict]:
        pass

    def stop_service(self):
        """
        退出插件
        """
        pass
