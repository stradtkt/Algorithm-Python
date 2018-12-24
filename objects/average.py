class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)

a = AverageList([1,2,3,4,5,6,7,8,9,10])
print(a.average) # 5.5
