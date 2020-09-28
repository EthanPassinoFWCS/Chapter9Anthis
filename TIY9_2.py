class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} Food Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Our restaurant, {self.restaurant_name} is open!")


rest1 = Restaurant("Subway", "American")
rest2 = Restaurant("Panda Express", "Chinese")
rest3 = Restaurant("Kitchen Table", "American")

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()
