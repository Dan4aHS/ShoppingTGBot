import requests
from client import dp, bot
from aiogram import types
from aiogram.filters import Command, MagicData
import app.grpcapp
import config
import messages
import qr


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(messages.start_msg())


@dp.message(MagicData)
async def create_request(message: types.Message):
    photos = message.photo
    for i in range(3, len(photos), 4):
        file_id = photos[i].file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, config.TEMP_FILE)
        s = await qr.get_qr_data(config.TEMP_FILE)
        if s == '':
            await message.answer('Не могу считать QR')
            return
        await message.answer('QR успешно прочитан, отправляю в базу данных')
        res = await requests.add_request(message.from_user.id, s)
        await message.answer(str(res.count))




