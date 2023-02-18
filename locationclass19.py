import math
class Location:
    # def __init__(self,x=0,y=0):
    #     self.x = x
    #     self.y = y

    def __init__(self,x:int=0,y:int=0):
        try:
            self.x = int(x)
            self.y = int(y)
        except:
            raise Exception("Invalid values.")
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


    #----------Ep 20 Python FL----------



    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        LP = Location()
        LP.x = self.x + other.x
        LP.y = self.y + other.y

        return LP 

    def __sub__(self, other):
        LP = Location()
        LP.x = self.x - other.x
        LP.y = self.y - other.y

        return LP 

        
