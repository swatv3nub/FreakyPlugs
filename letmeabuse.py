"""command: .abusehin , .abusemal"""

#!/usr/bin/env python3
# SpEcHiDe <<I GUESS>>
# -*- coding: utf-8 -*-

import random

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd(pattern=r"habuse(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "hin":
        emoticons = [
            "Maderchod- MOTHERFUCKER",
            "Bhosadike-BORN FROM A ROTTEN PUSSY",
            "Bhen chod-Sister fucker",
            "Bhadhava- Pimp",
            "Chodu- Fucker",
            "Chutiya- Fucker, bastard",
            "Gaand- ASS",
            "Gaandu-Asshole",
            "Gadha, Bakland- Idiot",
            "Lauda, Lund- Penis, dick, cock",
            "Hijra- Gay, Transsexual",
            "Kuttiya- Bitch",
            "Paad- FART",
            "Randi- HOOKER",
            "Saala kutta- Bloody dog",
            "Saali kutti- Bloody bitch",
            "Tatti- Shit",
            "Kamina- bastard",
            "Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
            "Chut ke dhakkan- Pussy lid",
            "Chut ke gulam- Pussy whipped",
            "Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
            "Choot marani ka- Pussy whipped",
            "Choot ka baal- Hair of vagina",
            "Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
            "Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
            "Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
            "Chipkali ke chut ke pasine- Sweat of reptiles cunt",
            "Chipkali ki bhigi chut- Wet pussy of a wall lizard",
            "Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
            "Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
            "Cuntmama- Vaginal uncle",
            "Chhed- Vagina,Hole",
            "Apni gaand mein muthi daal- Put your fist up your ass",
            "Apni lund choos- Go and suck your own dick",
            "Apni ma ko ja choos- Go suck your mom",
            "Bhen ke laude- Sister’s dick",
            "Bhen ke takke: Go and suck your sister’s balls",
            "Abla naari tera buble bhaari-  woman, your tits are huge",
            "Bhonsdi-Waalaa- You fucker",
            "Bhadwe ka awlat- Son of a pimp",
            "Bhains ki aulad- Son of a buffalo",
            "Buddha Khoosat- Old fart",
            "Bol teri gand kaise maru- let me know how to fuck you in the ass",
            "Bur ki chatani- Ketchup of cunt",
            "Chunni- Clit",
            "Chinaal- Whore",
            "Chudai khana- Whore house",
            "Chudan chuda- Fucking games",
            "Chut ka pujari- pussy worshipper",
            "Chut ka bhoot- Vaginal Ghost",
            "Gaand ka makhan- Butter from the ass",
            "Gaand main lassan- Garlic in ass",
            "Gaand main danda- Stick in ass",
            "Gaand main keera- Bug up your ass",
            "Gaand mein bambu- A bambooup your ass",
            "Gaandfat- Busted ass",
            "Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
            "Hazaar lund teri gaand main-Thousand dicks in your ass",
            "Jhat ke baal- Pubic hair",
            "Jhaant ke pissu- Bug of pubic hair",
            "Kadak Mall- Sexy Girl",
            "Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
            "Khotey ki aulda- Son of donkey",
            "Kutte ka awlat- Son of a dog",
            "Kutte ki jat- Breed of dog",
            "Kutte ke tatte- Dog’s balls",
            "Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
            "Lavde ke bal- Hair on your penis",
            "muh mei lele: Suck my dick",
            "Lund Chus: Suck dick",
            "Lund Ke Pasine- Sweat of dick",
            "Meri Gand Ka Khatmal: Bug of my Ass",
            "Moot, Mootna- Piss off",
            "Najayaz paidaish- Illegitimately born",
            "Randi khana- whore house",
            "Sadi hui gaand- Stinking ass",
            "Teri gaand main kute ka lund- A dog’s dick in your ass",
            "Teri maa ka bhosda- Your mother’s breasts",
            "Teri maa ki chut- Your mother’s pussy",
            "Tere gaand mein keede paday- May worms infest your ass-hole",
            "Ullu ke pathe- Idiot",
        ]
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀ Ĺ̯▀   )",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)


CMD_HELP.update(
    {
        "letmeabuse": "**LetMeAbuse**\
\n\n**Syntax : **`.habuse`\
\n**Usage :** Abuses Your Enemy."
    }
)
