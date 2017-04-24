
class Line(object):
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        (x1, y1) = self.coor1
        (x2, y2) = self.coor2
        dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
        return dis

    def slope(self):
        (x1, y1) = self.coor1
        (x2, y2) = self.coor2
        slope = (float(y2)-y1)/(x2-x1)
        return slope


def main():
    l = Line((3,2), (8, 10))
    print('distance ', l.distance())
    print ('slope ', l.slope())

main()
