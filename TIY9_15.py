from random import choice, randint
import string
my_rand_list = []
for i in range(1, 11):
    my_rand_list.append(randint(1, 100))

letters = string.ascii_letters

for i in range(1, 6):
    my_rand_list.append(choice(letters))

def get_ticket():
    return f"{choice(my_rand_list)} {choice(my_rand_list)} {choice(my_rand_list)} {choice(my_rand_list)}"

winning_ticket = get_ticket()
my_ticket = ""
looped = 0
while not my_ticket == winning_ticket:
    my_ticket = get_ticket()
    looped+=1

print(f"It took {looped} time(s) to get the winning ticket!")





