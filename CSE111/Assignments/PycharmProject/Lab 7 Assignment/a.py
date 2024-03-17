class Batsman :
    name = 'New Batsman'
    run = 6101
    ball = 7380
    def __init__(self, *data) :
        self.count = 0
        for i in data :
            self.count += 1
        if self.count == 0:
            self.name = Batsman.name
            self.run = Batsman.run
            self.ball = Batsman.ball
        elif self.count == 1:
            self.name = data[0]
            self.run = Batsman.run
            self.ball = Batsman.ball
        elif self.count == 2:
            self.name = data[0]
            self.run = data[1]
            self.ball = Batsman.ball
        elif self.count == 3:
            self.name = data[0]
            self.run = data[1]
            self.ball = data[2]

    def printCareerStatistics(self) :
        print("Name:",self.name)
        print(f"Runs Scored: {self.run} Balls Faced: {self.ball}")
    def battingStrikeRate(self) :
        a = self.run / self.ball
        a = a * 100
        return a
    def setName(self,name) :
        self.name = name





#====================================================================================
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())