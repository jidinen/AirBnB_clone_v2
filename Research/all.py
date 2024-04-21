#!/usr/bin/python3
class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

class Car:
    def __init__(self, car_id, brand):
        self.car_id = car_id
        self.brand = brand

class ObjectStorage:
    def __init__(self):
        self.__objects = {}

    def add_object(self, obj_id, obj):
        self.__objects[obj_id] = obj

    def all(self, cls=None):
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    filtered_dict[key] = value
            return filtered_dict

# Create instances of Person and Car
person1 = Person(1, 'John Doe', 12)
person2 = Person(2, 'Jane Smith', 56)
car1 = Car(101, 'Toyota')
car2 = Car(102, 'Honda')

# Create an ObjectStorage instance
storage = ObjectStorage()

# Add objects to the storage
storage.add_object(1, person1)
storage.add_object(2, person2)
storage.add_object(101, car1)
storage.add_object(102, car2)

# Retrieve all objects
all_objects = storage.all()
print("###")
#print("All objects:", all_objects)

# Retrieve only Person objects
person_objects = list(storage.all(cls=Person).values())

print()
#print(storage.all(Person).values())
#print("Person objects:", person_objects)
