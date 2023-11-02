import calendar
#print(calendar.TextCalendar(firstweekday=6).formatyear(2023))

YY = int("2004")
MM = int("02")
DD = int("29")

""" weekDay = calendar.weekday(YY, MM, DD)
print(weekDay)

weekDayName = calendar.day_name[weekDay]
print(weekDayName)

weekDayNameUpper = weekDayName.upper()
print(weekDayNameUpper) """

print(calendar.day_name[calendar.weekday(YY, MM, DD)].upper())