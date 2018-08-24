# animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]
# viciousness = [1, 5, 10, 10, 1]

# for i, animal in enumerate(animals):
#     print('animal index {}'.format(i))
#     print('animal {}'.format(animal))


# ships = ["Andrea Doria", "Titanic", "Lusitania"]
# cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

# for i, ship in enumerate(ships):
#     print('ship {}'.format(ship))
#     print(cars[i])

# =====================================================

# door_count = [1, 2, 3]
# cars = [
#         ["black", "honda", "accord"],
#         ["red", "toyota", "corolla"],
#         ["red", "toyota", "corolla"]
#        ]


# for i, car in enumerate(cars):
#     car.append(door_count[i])

# print(cars)

# =======================================================

# things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
# trees = ["cedar", "maple", "fig"]

# for i, row in enumerate(things):
#     row.append(trees[i])

# print(things)

# =======================================================

# apple_prices = [100, 101, 102, 105]

# apple_prices_doubled = [i * 2 for i in apple_prices]
# print('Multiplied by 2 {}'.format(apple_prices_doubled))

# apple_prices_lowered = [i - 100 for i in apple_prices]
# print("Apple prices lowered {}".format(apple_prices_lowered))


# =======================================================

# name_counts = {}

# for row in legislators:
#     first_name = row[1]
#     gender = row[3]
#     year = row[7]

#     if gender == "F":
#         if year > 1940:
#             if first_name not in name_counts:
#                 name_counts[first_name] = 1
#             else:
#                 name_counts[first_name] += 1

# =======================================================



# a = None
# b = a is None or a > 10

# print('a',a)
# print('b',b)


# a = None
# b = a is not None and a > 10

# print('a',a)
# print('b',b)

# =======================================================




# values = [None, 10, 20, 30, None, 50]
# checks = []


# for value in values:
#     if value is not None and value > 30:
#         checks.append(True)
#     else:
#         checks.append(False)




# values = [None, 10, 20, 30, None, 50]
# checks = []


# checks = [x is not None and x > 30 for x in values]


# print(checks)

# =======================================================




# fruits = {
#         "apple": 2,
#         "orange": 5,
#         "melon": 10
#     }

# for fruit in fruits:
#     rating = fruits[fruit]
#     print(fruit)
#     print(rating)



# =======================================================


# max_value = None

# for key, value in name_counts.items():
#     count = value
#     max_value = count if max_value is None or count > max_value else print('wtf')

# print(max_value)


# =======================================================



# top_male_names = []
# male_name_counts = {}
# for row in legislators:
#     if row[3] == "M" and row[7] > 1940:
#         name = row[1]
#         if name in male_name_counts:
#             male_name_counts[name] = male_name_counts[name] + 1
#         else:
#             male_name_counts[name] = 1
            
# highest_male_count = None
# for name,count in male_name_counts.items():
#     if highest_male_count is None or count > highest_male_count:
#         highest_male_count = count

# for name,count in male_name_counts.items():
#     if count == highest_male_count:
#         top_male_names.append(name)
    


