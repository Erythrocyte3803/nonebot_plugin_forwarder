from nonebot import on_message, logger
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot
from nonebot.rule import startswith
from nonebot.typing import T_State
from nonebot.params import State
from nonebot.plugin import on_command
from nonebot.adapters.cqhttp import Bot, MessageSegment
from nonebot_plugin_guild_patch import GuildMessageEvent
import asyncio

from .config import forwarder_explict, forwarder_prefix, forwarder_source_group, forwarder_source_guild, forwarder_dest_group, forwarder_dest_guild, forwarder_dest_guild_channels, guild_name, guild_link, cids, cnames, group_name

rule = startswith(forwarder_prefix)
msg_matcher = on_message(rule, priority=10, block=False)


async def send_meg(bot: Bot, group_id: str, msg: str):
    await bot.send_group_msg(group_id=group_id, message=msg, auto_escape=False)

async def send_ch(bot: Bot, guild_id: str, channel_id: str, msg: str):
    await bot.send_guild_channel_msg(guild_id=guild_id, channel_id=channel_id, message=msg, auto_escape=False)

@msg_matcher.handle()
async def _(bot: Bot, event: GroupMessageEvent, state: T_State = State()):
    if str(event.group_id) in forwarder_source_group:
        if forwarder_explict:
            flag = forwarder_explict[0] == "" or str(event.user_id) in forwarder_explict
        else:
            flag = True
        if flag:
            # logger.debug("准备转发")
            if forwarder_dest_group[0] == str(event.group_id):
                msg = event.message
                group = str(event.group_id)
                nickname = event.sender.nickname
                msgformat = '[' + group_name[0] + ']' + nickname + ' >>> ' + msg + ' (群号: ' + group + ')'
                tasks = [send_meg(bot, forwarder_dest_group[1], msgformat)]
                tasks1 = [send_ch(bot, forwarder_dest_guild[0], cid, msgformat) for cid in forwarder_dest_guild_channels]
                await asyncio.wait(tasks)
                await asyncio.wait(tasks1)
            if forwarder_dest_group[1] == str(event.group_id):
                msg = event.message
                group = str(event.group_id)
                nickname = event.sender.nickname
                msgformat = '[' + group_name[1] + ']' + nickname + ' >>> ' + msg + ' (群号: ' + group + ')'
                tasks = [send_meg(bot, forwarder_dest_group[0], msgformat)]
                tasks1 = [send_ch(bot, forwarder_dest_guild[0], cid, msgformat) for cid in forwarder_dest_guild_channels]
                await asyncio.wait(tasks)
                await asyncio.wait(tasks1)
@msg_matcher.handle()
async def _(bot: Bot, event: GuildMessageEvent, state: T_State = State()):
    if str(event.guild_id) in forwarder_source_guild:
        if forwarder_explict:
            flag = forwarder_explict[0] == "" or str(event.user_id) in forwarder_explict
        else:
            flag = True
        if flag:
            # logger.debug("准备转发")
            if forwarder_dest_guild[0] == str(event.guild_id):
                msg = event.message
                guild = str(event.guild_id)
                channel = str(event.channel_id)
                nickname = event.sender.nickname
                gname = guild_name[0]
                glink = guild_link[0]
                if channel in cids:
                    cindex = cids.index(channel)
                    chname = cnames[cindex]
                    msgformat = '[' + gname +']['+ chname + ']' + nickname + ' >>> ' + msg + ' (加入频道: '+ glink + ')'
                else:    
                    msgformat = '[' + gname + ']' + nickname + ' >>> ' + msg + ' (加入频道: '+ glink + ')'
                tasks = [send_meg(bot, groups, msgformat) for groups in forwarder_dest_group]
                await asyncio.wait(tasks)