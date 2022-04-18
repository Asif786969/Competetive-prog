class complex:
    def __init__(self,r1,i1,r2,i2):
        self.r1=r1
        self.i1=i1
        self.r2=r2
        self.i2=i2
    def print(self):
        if(self.i1>0):
            print(self.r1,"+i",self.i1)
        else:
            print(self.r1,"-i",-self.i1)
    def plus(self):
        self.r1+=self.r2
        self.i1+=self.i2
    def multiply(self):
        a=self.r1
        b=self.i1
        c=self.r2
        d=self.i2
        self.r1=a*c-b*d
        self.i1=a*d+c*b
r1=3
i1=-1
r2=5
i2=-4
c=complex(r1,i1,r2,i2)
c.multiply()
c.print()
