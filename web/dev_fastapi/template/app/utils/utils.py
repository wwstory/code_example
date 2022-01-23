from datetime import datetime, date


# https://www.cnblogs.com/lvxiuquan/archive/2012/07/19/2599174.html
def datetime2date(t: datetime):
    return t.date()


def date2datetime(t: date):
    # return datetime.strptime(str(t), '%Y-%m-%d')
    return datetime.combine(t, datetime.time())
