api_id = 00000000 #ВНЕСИ МЕНЯ
api_hash = 'хххххххххххх' #ВНЕСИ МЕНЯ

from telethon import TelegramClient, events, utils, connection
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
import re

client = TelegramClient('USERNAME.session', api_id, api_hash, proxy=('proxy.digitalresistance.dog', 443, 'd41d8cd98f00b204e9800998ecf8427e'), connection=connection.ConnectionTcpMTProxyRandomizedIntermediate).start()

global Target
@client.on(events.MessageEdited)
async def handler_edit(event):
    global Target
    if (utils.get_display_name(await event.get_sender()) == 'Bastion Siege v2') and (re.search(r'Цель:', event.message.message)):
        try: EnemyAlliance = re.search(r'\[(.*)\]', event.message.message).group(1)
        except: EnemyAlliance = ''
        if (Target != '') and (Target != EnemyAlliance):
            await client(GetBotCallbackAnswerRequest(764095451, event.id, data=event.reply_markup.rows[0].buttons[0].data))   
@client.on(events.NewMessage)
async def handler(event):
    global Target
    if (event.from_id == event.to_id.user_id) and (re.search(r'^/find', event.message.message.lower())):
        try: Target = re.search(r'\/find (.*)', event.message.message).group(1)
        except: Target = ''

try: client.run_until_disconnected()
finally: client.disconnect()