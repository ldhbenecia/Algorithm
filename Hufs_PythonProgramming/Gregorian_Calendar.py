# To compute the week day, given year, month, day.
# The day after the 4th. October 1582 would be 15th. October 1582

year = int(input('Enter Gregorian year (year >= 1583): \n'))
month = int(input('Enter Gregorian month (month: 1..12): \n'))
day = int(input('Enter Gregorian day (1..28|29|30|31): \n'))

if month in [1,3,5,7,8,10,12]:
	month_days = 31
elif month in [4,6,9,11]:
	month_days = 30
elif month in [2]:
	month_days = 28
	
if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):#윤년 = 2월 29일까지 있는 년
	if month == 2:
		month_days = 29

#Julian 값
y = year
m = month
d = day

y += 8000
if m < 3:
	y -=1
	m +=12
julian = (y * 365) + (y // 4) - (y // 100) + (y // 400) - 1200820 + (m *153 + 3)// 5 - 92 + (d - 1)


if year < 1583:
	print("Enter year >= 1583! Try again!")
elif month > 12:
	print("Wrong month! Try again!")
elif day > month_days:
	print("Wrong day! Try again!")
	
	
elif julian % 7 + 1 == 1:
	print("%d-%d-%d is Monday" %(year,month,day))
elif julian % 7 + 1 == 2:
	print("%d-%d-%d is Tuesday" %(year,month,day))
elif julian % 7 + 1 == 3:
	print("%d-%d-%d is Wednesday" %(year,month,day))
elif julian % 7 + 1 == 4:
	print("%d-%d-%d is Thursday" %(year,month,day))
elif julian % 7 + 1 == 5:
	print("%d-%d-%d is Friday" %(year,month,day))
elif julian % 7 + 1 == 6:
	print("%d-%d-%d is Saturday" %(year,month,day))
elif julian % 7 + 1 == 7:
	print("%d-%d-%d is Sunday" %(year,month,day))