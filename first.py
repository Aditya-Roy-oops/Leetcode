print('hello Python')
message="hi Whats ur name?" #string
print(message)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.capitalize())

print(f"{name} is fine")

print(f"{name.capitalize()} is fine today.")
print(f"\t{name.capitalize()} is fine today.\nWhat a bout you?")

universe_age= 14_000_000_000 
print(universe_age) # prints only 14000000000

x,y,z=1,3,2

m=max(x,y,z)
print(m)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

# print(motorcycles.pop())
last_owened=motorcycles.pop()
print(last_owened)

motorcycles.append('kawasaki')
print(motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyato', 'subaru', 'mesrati']
print(sorted(cars)) # temperory sorting
print(cars)

cars.reverse()
print(cars)
print(len(cars))

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print(*magicians)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("Thank you, everyone. That was a great magic show!")


for value in range(1,5):
    print(value)

for value in range(5,1): # dosen't work or shows nothing like decrement series
    print(value,'\n')

for value in range(4,11,2): # Even numbers using skipping value by 2
    print(value)

even_numbers = list(range(2, 11, 2)) # listing values with skipping values
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print('squares list: ',squares)

print('min:' , min(squares))
print('max:' , max(squares))
print('sum:' , sum(squares))

cubes = [value**3 for value in range(1, 11)] # a[] = [<function> <conditions>] 
print(cubes)

# one_million = list[range(1,100_000_1)] # wrong way
# one_million = [range(1,100_000_1)] # wrong way
# one_million = (range(1,100_000_1)) # wrong way

one_million = list(range(1,100_000_1))
# print('one million in a list ', one_million) # to print one_million list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[:4])

print(players[2:])

print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods

# friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
print('\n')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
print('\n')


dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0]=250 # 'tuple' object does not support item assignment

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
print(car == 'audi') # Case-Sensitive
print(car.lower() == 'audi')

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("Hold the anchovies!")


age1 = 22
age2 = 16
# and
if age1>=21 and age2>18:
    print("ok")
else:
    print('not ok')


# or
if age1>=21 or age2>18:
    print("ok")
else:
    print('not ok')


banned_users = ['andrew', 'carolina', 'david']
user = 'mArie'
if user not in banned_users:
    print(f"{user.lower().title()}, u can post a response if u wish.")

age = 12

if age < 4 :
    price = 0
elif age < 18 :
    price = 25
elif age < 65 :
    price = 40
else :
    price = 20

print(f"Your admission cost is ${price}")


requested_toppings=['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('adding mushrooms')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
    print('adding extra cheese')
print('\nFinished making your pizza\n')


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}')

print('Finished pizza making\n')


for requested_topping in requested_toppings:
    if requested_topping is 'green peppers': # if requested_topping == 'green peppers':
        print('sorry, we out of green peppers')
    else:
        print( f'Adding {requested_topping}')
print('Finished pizza making\n')


requested_toppings=[] # Empty list

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('Finished making pizza\n')
else:
    print('Are u sure u want a plain pizza?\n')

dict3 = dict([('c', 3), ('d', 4)])  # Using dict() with list of tuples
dict4 = dict(e=5, f=6)  # Using keyword arguments
print(dict3)
print(dict4)