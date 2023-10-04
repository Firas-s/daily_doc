from datetime import datetime, timezone,timedelta
import pytz
import time

def get_ingestion():
    now = datetime.now(pytz.timezone('UTC'))
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_timestamp(stamp):
    if stamp is None:
        return None
    now = datetime.fromtimestamp(stamp, pytz.timezone('UTC'))
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_now(delta):
    ts = time.time()
    return datetime.fromtimestamp(round(ts)-delta*60, pytz.timezone('UTC'))

def get_timedelta(opening_time):
    time = opening_time.split(':')
    return timedelta(days=0, hours=int(time[0]), minutes=int(time[1]), seconds=0)

def add_hours(time1, time2):
    format = '%H:%M'
    time = str(datetime.strptime(time2, format) - datetime.strptime(time1, format)).split(":")
    return time

def get_hours(time):
    minutes = int(time.total_seconds()/60)
    h, m = divmod(minutes, 60)
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    return "{}:{}".format(h, m)
