from nonebot import get_driver, logger

config = get_driver().config
#=====================群聊设置======================
#源群
if not hasattr(config, "forwarder_source_group"):
    forwarder_source_group = ""
    logger.info("未检测到forwarder_source_group配置")
else:
    forwarder_source_group = config.forwarder_source_group
#目标群
if not hasattr(config, "forwarder_dest_group"):
    forwarder_dest_group = [""]
    logger.info("未检测到forwarder_dest_group配置")
else:
    forwarder_dest_group = config.forwarder_dest_group
#群名
if not hasattr(config, "group_name"):
    group_name = ["一群","二群"]
    logger.info("未检测到group_name配置")
else:
    group_name = config.group_name
#===================================================
#=====================频道设置======================
#源频道
if not hasattr(config, "forwarder_source_guild"):
    forwarder_source_guild = ""
    logger.info("未检测到forwarder_source_guild配置")
else:
    forwarder_source_guild = config.forwarder_source_guild
#目标频道
if not hasattr(config, "forwarder_dest_guild"):
    forwarder_dest_guild = [""]
    logger.info("未检测到forwarder_dest_guild配置")
else:
    forwarder_dest_guild = config.forwarder_dest_guild
#目标子频道
if not hasattr(config, "forwarder_dest_guild_channels"):
    forwarder_dest_guild_channels = [""]
    logger.info("未检测到forwarder_dest_guild_channels配置")
else:
    forwarder_dest_guild_channels = config.forwarder_dest_guild_channels
#频道名
if not hasattr(config, "guild_name"):
    guild_name = ["频道"]
    logger.info("未检测到guild_name配置")
else:
    guild_name = config.guild_name
#频道链接
if not hasattr(config, "guild_link"):
    guild_link = ["请设置链接"]
    logger.info("未检测到guild_link配置")
else:
    guild_link = config.guild_link
#要关联的子频道ID
if not hasattr(config, "cids"):
    cids = [""]
    logger.info("未检测到cids配置")
else:
    cids = config.cids
#要关联的子频道名
if not hasattr(config, "cnames"):
    cnames = [""]
    logger.info("未检测到cnames配置")
else:
    cnames = config.cnames
#=================================================== 
#=====================其它设置======================
#前缀   
if not hasattr(config, "forwarder_prefix"):
    forwarder_prefix = [""]
    logger.info("未检测到forwarder_prefix配置，默认为 ''")
else:
    forwarder_prefix = config.forwarder_prefix
#过滤器
if not hasattr(config, "forwarder_explict"):
    forwarder_explict = [""]
    logger.info("未检测到forwarder_explict配置，默认为['']")
else:
    forwarder_explict = config.forwarder_explict
#=================================================== 