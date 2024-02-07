
"""
https://jellis18.github.io/post/2022-01-11-abc-vs-protocol/
Interface, ABC

"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    ABC classe
    """
   
    @abstractmethod
    def walk(self)->None:
        ...
    
    @abstractmethod
    def speak(self)->None:
        ...

class dog(Animal):
    def walk(self) -> None:
        print("walk")

    def speak(self) -> None:
        print("speak")
       


def main():

  dog=dog()
  dog.speak()
if __name__ == "__main__":
    main()
   
   
   
    

