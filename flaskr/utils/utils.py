import datetime


def get_diff_hours(date1: datetime.datetime, date2: datetime.datetime) -> float:
    diff = date2 - date1
    diff_hours = diff.total_seconds() / 60 / 60
    return diff_hours

# if __name__ == '__main__':
#     now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
#     last_hour_date_time = now - datetime.timedelta(hours=1, minutes=30)
#     hours = get_diff_hours(last_hour_date_time, now)
#     print(hours)
