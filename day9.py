# class Avenger:
#     def __init__(self, name, knownAs):
#         self.name = name
#         self.knownAs = knownAs

#     def reveal_identity(self):
#         print(f'I am {self.name}, also known as {self.knownAs}')

# hulk = Avenger('Bruce Banner', 'Hulk')
# iron_man = Avenger('Tony Stark', 'Iron Man')
    
# hulk.reveal_identity()
# iron_man.reveal_identity()

class Player:
    def __init__(self, name, age, direction):
        self.name = name
        self.age = age
        self.direction = direction
        
    
    def run(self):
        return f'{self.name} is running'

    def miss_ball(self):
        return f'{self.name} missed the ball on the {self.direction} side of the field'
    
class Cricketer(Player):
    def catch_ball(self):
        return f'{self.name} caught the ball on the {self.direction} side of the field'

class Batsman(Cricketer):
    def swing_bat(self):
        return f'What a shot to the {self.direction} by {self.name}' 

player1 = Batsman('Nathan Wawruck', 24, 'left')
player2 = Batsman('Les Donald', 24, 'right')

print(player2.swing_bat())
print(player2.miss_ball())

print(player1.run())
print(player1.catch_ball())
print(player1.swing_bat())