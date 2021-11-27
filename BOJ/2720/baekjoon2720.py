t = int(input())
money = []

for i in range(t):
    money = int(input())
    
    quar = money // 25
    money %= 25
    dime = money // 10
    money %= 10
    nick = money // 5
    money %= 5
    penny = money
    
    print(quar, dime, nick, penny)