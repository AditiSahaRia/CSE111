class Batsman :
    def __init__(self, *data) :
        name = "New Batsman"
        run = 6101
        ball = 7380
        st = "<class 'str'>"
        ine = "<class 'int'>"
        count = 0
        for i in data :
            if str(type(i)) == st :
                name = i
            elif str(type(i)) == ine :
                if count == 0 :
                    run = i
                    count += 1
                elif count == 1 :
                    ball = i
        self.name = name
        self.run = run
        self.ball = ball
    def printCareerStatistics(self) :
        print("Name:",self.name)
        print("Runs Scored: "+str(self.run)+",Balls Faced: "+str(self.ball))
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