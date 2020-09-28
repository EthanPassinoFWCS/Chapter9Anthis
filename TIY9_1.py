class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} Food Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Our restaurant, {self.restaurant_name} is open!")


rest = Restaurant("Kitchen Table", "American")
print(rest.restaurant_name)
print(rest.cuisine_type)

rest.describe_restaurant()
rest.open_restaurant()
