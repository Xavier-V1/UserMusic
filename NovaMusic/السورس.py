import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import HNDLR, SUDO_USERS

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 بـنـك/b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⏳ شغال</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    jmthon = await m.reply("1")
    await jmthon.edit("2")
    await jmthon.edit("3")
    await jmthon.edit("4")
    await jmthon.edit("5")
    await jmthon.edit("6")
    await jmthon.edit("7")
    await jmthon.edit("8")
    await jmthon.edit("9")
    await jmthon.edit("**تم اعادة تشغيل سورس نوفـا ميوزك بنجاح ✓**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HEPZ = f"""
- هيي ي قلب  {m.from_user.mention} 🌿💕
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
قائمـة اوامر سـورس نـوفـا مـيـوزك. 🌿💕
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
- أوامر المستخدمين: 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​✫
• {HNDLR}شغل
 اسم الاغنيه | رابط يوتيوب | الرد على ملف مقطع صوتي ​​​​•
 - لتشغيل مقطع صوتي في المكالمه
                                     ​​​​​​​​​​​​​✫
• {HNDLR}فيديو
 عنوان الفيديو | رابط يوتيوب | الرد على الفيديو ​​​​•
 - لتشغيل فيديو في المكالمة
                                     ​​​​​​​​​​​✫
• {HNDLR}القائمة
  - لعرض قائمة التشغيل الحالية
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}بنك
 - لعرض سرعه النت للبوت
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}الاوامر
 - لعرض اوامر سورس ميوزك نوفـا
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
- أوامر المشرفين  : 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}كمل
 - لمواصلة تشغيل المقطع الصوتي أو الفيديو المتوقف
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}وقف
 - لإيقاف تشغيل المقطع الصوتي أو مقطع فيديو مؤقتًا
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}تخطي
 - لتخطي المقطع الصوتي أو الفيديو الحالي وتشغيل ما بعده
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}انهاء
 - لإنهاء التشغيل
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
By : @K_P_S_6
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
"""
    await m.reply(HEPZ)


@Client.on_message(filters.command(["السورس","الريبو","سورس"], prefixes=f"{HNDLR}"))
async def repo(client, martin: Message):
    await martin.delete()    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("# 𝙏𝙀𝘼𝙈 𝙉𝙊𝙑𝘼", url=f"https://t.me/O_A_V"),
                InlineKeyboardButton("# 𝙎𝙊𝙐𝙍𝘾𝙀", url=f"https://t.me/K_P_S_6"),
            ]
        ]
    )

    REPZ = f"""
- هيي ي قلب  {m.from_user.mention} 🌿💕
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
🎶 سورس نوفـا ميوزك
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
لـتشغيل الاغاني في المحادثات الصوتيه
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
                                   [لــنـكك تــنصـيب سورس نـوفـا مــيـوزك 🌿💕](https://heroku.com/deploy?template=https://github.com/Xavier-V1/UserMusic)
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​✫                                                                      ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​
⚒️ لعرض اوامر السورس ارسل  {HNDLR}الاوامر
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
📚 • قناة نوفـا  : @K_P_S_6
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫                                   
"""
    await martin.reply_photo(
        photo=f"https://telegra.ph/file/ad4ede69d64e5640abd7d.jpg",
        caption=REPZ,
        reply_markup=keyboard,
    )