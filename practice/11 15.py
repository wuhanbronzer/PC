# Poker Game 15点
'''from random import randint
class Poker:
    def __init__(self):
        self.num = 10
        self.member = [x for x in range(1,11)]
    def get_card(self):
        a = randint(1,self.num)
        self.num -= 1
        self.member.pop(a-1)
        return a
    @property
    def show_father(self):
        return self.num
class Player(Poker):
    def __init__(self):
        self.points = 0
    def get_card(self, point):
        self.points += point
    def check_status(self):
        return True if self.points <= 15 else False
    def show_points(self):
        return self.points
def main():
    Poke = Poker()
    Play = Player()
    Play2 = Player()
    input('start game with press 1')
    conti = False
    while not conti:
        Play.get_card(Poke.get_card())
        print(f'你当前点数是{Play.show_points()}')
        if not Play.check_status():
            print('you lose')
            print('you boomed')
            break
        Play2.get_card(Poke.get_card())
        if not Play2.check_status():
            print('you win')
            print('he boomed')
            break
        judge = input('是否继续抽牌（输入任意键继续）')
        if not judge:
            conti = True
            if Play.show_points() > Play2.show_points():
                print(f'你赢了，你的点数为{Play.show_points()}，对手的点数为{Play2.show_points()}')
            elif Play.show_points() < Play2.show_points():
                print(f'你输了，你的点数为{Play.show_points()}，对手的点数为{Play2.show_points()}')
            else:
                print('平局')


main()'''
#21点游戏
import random
money = 1000
for i in range(100):
    input('输入1开始游戏')
    while True:
        debt = int(input(f'请下注(金额为整)|当前余额{money}'))
        if 0 < debt <= money:
            break
    num1 = random.randint(1,7) + random.randint(1,7)#应该加入更换随机数种子！！！
    go_on = False
    if num1 == 1 or 7:
        print('玩家胜')
        money += debt
    elif num1 == 2 or 3 or 12:
        print('庄家胜')
        money -= debt
    else:
        go_on = True
    while go_on:
        go_on = False
        num2 = random.randint(1,7) + random.randint(1,7)
        if num2 == num1:
            print('玩家胜')
            money += debt
        elif num2 == 7:
            print('庄家胜')
            money -= debt
        else:
            go_on = True
    print(f'剩余赌资{money}')