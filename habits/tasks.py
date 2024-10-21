from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_message_to_user():
    """
    рассылка привычек пользователям за час и за 10 минут, после этого next_date + period, другими словами через сколько дней повторить рассылку, по умолчанию через 1
    """
    habits = Habit.objects.filter(is_pleasant=False)
    for habit in habits:
        if habit.user.telegram_id and habit.next_date == datetime.today().date():
            total_seconds = (
                habit.time.hour * 3600 + habit.time.minute * 60 + habit.time.second
            )
            now_time_is = datetime.now().time()
            now_total_seconds = (
                now_time_is.hour * 3600 + now_time_is.minute * 60 + now_time_is.second
            )
            time_diff = total_seconds - now_total_seconds
            if 3630 > time_diff >= 3570:
                message = f": {habit.title}, которую нужно выполнить через час в {habit.time} в {habit.place}"
                send_telegram_message(message=message, chat_id=habit.user.telegram_id)
            if 570 < time_diff <= 630:
                message = (
                    f": {habit.title}, нужно выполнить через 10 мин в {habit.place}"
                )
                send_telegram_message(message=message, chat_id=habit.user.telegram_id)
                habit.next_date += timedelta(days=habit.period)
                habit.save(update_fields=["next_date"])
