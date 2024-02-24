class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")