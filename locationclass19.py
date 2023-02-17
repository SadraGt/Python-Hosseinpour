import math
class Location:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x} , {self.y}")

    def distance(self , other = None):   # چند ریختی اگه دیتای دیگه ای بدی یه دستوری اجرا میشه با همین نام ولی اگه دیتای دیگه ای ندی همین اولی اجرا میشه 
        if other == None:
            D1 = math.sqrt(self.x*self.x+self.y*self.y)
            return D1
        else:
            H1 = (self.x - other.x) ** 2
            V1 = (self.y - other.y) ** 2
            D2 = math.sqrt(H1 + V1)
            return D2
        
