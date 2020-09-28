class User:
    def __init__(self, first_name, last_name, username, birth, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.birth = birth
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Birth: {self.birth}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello, {self.first_name}, how is your day?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Ethan", "Passino", "EthanPassino", "2/6/03", 17, "M")

print(str(user1.login_attempts))
user1.increment_login_attempts()
print(str(user1.login_attempts))
user1.increment_login_attempts()
user1.increment_login_attempts()
print(str(user1.login_attempts))
user1.reset_login_attempts()
print(str(user1.login_attempts))

