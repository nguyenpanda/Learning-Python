class TeamA:
    member = 0

    def __init__(self, name, age, study_level):
        self.name = name
        self.age = age
        self.study_level = study_level

        TeamA.member += 1

    def GetBornYear(self):
        return 2023 - self.age

    def GetFullInfo(self):
        print("Name: " + self.name)
        print("Born year: " + str(self.GetBornYear()))
        print("Study level: " + self.study_level + "\n")


mem1 = TeamA("Ha Tuong Nguyen", 2004, "University")
mem2 = TeamA("Dinh Ba Khanh", 2004, "University")
mem3 = TeamA("Nguyen Duc Huy", 2004, "University")

TeamA.GetFullInfo(mem1)

class TeamPolicyMaker:
    member = 0

    def __init__(self, name, born, position):
        self.__name = name
        self.__born = born
        self.position = position

        self.member += 1

    def GetPolicyMakerName(self):
        return self.__name

    def GetPolicyMakerAge(self):
        return 2023 - self.__born

    def GetFullInfomationOfPolicyMaker(self):
        print("Name: " + self.__name)
        print("Born year: " +  str(self.__born))
        print("Position: " + self.position + "\n")


p_mem1 = TeamPolicyMaker("Donald Trump", 1946, "Former President")
p_mem2 = TeamPolicyMaker("Antony Blinken", 1962, "Minister of Foreign Affairs")

print(TeamPolicyMaker.GetPolicyMakerName(p_mem1))

# TeamPolicyMaker.GetFullInfomationOfPolicyMaker(p_mem1)


