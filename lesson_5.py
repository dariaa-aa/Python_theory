class Person:

    country = 'USA'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return f'{self.fname}{self.lname}@gmail.com'

    def speak(self):
        return f'{self.fname} {self.lname} says hello'

    def learn(self):
        return 'I\'m learning'

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country
        print(cls.country)

    @staticmethod
    def is_adult(age):
        return age > 18

person_1 = Person('Alex', 'Baker')
#
# print(person_1.speak())
#
person_2 = Person('Dasha', 'Podolskaia')
# print(person_2.lname)
# print(person_2.speak())
# print(person_2.country)
# Person.change_country('Canada')
# print(tester_1.country)
# print(programmer_1.country)
# print(person_2.country)
# print(Person.is_adult(15))
# print(person_1.email)
# person_1.fname = 'Bob'
# print(person_1.email)

class Programmer(Person):
    def __init__(self, fname, lname, language, job_title, salary):
        super().__init__(fname, lname)
        self.language = language
        self._job_title = job_title
        self.__salary = salary

    def coding(self):
        return f'{self._job_title} {self.fname} {self.lname} uses {self.language} language'

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def learn(self):
        return 'I\'m learning coding'

programmer_1 = Programmer('Daria', 'Podol', 'Python', 'AQA', '4900 $')

# print(programmer_1.coding())
# print(programmer_1.__dict__)
# print(programmer_1.speak())
# print(programmer_1.country)
# print(programmer_1.get_salary())
# programmer_1.set_salary('5000 $')
# print(programmer_1.get_salary())
# print(programmer_1._Programmer__salary)
# print(programmer_1._job_title)

class Tester(Person):
    def __init__(self, fname, lname, job_title, framework):
        super().__init__(fname, lname)
        self.framework = framework
        self.job_title = job_title

    def testing(self):
        return f'{self.fname} {self.lname} as a(n) {self.job_title} uses {self.framework}'

    def say(self, **kwargs):
        dct = kwargs
        word = kwargs['word']
        amount = kwargs['amount']
        return f'{self.job_title} {self.fname} is saying {word} {amount}'

    # def learn(self):
    #     return 'I\'m learning testing'

# tester_1 = Tester('Dima', 'PyTest', 'SDET')
# print(tester_1.say(word='poop', amount='5 times'))
# print(tester_1.testing())
# print(tester_1.framework)
# print(tester_1.__dict__)
# print(tester_1.country)
# tester_1.lname = 'Pussy'
# print(tester_1.lname)
# tester_1.fname = 'Vasya'
# print(tester_1.__dict__)

# print(person_1.learn())
# print(programmer_1.learn())
# print(tester_1.learn())

# print(programmer_1.is_adult(13))

# class SDET(Tester, Programmer):
#
#     def __init__(self, fname, lname, language, job_title, salary, framework):
#             Person.__init__(fname, lname)
#             Tester.__init__(fname, lname, job_title, framework)
#             Programmer.__init__(fname, lname, language, job_title, salary)

    def build_arch(self):
        return 'I\'m building testing architecture'
#
# sdet_1 = SDET('Petya', 'Vovovich', 'Python', 'SDET', '5000$', 'pytest')
# print(sdet_1.__dict__)

class Stack:

    def __init__(self):
        self.values = []

    def push(self, element):
        self.values.append(element)

    def pop(self):
        if not self.is_empty():
            self.values.pop()
        else:
            print('Пустой стек')

    def peek(self):
        if not self.is_empty():
            return self.values[-1]
        else:
            print('Пустой стек')

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

    def get_stack(self):
        return self.values

# stack_1 = Stack()
# print(stack_1.is_empty())
# stack_1.pop()
# stack_1.push(5)
# print(stack_1.peek())
# print(stack_1.size())
# stack_1.pop()
# print(stack_1.size())
# stack_1.peek()
# stack_1.push([89, 7, 3])
# print(stack_1.get_stack())

class User:

    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.add_one()

    @classmethod
    def add_one(cls):
        cls.count += 1

user_1 = User('Dasha', 'Podolskaia')
# print(User.count)

# setattr(User, 'age', 30)
# setattr(user_1, 'eye_color', 'blue')
# print(User.age)
# print(user_1.age)
# print(user_1.eye_color)

class Persona:
    pass

persona_1 = Persona()

file = {
    'name': 'Dasha',
    'age': 23,
    'hobby': 'puzzles'
}

for key, value in file.items():
    setattr(persona_1, key, value)

# print(persona_1.__dict__)

file_2 = ['age', 'fname', 'lmane']

# for value in file_2:
#     if getattr(persona_1, value, False):
        # print(getattr(persona_1, value))

# print(hasattr(Persona, 'name'))
# print(hasattr(persona_1, 'name'))
# setattr(persona_1, 'gender', 'male')
# print(hasattr(persona_1, 'gender'))
# print(getattr(persona_1, 'gender'))
# delattr(persona_1, 'gender')
# print(hasattr(persona_1, 'gender'))

class Coordinates:
    def __init__(self):
        self.x = 0
        self.y = 0

point_1 = Coordinates()
# print(point_1.__dict__)
point_1.x = 5
# print(point_1.__dict__)

class Numbers:
    def __init__(self, number):
        self.is_even(number)

    def is_even(self, num):
        if num % 2 == 0:
            self.number = num
        else:
            self.number = num + 1

num_1 = Numbers(12)
num_2 = Numbers(197)
# print(num_1.__dict__)
# print(num_2.__dict__)



class Animal:

    def __init__(self, name, owner, color, speed):
        self.__name = name
        self.__owner = owner
        self.color = color
        self.speed = speed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

cat_1 = Animal('Frosya', 'Dasha', 'multiple', 5)
cat_1.set_name('Love')
# print(cat_1.get_name())
cat_1.owner = 'me'
# print(cat_1.owner)

class Cat(Animal):

    def __init__(self, name, owner, color, speed):
        self.name = name
        self.owner = owner
        super().__init__(name, owner, color, speed)

    def says(self, word):
        return f'Cat named {self.name} says {word}'


cat_2 = Cat('Pinky', 'Vasya', 'brown', 5)
print(cat_2.says('fuck you'))

class Dog(Animal):
    pass

dog_1 = Dog('Pusya', 'Dima', 'red', 8)
print(dog_1.__dict__)
dog_1.__dict__ = {'_Animal__name': 'Pusya', '_Animal__owner': 'Dima', 'color': 'red', 'speed': 8, 'type': 'mammal'}
print(dog_1.type)