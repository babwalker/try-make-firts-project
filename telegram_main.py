from config import *
from keyboard import *


storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)

class ClientStatesGroup(StatesGroup):

    callback_answer = State()
    choose_tier = State()
    countries = State()

@dp.message_handler(commands=["start"])
async def inline_echo(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name} Подберём тебе подходящий оффер?", reply_markup=inline_kb1)
    await ClientStatesGroup.callback_answer.set()

@dp.callback_query_handler(state=ClientStatesGroup.callback_answer)
async def some_callback_handler(query: types.CallbackQuery):
    if query.data == "0":
        await bot.send_message(query.from_user.id, f'Выбирай', reply_markup=greet_kb1)

@dp.message_handler(Text(equals="Back"), state=ClientStatesGroup.callback_answer)
async def back_one(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name} Подберём тебе подходящий оффер?", reply_markup=inline_kb1)

@dp.message_handler(state=ClientStatesGroup.callback_answer)
async def choose_offer_button(message: Message):
    await ClientStatesGroup.choose_tier.set()
    if message.text == offer1.text:
        await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier)

    elif message.text == offer2.text:
        await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier) 

    elif message.text == offer3.text:
        await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier) 

@dp.message_handler(Text(equals="Back"), state=ClientStatesGroup.choose_tier)
async def back_two(message: Message):
    await message.answer(f'Выбирай', reply_markup=greet_kb1)
    await ClientStatesGroup.callback_answer.set()

@dp.message_handler(Text(equals=offer1.text), state=ClientStatesGroup.choose_tier)
async def counties(message: Message):
    await ClientStatesGroup.countries.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)