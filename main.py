from pprint import pprint

cook_book = {}


def get_cook_book():
    with open('recipes.txt', encoding='UTF-8') as file_cook:
        for line in file_cook:
            name = line.strip()
            cook_book[name] = []
            file_cook.readline()
            item = 0
            while item == 0:
                ingredients = file_cook.readline()
                if len(ingredients) > 1:
                    ingredients = ingredients.strip()
                    ingredients = ingredients.split(' | ')
                    in_cook_book = \
                        {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
                    cook_book[name].append(in_cook_book)
                else:
                    item += 1
    pprint(cook_book)


def get_ingredients(dishes, person_count):
    dish_list = []
    ingredients = {}
    for name in dishes:
        for key, value in cook_book.items():
            if name == key:
                for item in value:
                    dish_list.append(item['ingredient_name'])
                    if len(set(dish_list)) == len(dish_list):
                        ingredients[item['ingredient_name']] = \
                            {'quantity': int(item['quantity']) * person_count, 'measure': item['measure']}
                    else:
                        difference = len(dish_list) - len(set(dish_list))
                        ingredients[item['ingredient_name']] = \
                            {'quantity': int(item['quantity']) * person_count * (difference + 1), 'measure': item['measure']}
    for key, value in ingredients.items():
        print(key, value)


get_cook_book()
print()
get_ingredients(['Запеченный картофель', 'Омлет'], 2)
print()

import os

base_path = os.getcwd()
path_first = '1.txt'
path_second = '2.txt'
path_third = '3.txt'
full_path_first = os.path.join(base_path, path_first)
full_path_second = os.path.join(base_path, path_second)
full_path_third = os.path.join(base_path, path_third)

with open('1.txt', 'r', encoding='UTF-8') as file:
    file_1 = file.readlines()

with open('2.txt', 'r', encoding='UTF-8') as file:
    file_2 = file.readlines()

with open('3.txt', 'r', encoding='UTF-8') as file:
    file_3 = file.readlines()

max_len = (len(file_1), len(file_2), len(file_3))
print(max_len)

with open('combined.txt', 'w', encoding='UTF-8') as file_combined:
    file_combined.write('Это первая статья' + '\n')
    file_combined.write('Всего строк: ' + str(len(file_1)) + '\n')
    file_combined.writelines(file_1)
    file_combined.write('\n')

with open('combined.txt', 'a', encoding='UTF-8') as file_combined:
    file_combined.write('Это вторая статья' + '\n')
    file_combined.write('Всего строк: ' + str(len(file_2)) + '\n')
    file_combined.writelines(file_2)
    file_combined.write('\n')
    file_combined.write('\n')

with open('combined.txt', 'a', encoding='UTF-8') as file_combined:
    file_combined.write('Это третья статья' + '\n')
    file_combined.write('Всего строк: ' + str(len(file_3)) + '\n')
    file_combined.writelines(file_3)
    file_combined.write('\n')




