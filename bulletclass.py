class bullet:
    
    def __init__(self,apos,iangle):
        self.alive = True
        self.direction = True
        self.bl = 5
        self.ipos = apos
        self.angle = iangle
        self.fpos = [5,0]
        self.inc = []

    def cfpos(self,cosv,sinv):
        x = self.bl * cosv
        y = self.bl * sinv
        self.inc = (x,y)
        x = x + self.ipos[0]
        y = y + self.ipos[1]
        self.fpos = [x,y]

    def get_p1(self):
        return self.fpos
    def get_p2(self):
        return self.ipos

    def newpos(self):
        self.fpos[0] += self.inc[0]
        self.fpos[1] += self.inc[1]
        self.ipos[0] += self.inc[0]
        self.ipos[1] += self.inc[1]
  
    def prnt(self):
        return "bullet print"
      
