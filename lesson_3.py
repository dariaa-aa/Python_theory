# my_list = [1, 2, 3]
#
# sentence = 'What a wonderful life'
# my_list1 = sentence.split()
# print(my_list1)
# my_list3 = list(sentence)
# print(my_list3)

# numbers = [1, 2, 3, 5, 6]
# for num in numbers:
#     print(num ** 2)

# print(numbers[-1])
#
# a = 'pool'
# numbers.append(a)
# print(numbers)
# numbers.insert(3, a)
# print(numbers)
# print(numbers.index(3))

# numbers2 = [10, 89, 5]
# numbers.append(numbers2)
# print(numbers)
# numbers.extend(numbers2)
# print(numbers)

# numbers2.sort()
# print(numbers2)
# print(sorted(numbers2))
# numbers2.reverse()
# print(numbers2)
# print(numbers2[::-1])

# num2 = []
# for i in numbers2:
#     if i % 2:
#         num2.append(i * i)
# print(num2)
#
# num3 = [x * x for x in numbers2 if not x % 2]
# print(num3)

# my_tuple = (1, 4, 6, 8, 98)
# print(my_tuple)
# my_tuple1 = 2, 7, 76, 34
# print(my_tuple1)
# print(max(my_tuple1))
# print(sum(my_tuple))

# def func(*args):
#     for item in args:
#         yield item * item
#
# for i in func(*my_tuple):
#     print(i)

my_dict = {
    'name': 'Alex',
    'surname': 'Smith',
    'age': 30,
    'department': 'IT'
}
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict['name'])
# print(my_dict.items())
# print(my_dict.pop('name'))
# # print(my_dict)
# my_dict['salary'] = 10000
# print(my_dict)
# print(my_dict.get('name', 'Not found'))

# for i in my_dict.items():
#     print(i)

# for key in my_dict:
#     print(key)

# for value in my_dict.values():
#     print(value)

# my_dict1 = {
#     'num1': 1,
#     'num2': 67,
#     'num3': 23,
#     'num4': 6,
#     'num15': 5,
# }
#
# result = 0
# for key in my_dict1:
#     result += my_dict1[key]
# print(result)

# set1 = {1, 2, 3, 'one', 'two'}
# set2 = {1, 2, 3, 'one', 'two', 100, 567}
# set3 = {1, 2, 3}
# set4 = {67, 90}
#
# print(set1.issubset(set3))
# print(set2.issuperset(set1))
# print(set1.intersection(set3))
# print(set2.difference(set3))
# print(set2.symmetric_difference(set4))
# print(set4.add(970))
# print(set4)
# set1.pop()
# print(set1)

# HW
# 3.1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# a = my_list[2]
# # # print(*a)
# a = [str(i) for i in a]
# print(', '.join(a))

# 3.2
# list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# i = 0
# result = 0
# while i < len(list_1):
#     try:
#         result += list_1[i]
#     except TypeError:
#         result += 0
#     i += 1
# print(result)
#
# i = 0
# result = 0
# while i < len(list_1):
#     try:
#         if list_1[i].find('a') != -1:
#             print(list_1[i])
#     except AttributeError:
#         result += list_1[i]
#     i += 1
# print(result)
# i = 0
# result = 0
# while i < len(list_1):
#     try:
#         if list_1[i].find('a') != -1:
#             print(list_1[i])
#     except AttributeError:
#         pass
#     i += 1

# 3.3
# my_list = ['cat', 'dog', 'horse', 'cow']
# print(tuple(my_list))

# 3.4
# family_1 = input('Please name all your older family members: ')
# family_2 = input('Please name all your younger family members: ')
# family_1 = family_1.split()
# family_2 = family_2.split()
# if len(family_1) > len(family_2):
#     print(*family_1)
# elif len(family_1) < len(family_2):
#     print(*family_2)
# else:
#     print('Equal')

# 3.5
# film_dict =  {
#     'title': 'Dune',
#     'director': 'Denis Villeneuve',
#     'year': 2021,
#     'budget': 165000000,
#     'main_actor': 'Timothee Chalamet',
#     'slogan': 'Beyond fear, destiny awaits'
# }
# print(film_dict.keys())
# for key in film_dict:
#     print(key)
# print(film_dict.values())
# for key in film_dict:
#     print(film_dict[key])
# for key in film_dict:
#     print(key)
# for value in film_dict.values():
#     print(value)
# print(film_dict.items())
# for i in film_dict.items():
#     print(i)
# for key, value in film_dict.items():
#     print(f'{key} - {value}')
# for key in film_dict:
#     print(f'{key} - {film_dict[key]}')

# 3.6
# my_dictionary = {
#     'num1': 375,
#     'num2': 567,
#     'num3': -37,
#     'num4': 21
# }
#
# print(sum(my_dictionary.values()))
# result = 0
# for key in my_dictionary:
#     result += my_dictionary[key]
# print(result)

# 3.7
# numbers = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(numbers))

# 3.8
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))

# Snail
# h = 0
# day = 1
#
# while h < 5:
#     print(day)
#     h += 3
#     if h < 5:
#         h -= 2
#     day += 1

# def find_needle(haystack):
#     return f'found the needle at position {haystack.index('needle') + 1}'


# NATO Phonetic Alphabet (retired)
#
# def nato(word):
#     phrase = []
#     for element in word:
#         phrase.append((LETTERS[element.capitalize()]))
#     return ' '.join(phrase)
#
# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end = ' ')
#     print()

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
#     print(counter)

# n = int(input())
# for i in range(n):
#     for j in range(1, 10):
#         print(f'{i + 1} + {j} = {i + 1 + j}', end = '\n')
#     print()

# n = int(input())
# for i in range(n // 2 + 1):
#     print('*' * (i + 1))
# counter = n // 2
# for j in range(n // 2):
#     print('*' * counter)
#     counter -= 1
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end = '')
#     print()

# from math import floor, ceil
# n = int(input('num: '))
# num1 = ceil(n / 2)
# num2 = floor(n / 2)
#
# for i in range(1, num1 + 1):
#     for _ in range(i):
#         print('*', end=' ')
#     print()
# for i in range(num2 + 1, 1, -1):
#     for _ in range(i - 1):
#         print('*', end=' ')
#     print()

# a, b, *_ = [1, 2, 8, 9]
# print(a, b)

# num = [1, 2, 8, 9]
# fam = ['mom', 'dad', 'granny', 'sister']
# gum = ['er', 3, 6, 'fgh']
# together = zip(num, fam, gum)
# print(list(together))

# for a, b, *_ in together:
#     print(a, b)
# for a, b, c in together:
#     print(a)

# num1 = [i*i*2 for i in num if i % 2]
# print(num1)

# num1 = num[:2]
# num2 = num[-3:]
# print(num1)
# print(num2)

# words = '   apple of banana   '
#
# for word in words.split():
#     if len(word) > 2:
#         words = words.replace(word, word.title())

# print(words)