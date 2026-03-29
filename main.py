# Declaring Person class
class Person:
    def __init__(self, first_name, last_name, age, email, day, month, year):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self._birth_day = (day, month, year)

    def get_first_name(self):
        return self.first_name.title()

    def get_last_name(self):
        return self.last_name.title()

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    @property
    def birth_day(self):
        return self._birth_day

    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_info(self):
        return (f"{self.first_name.title()} {self.last_name.title()}. {self.age} years old. "
                f"Email: {self.email}. Birth date: {self._birth_day}")

    def get_life_path_number(self):
        number = 0
        for i in self._birth_day:
            number += i

        while number > 9:
            number = (number // 10) + (number % 10)
        return number

    def get_info_by_number(self, number):
        with open("description.txt", "r") as file:
            text = file.read()

        start_tag = f"#{number}"
        if number < 9:
            end_tag = f"#{number + 1}"
            start = text.find(start_tag)
            end = text.find(end_tag)
            result = text[start:end]
        else:
            start = text.find(start_tag)
            result = text[start:]
        return result.strip()



print("Welcome to Numerology program!")

# f_name = input("Enter your first_name: ")
# l_name = input("Enter your last_name: ")
# age = int(input("Enter your age: "))
# email = input("Enter your email: ")
# b_day = int(input("Enter your birth day (1-31): "))
# b_month = int(input("Enter your month (1-12): "))
# b_year = int(input("Enter your year (e.g. 2002): "))
#
# person1 = Person(f_name, l_name, age, email, b_day, b_month, b_year)

person1 = Person("Alex", "Smith", 30, "alexsmith@gmail.com", 1, 10, 2002)
print(person1.get_info())
print(person1.get_life_path_number())
print(person1.get_info_by_number(person1.get_life_path_number()))