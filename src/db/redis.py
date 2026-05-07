# import aioredis
# 新版本的redis已经内置了异步支持 aioredis.StrictRedis->redis.asyncio.Redis

import redis.asyncio as aioredis
from src.config import Config

JTI_EXPIRY = 3600

# token_blocklist = aioredis.Redis(
#     host=Config.REDIS_HOST,
#     port=Config.REDIS_PORT,
#     db=Config.REDIS_DB,
#     decode_responses=True,
# )

token_blocklist = aioredis.Redis.from_url(Config.REDIS_URL)



async def add_jti_to_blocklist(jti: str)->None:
    await token_blocklist.set(
        name=jti,
        value="",
        ex=JTI_EXPIRY,
    )

async def token_in_blocklist(jti: str)->bool:
    jti_res = await token_blocklist.get(jti)
    return jti_res is not None
