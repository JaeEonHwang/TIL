# ws_8_1.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        pass

    @classmethod
    def plus_one(cls):
        cls.num_of_animal += 1

    @classmethod
    def get_num_of_number(cls):
        return cls.num_of_animal

class Dog(Animal):
    def __init__(self):
        Animal.plus_one()

class Cat(Animal):
    def __init__(self):
        Animal.plus_one()

class Pet(Dog,Cat):
    def __init__(self):
        pass
    
    @classmethod
    def access_num_of_animal(cls):
        animal_coung = cls.get_num_of_number
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'

if __name__ == '__main__':
    dog = Dog()
    print(Pet.access_num_of_animal())
    cat = Cat()
    print(Pet.access_num_of_animal())


# ws_8_5.py
class Dog:
    sound = '멍멍'

    def __init__(self):
        pass
    
    @classmethod
    def get_sound(cls):
        return cls.sound


class Cat:
    sound = '야옹'

    def __init__(self):
        pass

    @classmethod
    def get_sound(cls):
        return cls.sound


class Pet(Dog,Cat):
    def __init__(self):
        pass

    def __str__(self):
        sound = Pet.get_sound()
        return f'애완동물은 {sound} 소리를 냅니다.'
    
pet = Pet()
print(pet)