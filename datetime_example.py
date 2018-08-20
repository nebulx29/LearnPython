from datetime import datetime, date, time

#now = datetime.utcnow()

dt1 = datetime.now()
d1 = date.today()
#t1 = time.now()

print(dt1)
print(d1)
#print(t1)

dt2 = datetime(2018,8,14,21,26,0)
print(dt2)
print(dt2.timestamp())

dt3 = datetime(1970,1,5,0,0,0)
print(dt3)
print(dt3.timestamp())



dt4 = datetime.now()
print(dt4)
print(dt4.strftime("%A, %d. %B %Y %H:%M:%S"))


from datetime import timedelta
dt5 = datetime.now()
td = timedelta(days = 1, hours = 2, minutes = 30)   # add 1 day, 2 hours, 30 minutes
dt6 = dt5 + td
print(dt5)
print(td)
print(dt6)




dt7 = datetime(2018,8,15,20,30,0)
dt8 = datetime(2018,8,15,22,45,0)
td2 = dt8 - dt7
print(td2)
