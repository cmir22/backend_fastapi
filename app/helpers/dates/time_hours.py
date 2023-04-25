
### Time hours ###

from datetime import datetime


def convert_hours(my_time: str):
    time_format = "%H:%M %p"
    formated = datetime.strptime(my_time, time_format)
    return formated
