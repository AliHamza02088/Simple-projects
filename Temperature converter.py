class Temperature:
    def __init__(self,celcius):
        self._celcius = celcius

    @property
    def fahrenheit(self):
        return (self._celcius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self,value):
        self._celcius = (value - 32) * 5/9

temp = Temperature(0)
print(temp.fahrenheit)
temp.fahrenheit = 100
print(temp._celcius)
