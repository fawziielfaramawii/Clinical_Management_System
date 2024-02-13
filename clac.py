#from datetime import date
class employee :

    def __init__(self,name ,age ,department ,rating ,salary):
        self.name =name
        self.age = age
'''
        self.department= department
        self.collage=collage
        self.rating=rating
        self.salary=salary
        
     
    def get_name(self):
        return self.__name
    def set_name(self,newname):
         self.__name=newname
    def get_age(self):
        return self.__age
    def set_age(self,newage):
         self.__age=newage
         '''
         
         
         
         

    def describe(self):
        print(f"my name is : {self.name} and my age is :  {self.age} and")
        # = print("my name is : {} and my age is :  {} and",format(self.name,self.age)) 

        
        '''
    @classmethod
    def initbirthdayy(cls,name,birthday):
        return cls(name,date.today().year-birthday)

'''







'''
    def rate(self):
        if self.rating>=5:
            return True
        else:
            return False

    def bonus(self):
        if self.age==60 :
            self.salary +=500
            print("increase " + str(self.salary))
        else :
            print(" not increase")
'''


