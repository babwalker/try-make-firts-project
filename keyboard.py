from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

back = KeyboardButton("Back")
inline_btn_1 = InlineKeyboardButton('Подобрать оффер', callback_data="0")
inline_btn_2 = InlineKeyboardButton('Связаться с менеджером', callback_data="1", url="https://t.me/fertilizer4")
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)
tier1_kb = KeyboardButton("Tier 1")
tier2_kb = KeyboardButton("Tier 2")
tier3_kb = KeyboardButton("Tier 3")
all_countries = KeyboardButton("All countires")
tier = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    tier1_kb, tier2_kb, tier3_kb
).insert(all_countries).add(back)
offer1 = KeyboardButton("Gambling")
offer2 = KeyboardButton("Betting")
offer3 = KeyboardButton("Binary")
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    offer1, offer2, offer3
).add(back)