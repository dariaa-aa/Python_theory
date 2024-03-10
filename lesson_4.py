# name = 'Alice'
# def outer_func():
#     name = 'Alex'
#     def inner_func():
#         name = 'Albert'
#         return name
#     return inner_func
#
# # enclosure = outer_func()
# # print(outer_func()())
#
# def name():
#     # def name_1():
#     #     return 'Steven'
#     print('Alice')
#     # return name_1
#
# print(name()())

# def decorator_function(func):
#     def wrapper(*arg):
#         print('Wrapper function')
#         print(f'Wrapped function: {func.__name__}')
#         print(func(*arg))
#         print('Exiting wrapper function')
#     return wrapper
#
# @decorator_function
# def my_wrapper(item):
#     return f'{item} is wrapped!'
#
# my_wrapper('Dasha')
#
# @decorator_function
# def hello(name):
#     return f'My name is {name}'
#
# hello('Dasha')

# import math
# arr = [1, 5, 8, 9, 10, 25]
# result = math.prod(arr)
# print(result)

# import math as m
# arr = [1, 5, 8, 9, 10, 25]
# result = m.prod(arr)
# print(result)

# from math import prod
# arr = [1, 5, 8, 9, 10, 25]
# result = prod(arr)
# print(result)

# from math import *
# arr = [1, 5, 8, 9, 10, 25]
# result = prod(arr)
# print(result)

# import datetime
# birth_year = 1985
# current_date = datetime.date.today()
# current_age = current_date.year - birth_year
# print(current_date)
# print(current_age)

# def introduce(**kwargs):
#     print(type(kwargs))
#     # for key in kwargs:
#     #     print(f'{key} - {kwargs[key]}')
#     print(*kwargs)
#
# introduce(name='Anna', lname='Petrova', position='QA')

# def my_sum(*arg):
#     print(sum(arg))
#     print(arg)
#     print(*arg)
#
# my_sum(2, 6, 7)

# summ = lambda x, y: x * y
# print(summ(2, 5))

# def take_even(num):
#     if not num % 2:
#         return True
#     return False
#
# l = [1, 5, 8, 12, 15]
# # even = [x for x in l if not x % 2]
# # print(even)
# new_list = list(filter(lambda x: x % 2, l))
# # new_list1 = list(filter(take_even, l))
# # print(new_list)
# print(new_list1)

# my_list = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
# my_list_a = list(filter(lambda x: 'a' in str(x), my_list))
# print(my_list_a)

# HW
# 4.1
# def square(a):
#     per = 4 * a
#     sq = a * a
#     diag = 2**(1/2) * a
#     # my_list = [per, sq, diag]
#     # return tuple(my_list)
#     return (per, sq, round(diag, 2))
# print(square(9))

# 4.2
# def words(**kwargs):
#     for key in kwargs:
#         print(f'{key}: {kwargs[key]}')
#
# words(name='Dasha', age=5, lname='Pod')

# 4.3
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)

# 4.4
# import functools
# # import math
# my_list = [20, -3, 15, 2, -1, -21]
# res = functools.reduce(lambda x, y: x * y, my_list)
# # result = math.prod(my_list)
# print(res)
# # print(result)
# print(functools.reduce(lambda x, y: x * y, list(filter(lambda x: x > 0, my_list))))
# # print(functools.reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))


# 4.5
import datetime
# import time
# def decorator_function(func):
#     def wrapper(*arg):
#         time_1 = time.time()
#         # print(time_1)
#         # print(func(*arg))
#         (func(*arg))
#         # result = (func(*arg))
#         time_2 = time.time()
#         # print(time_2)
#         print(f'It took {(time_2 - time_1)} seconds for function to complete')
#         # return result
#     return wrapper
#
# @decorator_function
# def hello(name):
#     name = name * 6700000
#     return f'Hello {name}'
#
# hello('Dasha')

# time_1 = datetime.datetime.now().time()
# time_2 = time.time()
# print(time_2)

# 4.6
# import my_calc
#
# print(my_calc.summ(2, 67, 567))
# print(my_calc.div__(475, 9))
# print(my_calc.division(567, 89))
# print(my_calc.div_(67, 2))

# my_list = ['i', 'have','no','space']
# for i in range(2):
#     print(''.join(my_list[:i+1]))

# arr = ["a","cat"]
# phrase = ''
# i = 0
# while i < max(len(arr[0]), len(arr[1])):
#     try:
#         phrase += f'{arr[0][i]} '
#     except IndexError:
#         phrase += ''
#     try:
#         phrase += f'{arr[1][i]}\n '
#     except IndexError:
#         phrase += ' '
#     i += 1
#
# phrase = list(phrase)
# if phrase[-1] == '\n' or ' ':
#     phrase.pop(-1)
# if phrase[-1] == '\n' or ' ':
#     phrase.pop(-1)
# print(phrase)

# def palindrom(word):
    # if len(word) % 2:
    #     return 'another word'
    # else:
    #     word1 = word[0:int(len(word) / 2)]
    #     word2 = word[:int(len(word) / 2 - 1):-1]
    # return 'yes' if word1 == word2 else 'no'
    # word1 = [i.lower() for i in word if i.isalpha()]
    # return word1 == word1[::-1]


# print(palindrom('fbdFGAF И ВА'))

# starts_with = lambda word: word.startswith('W')
# print(starts_with('lkjnhb '))

# devide_13 = lambda num: num % 13 == 0 or num % 19 == 0
# print(devide_13(19))

# num = [-100, -56, - 87, -3, -7, - 124, 0, -56, 5678, 32, 0, 12, 4, -89, 34, 65, 0, 23, 6, 78, -98, 569]
# neg_list = list(filter(lambda x: x < 0, num))
# zero_list = list(filter(lambda x: x == 0, num))
# pos_list = list(filter(lambda x: x > 0, num))
# num_sorted = sorted(num, key=lambda x: (x % 2 == 0, x))
#
# # print(len(neg_list), len(zero_list), len(pos_list))
# print(num_sorted)

# a = '1 2 3 4 5 6'
# a1 = a.split()
# # a2 = [int(x) for x in a1]
# a2 = list(map(int, a1))
# print(a2)

# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# days_new = sorted(list(filter(lambda x: len(x) == 4 or x.startswith('S'), days)))
# print(days_new)

# numbers = [12, 7, 86, 3, 5, 2, 8]
# numbers_new = list(map(lambda x: x * 3, numbers))
# print(numbers_new)

# def text_dec(func):
#     def dec(*args, **kwargs):
#         print('Hello')
#         func(*args, **kwargs)
#         print('Goodbye')
#     return dec
#
# @text_dec
# def simple_func():
#     print('I am very simple function')
#
# simple_func()

# def mother(z):
#     y = 20
#
#     def son(x):
#         print(x, y, z)
#     return son
#
# a = mother(5)
# a(1)

# def decorator(func):
#     def wrapper(*args):
#         print('Beginning')
#         res = func(*args)
#         print('Ending')
#         return res
#     return wrapper
#
# @decorator
# def add(a, b):
#     return a + b
#
# print(add(1, 4))

# def get_count(sentence):
#     return sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
#
# print(get_count('aeiou'))

# a = 'abcdeb'
# print(a.split('b'))

def encode(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     alphabet_cap = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    result = ''
    for i in string:
        if i.lower() in alphabet:
            result += str(alphabet.index(i.lower()) + 1)
        else:
            result += i
    return result

print(encode('ZzzzZ'))

def make_backronym(acronym):
    phrase = []
    for i in acronym:
        print(i)
        print()
        phrase += dictionary[i.upper()]
    return ' '.join(phrase)