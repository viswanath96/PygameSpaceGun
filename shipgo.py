class ship(object):

    def __init__(self,name,pos):
        self.name = name
        self.alive = True
        self.pos = pos


    def get_pos(self):
        return self.pos


    def set_pos(self,pos):
        x,y = pos
        if x> 700:
            x = 700
        if y > 520:
            y = 520
        if x<0:
            x = 0
        if y < 0:
            y = 0

        self.pos = x,y

    def calive(self,pos):
        x1,y1 = pos
        x2,y2 = self.pos
        if x1 < (x2+80) and y1 < (y2 + 60)  and x1 > (x2-55) and y1 > (y2 - 55):
            print 'death caught'
            self.alive = False
