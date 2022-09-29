#solution 1

hours=int(input("Enter current hours: "))
minutes=int(input("Enter current minutes: "))
seconds=int(input("Enter current seconds: "))
in_seconds=int(input("Enter a lapse in seconds: "))

total_seconds = (hours * 3600 + minutes * 60 + seconds)+in_seconds
seconds = total_seconds % 60
total_minutes = total_seconds // 60
minutes = total_minutes % 60
total_hours = total_minutes // 60
hours = total_hours % 24

print("Digital clock {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))