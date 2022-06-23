import pyrogram
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram.types import ReplyKeyboardMarkup
import os

app=Client(
    "EpicBots",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

#Buttons & Captions
#-------------BOT LIST Buttons & Mg--------------#
HELP = """Welcome to Help Menu!
Im Epic State Bot ✓ 
Send /listbots & Chek all avibles Epic Bots 
I Will Be Update Evry Morning
"""
#-------------------------------------------------------------
HELP_BTN = [
[InlineKeyboardButton('BACK', callback_data="BACK_MENU")]
]

BOT_LIST_MG = "Chek Bellow & see all team Epic Bots Catogories"
REPLY_BUTTONS = ReplyKeyboardMarkup(
      [
            ["🎧Voice Chat"],
            ["Social"],
            ["Group Manager"],
            ["Tools & Helps"]
           
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
START_MG = """
**🔥 Hello There,  Im Epic Developers Bots State Bot
➤ Click /help Or The Button Below To Know How To Use Me
"""
START_BTN = [
            [
                InlineKeyboardButton('HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton(' SUPPORT', url='https://t.me/EpicChats'),
                InlineKeyboardButton('EPIC DEVELOPERS</>', url='https://t.me/NightVission')
            ],
            [
                InlineKeyboardButton('BOT STATE', callback_data="BOT_CALLBACK")
            ]
        ]
        
#Commands For Epic Bot
@app.on_message(filters.command("start") & filters.private)
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/ba8e2c222f7a4f82dd592.jpg",caption=START_MG,reply_markup=InlineKeyboardMarkup(START_BTN))
  
@app.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_sticker("CAACAgUAAxkBAAEFFdRisHcr0C1_svwE_gAB2PhkruEaZcgAAoUGAAI2X4lVZVPINGURBWcoBA",caption=HELP,reply_markup=InlineKeyboardMarkup(HELP_BTN))
  
@app.on_message(filters.command("listbots"))
async def listbots(bot, message):
  await message.reply_sticker("CAACAgUAAxkBAAEFFdRisHcr0C1_svwE_gAB2PhkruEaZcgAAoUGAAI2X4lVZVPINGURBWcoBA",caption=BOT_LIST_MG,reply_markup=InlineKeyboardMarkup(REPLY_BUTTONS))

#Button Replys
@app.on_message(filters.regex("🎧Voice Chat"))
def reply_to_VoiceChat(bot, message):
  bot.send_message(message.chat.id, "This Is Vc Bots")
  
  
 #Callbacks
@app.on_callback_query(filters.regex("HELP_CALLBACK"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup(HELP_BTN))
  
@app.on_callback_query(filters.regex("BACK_MENU"))
async def back_menu(_,query):
  await query.answer()
  await query.message.edit(START_MG,reply_markup=InlineKeyboardMarkup(START_BTN))
  
@app.on_callback_query(filters.regex("BOT_CALLBACK"))
async def help_menu(_,query):
  await query.answer()
  await query.message.edit(BOT_LIST_MG,reply_markup=ReplyKeyboardMarkup(REPLY_BUTTONS))
  
print("</>EPIC BOTS</>")
app.run()
