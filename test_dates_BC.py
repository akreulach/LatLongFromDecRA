import datetime as dt

today = dt.date(2018,7,2)
julian_start = dt.date(4713,1,1)

days_4713_to_1 = (julian_start-dt.date(1,1,1)).days
print("days_4713_to_1 = " + str(days_4713_to_1))

days_1_to_2000 = (dt.date(2000,1,1)-dt.date(1,1,1)).days
print("days_1_to_2000 = " + str(days_1_to_2000))

all = int(days_4713_to_1) + int(days_1_to_2000)
print("all = " + str(all))
