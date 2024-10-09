class Player:
    def __init__(self, endurance, speed, strength,accuracy):
        self.endurance=endurance
        self.speed=speed
        self.strength=strength
        self.accuracy=accuracy

class Striker(Player):
    def __init__(self, endurance,speed,strength,accuracy):
        super().__init__(endurance,speed,strength,accuracy)

    def make_goal(self):
        print('Goal!!!')

class Defender(Player):
    def __init__(self,endurance, speed, strength, accuracy):
        super().__init__(endurance, speed, strength, accuracy)

    def defend(self):
        print('Defend the goalie!!!')

class Midfielder(Player):
    def __init__(self,endurance, speed, strength, accuracy):
        super().__init__(endurance, speed, strength, accuracy)

    def assist(self):
        print('Assist the striker!')

class Goalie(Player):
    def __init__(self, endurance, speed, strength, accuracy):
        super().__init__(endurance, speed, strength, accuracy)

    def catch(self):
        print('Catch the ball!')

goalie=Goalie(100,50,100,100)
print(goalie.catch())
