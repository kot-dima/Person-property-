# class Person:
#     def __init__(self, name: str, surname: str, age: int):
#         self.__name: str = name
#         self.__surname: str = surname
#         self.__age: int = age

#     def show_person(self):
#         print("Дані:\n Імя та прізвище:", self.__name,
#               " ", self.__surname, "\n Віk: ", self.__age)

#     # @property
#     # def name(self):
#     #     return self.__name

#     # @name.setter
#     # def name(self):
#     #     return self.__name

#     # @surname.getter
#     # def surname(self):
#     #     return surname()

#     #     /
#     #     /
#     #     /


# name = input("Enter name - ")
# surname = input("Enter surname - ")
# age = int(input("Enter age - "))

# people = Person(name, surname, age)
# people.show_person()


class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.__name: str = name
        self.__surname: str = surname
        self.__age: int = age

    def show_person_info(self):
        print("Name: ", self.__name, "\nSurname: ",
              self.__surname, "\nAge: ", self.__age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname: str):
        self.__surname = new_surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: str):
        self.__age = new_age


# gvido = Person("Gvido", "Van Rossum", 46)
# gvido.show_person_info()
# print("property before ", gvido.name)
# print("-----------------------------------------")
# gvido.name = "Petya"
# gvido.show_person_info()
# print("property after ", gvido.name)


class Juniour (Person):
    def __init__(self, name: str, surname: str, age: int, skills: str, position: str):
        Person.__init__(self, name, surname, age)
        self.__skills = skills
        self.__position = position

    def show_person_info(self):
        print("Name: ", self.name, "\nSurname: ",
              self.surname, "\nAge: ", self.age,
              "\nSkills: ", self.__skills, "\nPosition: ", self.__position)


jun = Juniour("Adam", "Dobson", 23, "Write cod using Stack Overflow",
              "Full Stack Overflow developer")

jun.show_person_info()
print("------------------")
jun.name = "Adamus"
jun.show_person_info()
print("------------------")
jun.age = 25
jun.show_person_info()

