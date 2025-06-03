import random
import math

colors = ['red', 'green' , 'pink', 'orange' , 'white' ,'light green' ,
          'light red', 'brown', 'yellow' ,'black']

def setColor():
    a = math.floor(random.random()*10)
    return colors[a]

class Fruit:
    def __init__(self,name):
        self.name = name
        self.shape = 'Rounded'
        self.color = setColor()
    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    def setShape(self, shape):
        self.shape = shape
    def getShape(self):
        return self.shape
        


apple = Fruit("apple")
banana = Fruit("banana")
banana.setShape("Tall")
print(banana.getName())
print(banana.getColor())
print(banana.getShape())
print(apple.getShape())