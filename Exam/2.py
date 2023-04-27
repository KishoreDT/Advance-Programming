import math

class Circle:

    def __init__(self, x1, x2, y1, y2, r1, r2):
        self.r1 = r1
        self.x1 = x1
        self.y1 = y1
        self.r2 = r2
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        d=math.dist([self.x1,self.y1],[self.x2,self.y2])
        return d
    def collide(self):
        d=math.dist([self.x1,self.y1],[self.x2,self.y2])
        s=self.r1+self.r2
        if d<=s:
            return "They are colliding"
        else:
            return "They are not colliding"
c=Circle(1,2,4,8,5,10)
print(c.distance())
print(c.collide())