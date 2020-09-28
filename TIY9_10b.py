class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} Food Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Our restaurant, {self.restaurant_name} is open!")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Vanilla", "Brownie Blast", "Orange Sherbet", "Superman", "Mint"]

    def display_flavors(self):
        print("Flavors: ")
        for flavor in self.flavors:
            print(flavor)
