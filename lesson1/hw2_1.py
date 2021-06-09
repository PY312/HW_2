class Person:
    __total_persons = 0
    year = 2021
    def __init__(self, __name, __birth_year, **kwargs):
        self.__name = __name
        self.__birth_year = __birth_year
        self.__language = kwargs
        if self.__birth_year > 2021:
            raise ('Не верно введен год')
        Person.__total_persons+= 1

    def get_language(self):
        return self.kwargs
    def is_adult(self):
        if self.__birth_year <= 2003:
            return True
        else:
            return False
    def get_age(self):
         print(f'Возраст {self.year - self.__birth_year} лет')

    @classmethod
    def get_total_person(cls):
        return cls.__total_persons

    def talk(self):
        print('Hello World!')

class Teacher(Person):
    def talk(self, name):
        self.__name = name
        print(f"Greetings, I'm your teacher {name}")

    def teach(self, name):
        print(f'Lesson started by {name}')


p1 = Person('Иван', 1984, language = "russian")
p2 = Person('Петр', 1991, language = "ukrain")
p3 = Person('Жаныбек', 1940, language = "kyrgyz")
p4 = Person('Серик', 1984)
t1 = Teacher('Jack', 1989, language = "english")
p1.get_age()
p1.talk()
t1.talk()


