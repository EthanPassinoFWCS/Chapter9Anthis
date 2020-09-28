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


class Admin(User):
    def __init__(self, first_name, last_name, username, birth, age, gender):
        super().__init__(first_name, last_name, username, birth, age, gender)
        self.privileges = ["can add post", "can delete post", "can edit post", "can ban user", "can unban user", "can change username"]

    def show_privileges(self):
        print("Privileges: ")
        for privilege in self.privileges:
            print(privilege)



ad = Admin("Ethan", "Passino", "EthanPassino", "2/6/03", 17, "M")
ad.show_privileges()
