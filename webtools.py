# @ProjectHackfreaks // From Friday

import requests
from iplookup import iplookup
from selenium import webdriver
from youtube_search import YoutubeSearch

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd, edit_or_reply, sudo_cmd


@Freaky.on(Freaky_on_cmd(pattern="wshot ?(.*)"))
@Freaky.on(sudo_cmd(pattern="wshot ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    sedlyffreaky = await edit_or_reply(event, "Capturing Webshot, Stay Tuned.")
    driver = webdriver.Chrome()
    driver.get(urlissed)
    driver.get_screenshot_as_file("Webshot-@FreakyUserbot.png")
    imgpath = "Webshot-@FreakyUserbot.png"
    await sedlyffreaky.edit("Completed. Uploading in Telegram..")
    await borg.send_file(
        event.chat_id,
        file=imgpath,
        caption=f"**WEBSHOT OF** `{urlissed}` \n**Powered By @FreakyUserbot**",
    )


@Freaky.on(Freaky_on_cmd(pattern="lp ?(.*)"))
@Freaky.on(sudo_cmd(pattern="lp ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfbro = await edit_or_reply(event, "Wait Fetching Website Info")
        gone = event.pattern_match.group(1)
        url = f"https://api.ip2whois.com/v1?key=free&domain=" + gone
        await event.edit(
            "Fecthing Website Info ! Stay Tuned. This may take some time ;)"
        )
        lol = iplookup.iplookup
        okthen = lol(gone)
        sed = requests.get(url=url).json()
        km = sed["registrant"]
        kek = sed["registrar"]
        sedlyf = (
            f'Domain Name => {sed["domain"]} \nCreated On => {sed["create_date"]} \nDomain ID => {sed["domain_id"]} \nHosted ON => {kek["url"]}'
            f'\nLast updated => {sed["update_date"]} \nExpiry Date => {sed["expire_date"]} \nDomain Age => {sed["domain_age"]}'
            f'\nOwner => {km["name"]} \nCountry => {km["country"]} \nState => {km["region"]}'
            f'\nPhone Number => {km["phone"]} \nDomain Ip => {okthen}'
        )
        await tfbro.edit(sedlyf)
    except Exception:
        await tfbro.edit(f"Something Went Wrong. MayBe Website Wrong.")


@Freaky.on(Freaky_on_cmd(pattern="bin ?(.*)"))
@Freaky.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfsir = await edit_or_reply(event, "Wait Fetching Bin Info")
        kek = event.pattern_match.group(1)
        url = f"https://lookup.binlist.net/{kek}"
        midhunkm = requests.get(url=url).json()
        kekvro = midhunkm["country"]
        data_is = (
            f"<b><u>Bin</u></b> ➠ <code>{kek}</code> \n"
            f"<b><u>Type</u></b> ➠ <code>{midhunkm['type']}</code> \n"
            f"<b><u>Scheme</u></b> ➠ <code>{midhunkm['scheme']}</code> \n"
            f"<b><u>Brand</u></b> ➠ <code>{midhunkm['brand']}</code> \n"
            f"<b><u>Country</u></b> ➠ <code>{kekvro['name']} {kekvro['emoji']}</code> \n"
        )
        await tfsir.edit(data_is, parse_mode="HTML")
    except:
        await tfsir.edit("Not a Valid Bin Or Don't Have Enough Info.")


@Freaky.on(Freaky_on_cmd(pattern="iban ?(.*)"))
@Freaky.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    inputs = event.pattern_match.group(1)
    api = f"https://openiban.com/validate/{inputs}?getBIC=true&validateBankCode=true"
    lol = requests.get(url=api).json()
    try:
        tfhm = await edit_or_reply(event, "Wait Fetching IBAN Info")
        banks = lol["bankData"]
        kek = (
            f"<b><u>VALID</u></b> ➠ <code>{lol['valid']}</code> \n"
            f"<b><u>IBAN</u></b> ➠ <code>{lol['iban']}</code> \n"
            f"<b><u>BANK-CODE</u></b> ➠ <code>{banks['bankCode']}</code> \n"
            f"<b><u>BANK-NAME</u></b> ➠ <code>{banks['name']}</code> \n"
            f"<b><u>ZIP</u></b> ➠ <code>{banks['zip']}</code> \n"
            f"<b><u>CITY</u></b> ➠ <code>{banks['city']}</code> \n"
            f"<b><u>BIC</u></b> ➠ <code>{banks['bic']}</code> \n"
        )
        await tfhm.edit(kek, parse_mode="HTML")
    except:
        await tfhm.edit(f"Invalid IBAN Or Doesn't Have Enough Info")


@Freaky.on(Freaky_on_cmd(pattern="gitdl ?(.*)"))
@Freaky.on(sudo_cmd(pattern="gitdl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        kekman = await edit_or_reply(event, "Fetching Repo")
        inputs = event.pattern_match.group(1)
        sed = event.pattern_match.group(1)
        if sed:
            if " " in sed:
                noobfreaks = inputs.split(" ", 2)
        gitusername = noobfreaks[0]
        gitrepo = noobfreaks[1]
        gitbranch = noobfreaks[2]
        link = f"https://github.com/{gitusername}/{gitrepo}/archive/{gitbranch}.zip"
        await kekman.edit("Uploading... Stay Tuned.")
        await event.delete()
        await borg.send_file(event.chat_id, file=link, caption="You Repo Achieve File.")
    except:
        await borg.send_message(
            event.chat_id, "**Usage** : `.gitdl <gitusername> <gitrepo> <gitbranch>`"
        )


@Freaky.on(Freaky_on_cmd(pattern="yts ?(.*)"))
@Freaky.on(sudo_cmd(pattern="yts ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        fin = event.pattern_match.group(1)
        freaks_result = await edit_or_reply(
            event, "Fectching Result this May Take Time"
        )
        results = YoutubeSearch(f"{fin}", max_results=5).to_dict()
        noob = "<b>YOUTUBE SEARCH</b> \n\n"
        for moon in results:
            hmm = moon["id"]
            kek = f"https://www.youtube.com/watch?v={hmm}"
            freaks_name = moon["title"]
            freaks_chnnl = moon["channel"]
            total_freaks = moon["duration"]
            freaks_views = moon["views"]
            noob += (
                f"<b><u>VIDEO-TITLE</u></b> ➠ <code>{freaks_name}</code> \n"
                f"<b><u>LINK</u></b> ➠ <code>{kek}</code> \n"
                f"<b><u>CHANNEL</u></b> ➠ <code>{freaks_chnnl}</code> \n"
                f"<b><u>DURATION</u></b> ➠ <code>{total_freaks}</code> \n"
                f"<b><u>TOTAL-VIEWS</u></b> ➠ <code>{freaks_views}</code> \n\n"
            )
        await freaks_result.edit(noob, parse_mode="HTML")
    except:
        await event.edit("Some Thing Went Wrong.")


CMD_HELP.update(
    {
        "webtools": "WebTools\
\n\nSyntax : .wshot<link> .ip<address>, .bin<code>, .iban<username>, .gitdl<link>, .yts<link>\
\nUsage : Usefull Plugin For Coders"
    }
)
