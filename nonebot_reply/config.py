from pydantic import BaseModel, Field
from nonebot import get_driver, get_plugin_config

config = get_driver().config.dict()

class Config(BaseModel):
    group_whitelist = config.get('group_whitelist', [])

