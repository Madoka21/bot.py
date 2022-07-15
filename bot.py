from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import token

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я Метрополитен бот")

    
@dp.message_handler(commands=['all'])
async def process_start_command(message: types.Message):
    url = "http://metroalmaty.kz/?q=ru/schedule-list"
    a = requests.get(url)
    soup = BeautifulSoup(a.text, "html.parser")
    td = soup.find_all("td")
    b = []
    for t in td:
        b.append(t.text)


    for c in range (len(b)):
        if c % 3 == 1:
            await message.reply(b[c], b[c + 1], b[c - 1])
