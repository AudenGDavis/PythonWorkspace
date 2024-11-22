import json

#ChatGPT Dog Class:
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
        
    def to_dict(self):
        return {
            "name": self.name,
            "breed": self.breed,
            "age": self.age
        }
        
my_dog = Dog(name="Buddy", breed="Golden Retriever", age=3)

jsonString = json.dumps(my_dog.to_dict())
print(jsonString)