from abc import ABC , abstractmethod
import abc

class Animal (ABC):

    @property
    @abstractmethod
    def age (self):
        pass
        
    def run(self):
        pass

    def walk(self):
        pass

class Human (Animal):

    def run(self):
        print("The human is running!")
    
    def print_name(self):
        print("human name:") 
    
    def walk (self):
        print("human is walking!")

class Cat (Animal):

    def run(self):
        print("the cat is running!")

class Dog(Animal):
    
    def run(self):
        print ("cat is running!")
    
    def walk(self):
        print("cat is walking!")

    @property
    def age(self):
        return 20
    
    