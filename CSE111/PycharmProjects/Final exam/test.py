import datetime

#a1 = input()
#a1 = a1.split(' ')[1]
b1 = input()
b1 = b1.replace(' ', '')
#b1 = b1.split(' : ')
date_time_obj_01 = datetime.datetime.strptime(b1, '%H:%M:%S')
print(date_time_obj_01)


a2 = input()
a2 = a2.split(' ')[1]
b2 = input()
b2 = b2.split(' : ')
date_time_obj_02 = datetime.datetime.strptime(b2, '%Y-%m-%d %H:%M:%S.%f')
print(date_time_obj_02)
