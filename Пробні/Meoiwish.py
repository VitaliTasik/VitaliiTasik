python 
class Animal:   
    def speak(self): 
        pass  # Базовый метод, который будет переопределён в дочерних классах 
  
class Dog(Animal):  
    def speak(self):  
        return "Гав!"  
  
class Cat(Animal):  
    def speak(self):  
        return "Мяу!"  
  
animals = [Dog(), Cat()]  
for animal in animals:  
    print(animal.speak())  # Вызывается соответствующий метод для каждого объекта  
