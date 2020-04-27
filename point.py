class Point:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def ToString(self):
        if(self.z == 0):
            return print('Coordonnées du point: (',self.x,',',self.y,')')
        else:
            return print('Coordonnées du point: (',self.x,',',self.y,',',self.z,')')

p1 = Point(2,3,5)
p2 = Point(1,2)

p1.ToString()

p2.ToString()