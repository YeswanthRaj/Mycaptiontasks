class Area:
    def getdata(self,l,b):
        self.l=l
        self.b=b
    def cal(self):
        self.a=self.l*self.b
    def display(self):
        print("area=",self.a)
p=Area()
print("enter 2 no.s")
l=int(input())
b=int(input())
p.getdata(l, b)
p.cal()
p.display()