from random import choice, randint
import string
my_rand_list = []
for i in range(1, 11):
    my_rand_list.append(randint(1, 100))

letters = string.ascii_letters

for i in range(1, 6):
    my_rand_list.append(choice(letters))


print(f"Any ticket matching these letters and or numbers {choice(my_rand_list)} {choice(my_rand_list)} {choice(my_rand_list)} {choice(my_rand_list)}")
