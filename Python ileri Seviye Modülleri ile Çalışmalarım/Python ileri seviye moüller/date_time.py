from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")
su_an = datetime.now()

print(su_an.year)

print(datetime.strftime(su_an ," %B %A"))

print(datetime.strftime(su_an ," %Y %B %A"))

suan = datetime.now()

saniye = datetime.timestamp(suan)

print(saniye)

suan2 = datetime.fromtimestamp(0),

print(suan2)

tarih = datetime(2020,12,1)

print(datetime.strftime(tarih , "%Y %B %A"))



