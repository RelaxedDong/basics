import datetime
def getYesterday():
    today = datetime.datetime.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday
print(getYesterday())
