# homework_2.py

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.occupation}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, я одноклассник/одногруппник, учусь в группе {self.group_name}, "
            f"родился {self.birth_date}, работаю {self.occupation}."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, я ваш друг, моё хобби — {self.hobby}, "
            f"родился {self.birth_date}, работаю {self.occupation}."
        )

classmate1 = Classmate("Бектур", "05.12.2000", "программист", True, "IT-1")
classmate2 = Classmate("Айгерим", "11.03.2001", "дизайнер", False, "IT-1")

friend1 = Friend("Алмаз", "12.12.1999", "инженер", True, "футбол")
friend2 = Friend("Саша", "09.07.2000", "переводчик", True, "книги")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()