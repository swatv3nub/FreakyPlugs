"""Emoji
Available Commands:
.support
Support Channel/Group
"""


import asyncio

from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd("support"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("For The Support//Or Anything")
    animation_chars = [
        "Click here",
        "[For The Whole Things](https://t.me/FreakyUserbot)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
