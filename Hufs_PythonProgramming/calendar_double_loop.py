year = int(input("Enter Gregorian year (year >= 1583): \n\n"))


month_what = [1,2,3,4,5,6,7,8,9,10,11,12]
week_all = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
month_day = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


#Julian code

#달 연도 요일 출력 
for i in month_what:
	print('%s %d' %(month_day[i-1], year))
	print("  S  M  T  W  T  F  S")
	
	y = year
	month = i
	m = month
	d = 1
	if month in [1, 3, 5, 7, 8, 10, 12]:
		month_days = 31
	elif month in [4, 6, 9, 11]:
		month_days = 30
	elif month in [2]:
		month_days = 28
	
	if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):#윤년 = 2월 29일까지 있는 년
		if month == 2:
			month_days = 29		
			
	y += 8000
	if m < 3:
		y -= 1
		m += 12
	julian = (y * 365) + (y // 4) - (y // 100) + (y // 400) - 1200820 + (m * 153 + 3)// 5 - 92 + (d - 1)
	
	start_day = julian % 7 
#일 출력 
	if ( 0 <= start_day <= 5):
		for i in range(start_day+1):
			print('   ', end='')		
		
	for i in range(1, month_days + 1):
		if ( 0 <= start_day <= 5):
			if (start_day + i + 1 ) % 7 == 0 and i != month_days :
				print('{:3d}'.format(i))
			elif i == month_days:
				print('{:3d}\n'.format(i))
			else :
				print('{:3d}'.format(i), end ='')
				
		else:
			if i % 7 ==0:
					print('{:3d}'.format(i))
			elif i == month_days:
					print('{:3d}\n'.format(i))
			else:
					print('{:3d}'.format(i), end ='')