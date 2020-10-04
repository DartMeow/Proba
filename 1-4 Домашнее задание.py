x = int(input("Ведите челое многозначное число "))
y = x % 10
x = x // 10
while x > 0:
    if x % 10 > y:
        y = x % 10
    x = x // 10
print(y)