class grandfather: #Parent class of father
    def grandfatherInfo(self):
        print("i have land")

class father(grandfather):  #parent class of child and child class of grandfather
    def fatherInfo(self):
        print("i have a car")

class child(father):
    def childInfo(self):  #child class of father
        print("i have a bike")


a=grandfather()   #object of class grandfather 
a.grandfatherInfo()

b=father()  #object of class father 
b.grandfatherInfo()
b.fatherInfo()

check=child()  #object of class child 
check.grandfatherInfo()
check.fatherInfo()
check.childInfo()


'''
class grandfather: can access methods of itself only

class father: can access methods of itself and class grandfather(inherits class grandfather)

class child: can access methods of itself,class father and class grandfather (inherits class father )
'''
