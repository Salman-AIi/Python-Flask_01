Lottery_player = {
    'Name':'Rolf',
    'Numbers':(13,45,23,67,40)
}

class LotteryPlayer:

    def __init__(self,name):
        self.name = name
        self.numbers = (13,45,23,67,40)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer('Rolf')
player_two = LotteryPlayer('John')
player_two.numbers = (14,25,85,21,45)

print(player_one.name == player_two.name)


# player = LotteryPlayer()
# print(player.name)
# print(player.numbers)