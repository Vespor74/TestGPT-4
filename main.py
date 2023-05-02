import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = #'Your telegramm token'
openai.api_key = #'Your openai token'

bot = Bot(token)
dp = Dispatcher(bot)

def update(messages, role, content):
    messages.append({'role': role, 'content':content})
    return messages

@dp.message_handler()
async def send(message : types.Message):
  response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
  )
  await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)