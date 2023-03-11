class bot(object):
    def __init__(self,name):
        self.name = name
        self.pos = (0,0)
        self.alive = True

    def get_pos(self):
        return self.pos


    def set_pos(self,pos):
        x,y = pos
        if x> 725:
            x = 725
        if y > 525:
            y = 525
        if x<0:
            x = 0
        if y < 0:
            y = 0

        self.pos = x,y


    def gen_pos(self,pos):
        x,y = pos
        sx,sy = self.pos
        if x - sx > 0:
            sx+= 1
        if y -sy > 0 :
            sy+= 1
        if x - sx < 0:
            sx-= 1
        if y -sy < 0 :
            sy-= 1
        self.pos = (sx,sy)

    def calive(self,pos):
        x1,y1 = pos
        x2,y2 = self.pos
        if x1 < (x2+75) and x1> x2 and y1 < (y2+75) and y1> y2:
            self.alive = False
#            print 'die'
