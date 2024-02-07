from faker import Faker
fake = Faker('fr_FR')



for _ in range(10):
    print(fake.first_name())
class FirstClass:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name
    
    def __eq__(self,other):
        if isinstance(other,FirstClass):
            return other.age==self.age
        return False
    
    def first_func(self)->str:
        return "duck"

def sonorize(duck:FirstClass)->None:
    print(duck.first_func())

instance1=FirstClass(23,"test")
instance2=FirstClass(24,"test")
print(instance1==instance2)




# if __name__=="__main__":
#     sonorize(FirstClass())

