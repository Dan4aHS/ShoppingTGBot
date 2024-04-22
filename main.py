import asyncio
import client
import handlers


async def main():
    await client.bot.delete_webhook(drop_pending_updates=True)
    await client.dp.start_polling(client.bot)


if __name__ == '__main__':
    asyncio.run(main())
