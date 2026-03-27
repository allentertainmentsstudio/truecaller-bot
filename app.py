from truecallerpy import search_phonenumber
from pyrogram import Client, filters, enums, errors
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database import add_user, add_group, all_users, all_groups, users, remove_user
import asyncio, random
from configs import cfg

bot = Client(
    "trucaller",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)
OWNER_ID = cfg.SUDO
CHID = cfg.CHID
LOG_ID = cfg.LOGCHID
cc = cfg.API

async def numchk(n: str, x):
    try:
        if len(n) == 12:
            if n.startswith("+91"):
                number = n[3:]
            else:
                number = "Invalid Number"
        elif len(n) == 10:
            if n.startswith("0"):
                number = n[1:]
            else:
                number = "Invalid Number"    
        elif len(n) == 9:
            number = n
        else:
            number = "Invalid Number"
    except Exception as e:
        number = "Invalid Number"
        await bot.send_message(LOG_ID,f"**Error**\n\n`{e}`")
    return await getinfo(number, x)

#______________________________________________________________

sendtxt = """
<b><u>👾 Founded Information's ✓✓</u></b>

<b>»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»</b>

<b>💁‍♂️┎╼ Name :-</b> <code>{}</code>

<b>📞 ├╼ Number :- </b> <code>{}</code>

<b>👁‍🗨 ├╼ Number Type :-</b> <code>{}</code>

<b>📮 ├╼ Countrycode :-</b> <code>{}</code>

<b>📶 ├╼ ISP :-</b> <code>{}</code>

<b>⏳┖╼ TimeZone :-</b> <code>{}</code>

<b>Social Accounts ⤸⤸</b>
<b><i>☘️ Telegram Link :-</i> <a href="https://t.me/Anujedits76">Click Here</a></b>
<b><i>☘️ Whatsapp Link :-</i> <a href="https://wa.me/qr/KIMMGWH7GUEYO1">Click Here</a></b>

<b>»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»</b>

<b><spoiler>🔥 Powered By @anujedits76 ©️| @phone_number_info_ak_bot 🤖</spoiler></b>

"""

async def getinfo(num : int,x):
    try:
        if num == "Invalid Number":
            await x.edit_text("**🫠 Invalid number!**")
        else:
            lel = int(num)
            try:
                r = search_phonenumber(str(lel), 'LK' ,cc )
                await x.edit_text(sendtxt.format(r['data'][0]['name'],r['data'][0]['phones'][0]['nationalFormat'],r['data'][0]['phones'][0]['numberType'],r['data'][0]['phones'][0]['countryCode'],r['data'][0]['phones'][0]['carrier'],r['data'][0]['addresses'][0]['timeZone'],f"t.me/{r['data'][0]['phones'][0]['e164Format']}",f"wa.me/{r['data'][0]['phones'][0]['e164Format']}"),disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)
            except Exception as e:
                await x.edit_text("**🤷‍♂️ Not in Truecaller Database. 🤷‍♂️**")
                await bot.send_message(LOG_ID,f"**#Error**\n\n`{e}`")
                print(e)
    except Exception as e:
        await x.edit_text("**🫠 Invalid number!**")
        await bot.send_message(LOG_ID,f"**#Error**\n\n`{e}`")

@bot.on_message(filters.command("start"))
async def stsrt(_, m : Message):
    try:
        await bot.get_chat_member(CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Update Channel", url="https://t.me/log_channel_a"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/log_channel_a")
                    ]
                ]
            )
            k = add_user(m.from_user.id)
            if k == "444":
                print('lol')
            else:
                await bot.send_message(LOG_ID, m.from_user.first_name +" Is started Your Bot!")
            await m.reply_photo(photo='https://telegra.ph/file/2f61421c348c1ec42fde7.jpg',caption=
f"""**
👋 Hello {m.from_user.mention}!

I'm Simple Unknown call information gather bot. 
you can check any India 🇮🇳 mobile number informations from me.

Features:- ⚕⚕
    💫 Find unknown numbers owner name and other details.
    📮 Get Social Account links.
    🎯 24/7 hours active.
    ☘️ Hosted on Heroku.
    
👾 To see how it works just send /help command.

🎡 Other Countries will add soon.

||🔥 Powered By @anujedits76 ©️ | @phone_number_info_ak_bot 🤖||**""", reply_markup=keyboard)
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/phone_number_info_ak_bot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\nstart me private to use me.**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**🚧Access Denied!🚧\n\nPlease Join @{} to use me.If you joined click check again button to confirm.**".format("log_channel_a"), reply_markup=key)
    except Exception as e:
        print(e)

@bot.on_message(filters.text &filters.private & ~filters.command(['start','help', 'users', 'fcast', 'bcast']))
async def main(_, m : Message):
    text = m.text.replace(" ", "")
    x = await m.reply_text("**__⚡️ processing...**__")
    await numchk(text, x)

@bot.on_message(filters.command("help"))
async def help(_, m : Message):
    await m.reply_text("**⚠️Currently Available only for Sri Lankan Numbers.⚠️\nJust send target phone number to lookup informations.\n\n✅Available formats:-\n - +9171⚹⚹⚹⚹⚹⚹⚹\n - 071⚹⚹⚹⚹⚹⚹⚹\n - 71⚹⚹⚹⚹⚹⚹⚹\n\n🍂 Ex:- `+919719168804`\n\n💁‍♂️ If you Need help please send message to __@anujedits76.__\n\n||🔥 Powered By @anujedits76 ©️ | @phone_number_info_ak_bot 🤖||**")

@bot.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await bot.get_chat_member(CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Update Channel", url="https://t.me/Taprobane_Lk"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/TaprobaneChat")
                    ]
                ]
            )
            c = add_user(cb.from_user.id)
            await cb.message.edit(
f"""**
👋 Hello {cb.from_user.mention}!

I'm Simple Unknown call information gather bot. 
you can check any India 🇮🇳 mobile number informations from me.

🧜 Features:-
    💫 Find unknown numbers owner name and other details.
    👾 Get Social Account links.
    🎯 24/7 hours active.
    📦 Hosted on Heroku.
    
🪩To see how it works just send /help command.

🎡 Other Countries will add soon.

||🔥 Powered By @anujedits76 ©️ | @phone_number_info_ak_bot 🤖||**""", reply_markup=keyboard) 
              
        if c == "444":
                print('lol')
        else:
            await bot.send_message(LOG_ID, cb.from_user.first_name +" Is started Your Bot!")
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You are not joined to channel join and try again. 🙅‍♂️")
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.on_message(filters.command("users") & filters.user(OWNER_ID))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.on_message(filters.command("bcast") & filters.user(OWNER_ID))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.on_message(filters.command("fcast") & filters.user(OWNER_ID))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now")
bot.run()
