class User:
    def __init__(self, first_name, last_name, username, birth, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.birth = birth
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Birth: {self.birth}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello, {self.first_name}, how is your day?")


user1 = User("Ethan", "Passino", "EthanPassino", "2/6/03", 17, "M")
user2 = User("Hallie", "Passino", "HalliePassino", "8/08/01", 19, "F")
user3 = User("Lucy", "Passino", "LucyPassino", "??/??/??", 16, "F")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
