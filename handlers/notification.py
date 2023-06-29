import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINs, bot
from DataBase.database import sql_command_all
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger


async def go_to_sleep(text):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(
            user[0], f"ИДи спаать {text} !"
        )


async def wake_up():
    for user in ADMINs:
        await bot.send_video(
            chat_id=user,
            caption=f"Вставай!"
        )


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        wake_up,
        target_date = datetime(2023, 7, 10, 0, 0)
        ),



    scheduler.start()