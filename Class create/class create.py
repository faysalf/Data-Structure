
class BBPI:
    def __init__(self, number, shift, section):
        self.total_students = number
        self.numberofshift = shift
        self.section = section


    def CMT(self):
        print(self.total_students, self.numberofshift, self.section)

    def EMT(self):
        print(self.total_students, self.numberofshift, self.section)

    def RAT(self):
        print(self.total_students, self.numberofshift, self.section)

    def AIDT(self):
        print(self.total_students, self.numberofshift, self.section)

class CPI(BBPI):
    def CIVIL(self):
        print(self.total_students, self.numberofshift, self.section)

if __name__== "__main__":
    info = BBPI(800,2,2)
    info.CMT()