time = int(input("Ведите пожалуста количество секунд " ))
hour = str(time//3600)
minute = (time//60)%60
second = time%60
if minute < 10:
    minute = '0' + str(minute)
else:
    minute = str(minute)
if second < 10:
    second = '0' + str(second)
else:
    second = str(second)
print(hour + ':' + minute + ':' + second)
