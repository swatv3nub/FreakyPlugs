from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`User ID Is Required")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Something Went Wrong", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@Freaky.on(Freaky_on_cmd(pattern="gban ?(.*)"))
async def gspider(FreakyUserbot):
    lol = FreakyUserbot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        Freaky = await lol.reply("Gbanning This User !")
    else:
        Freaky = await lol.edit("Wait Processing.....")
    me = await FreakyUserbot.client.get_me()
    await Freaky.edit(f"Global Banning!")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await FreakyUserbot.get_chat()
    a = b = 0
    if FreakyUserbot.is_private:
        user = FreakyUserbot.chat
        reason = FreakyUserbot.pattern_match.group(1)
    else:
        FreakyUserbot.chat.title
    try:
        user, reason = await get_full_user(FreakyUserbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await Freaky.edit(f"**Something W3NT Wrong 🤔**")
    if user:
        if user.id == 1228116248 or user.id == 1167145475:
            return await Freaky.edit(
                f"**Didn't , Your Father Teach You ? That You Cant Gban Dev**"
            )
        try:
            from FreakyUserbot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await FreakyUserbot.client(BlockRequest(user))
        except:
            pass
        testFreakyUserbot = [
            d.entity.id
            for d in await FreakyUserbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testFreakyUserbot:
            try:
                await FreakyUserbot.client.edit_permissions(
                    i, user, view_messages=False
                )
                a += 1
                await Freaky.edit(f"**GBANNED // Total Affected Chats **: `{a}`")
            except:
                b += 1
    else:
        await Freaky.edit(f"**Reply to a user !!**")
    try:
        if gmute(user.id) is False:
            return await Freaky.edit(f"**Error! User probably already gbanned.**")
    except:
        pass
    return await Freaky.edit(
        f"**Freaky Gbanned [{user.first_name}](tg://user?id={user.id}) And Added To GbanWatch In The Chats Where I am Admin : {a} **"
    )


@Freaky.on(Freaky_on_cmd(pattern="ungban ?(.*)"))
async def gspider(FreakyUserbot):
    lol = FreakyUserbot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        Freaky = await lol.reply("`Wait Let Me Process`")
    else:
        Freaky = await lol.edit("One Min ! ")
    me = await FreakyUserbot.client.get_me()
    await Freaky.edit(f"Trying To Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await FreakyUserbot.get_chat()
    a = b = 0
    if FreakyUserbot.is_private:
        user = FreakyUserbot.chat
        reason = FreakyUserbot.pattern_match.group(1)
    else:
        FreakyUserbot.chat.title
    try:
        user, reason = await get_full_user(FreakyUserbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await Freaky.edit("Someting Went Wrong 🤔")
    if user:
        if user.id == 1228116248 or user.id == 1167145475:
            return await Freaky.edit(
                "**A Dev is Never Gbanned // Why Trying To Ungban !**"
            )
        try:
            from FreakyUserbot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await FreakyUserbot.client(UnblockRequest(user))
        except:
            pass
        testFreakyUserbot = [
            d.entity.id
            for d in await FreakyUserbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testFreakyUserbot:
            try:
                await FreakyUserbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await Freaky.edit(f"**UNGBANNING // AFFECTED CHATS - {a} **")
            except:
                b += 1
    else:
        await Freaky.edit("**Reply to a user !!**")
    try:
        if ungmute(user.id) is False:
            return await Freaky.edit("**Error! User probably already ungbanned.**")
    except:
        pass
    return await Freaky.edit(
        f"**UNGBANNED // USER - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )


@Freaky.on(ChatAction)
async def handler(rkG):
    if rkG.user_joined or rkG.user_added:
        try:
            from FreakyUserbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await rkG.get_user()
            gmuted = is_gmuted(guser.id)
        except:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await rkG.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                rkG.chat_id, guser.id, view_messages=False
                            )
                            await rkG.reply(
                                f"**Gbanned User Joined!!** \n"
                                f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Action **  : `Banned`"
                            )
                        except:
                            rkG.reply("`No Permission To Ban`")
                            return


CMD_HELP.update(
    {
        "gban_gmute": "**Gban_Gmute**\
\n\n**Syntax : **`.gban <reply to a user / mention their ID>`\
\n**Usage :** bans the user in every group where you are admin.\
\n\n**Syntax : **`.ungban <reply to a user / mention their ID>`\
\n**Usage :** unbans the user in every group where you are admin."
    }
)
