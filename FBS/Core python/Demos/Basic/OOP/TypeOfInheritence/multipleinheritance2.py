
class Agriculture:
    def __init__(self,crops):
        self.crop=crops

    def getCrop(self):
        return self.crop
    def setCrop(self,crops):
        self.crop=crops

    def __str__(self):
        return f"Agriculture class"
# ++++++++++++++++++++++++++++++++++++++++++++++++++

class Technology:
    def __init__(self,sensor):
        self.sensor=sensor

    def getSensor(self):
        return self.sensor
    def setSensor(self,sensor):
        self.sensor=sensor

    def __str__(self):
        return f"Technology class"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++

class SmartFarming(Technology,Agriculture):
    def __init__(self, crops):
        super().__init__(crops)

    def __str__(self):
        return super().__str__()+f"\nSmartFarming class"

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
s1=SmartFarming("Cotton")
print(s1)