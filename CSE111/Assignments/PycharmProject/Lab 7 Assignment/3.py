import datetime
date = str(datetime.date.today())
date = date.split('-')
current_date = date[1]+'-'+date[2]
if current_date == '09-18':
    print('Happy Birthday my pagli jhalli friend. We love you a lot.')
else:
    print('Waiting for 18th September.')