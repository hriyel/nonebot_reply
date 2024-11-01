from logging import config
from nonebot import on_command
from nonebot import on_message
import random

from .config import config

group_whitelist = config.group_whitelist # type: ignore
reply = on_message(priority=1,block=False,)

text = {} #存储当前消息
a=0

def reply (a): #判断是否复读
    a=random.randint(1,6)
    if a == 1:
        if group_id in group_whitelist:
            return True
        else:
            return False

@reply.handle()