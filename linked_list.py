class node:
    def __init__(self,x):
        self.data=x
        self.adrs=None

n1=node(500)
n2=node(200)
n3=node(400)
n4=node(100)
n5=node(300)

n4.adrs=n2
n2.adrs=n5
n5.adrs=n3
n3.adrs=n1

t=n4
while t:
    print(t.data,"==>",end='')
    t=t.adrs
