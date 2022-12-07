from config import *
from keyboard import *

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def inline_echo(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name} Подберём тебе подходящий оффер?", reply_markup=inline_kb1)

@dp.callback_query_handler()
async def some_callback_handler(query: types.CallbackQuery):
    print(query.message.text)
    if query.data == "0":
        print("1")
        await bot.send_message(query.from_user.id, f'Выбирай', reply_markup=greet_kb1)
    else:
        one()
    print(query.message.text)

@dp.message_handler()
async def choose_offer_button(message: Message):
    if message.text == offer1.text:
        await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier)
    elif message.text == offer2.text:
        await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier)
    elif message.text == offer3.text:
        await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier)
    else:
        two()

@dp.message_handler()
def one():
    print("2")
    async def back_one(message: Message):
        await message.answer(f"Привет, {message.from_user.full_name} Подберём тебе подходящий оффер?", reply_markup=inline_kb1) 
    return back_one

@dp.message_handler()
def two():
    async def back_two(message: Message):
        await bot.send_message(message.from_user.id, f'Выбирай', reply_markup=greet_kb1)
    return back_two

@dp.message_handler()
def three():
    async def back_three(message: Message):
        if message.text == offer1.text:
            await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier)
        elif message.text == offer2.text:
            await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier)
        elif message.text == offer3.text:
            await message.answer(f"Выбери подходящее ГЕО", reply_markup=tier)
    return back_three

one()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)