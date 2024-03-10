# x = 5
# print(x <= 10)

# num = 3
# if num == 5:
#     print('Five!')
# elif num < 5:
#     print('Less than five')
# else:
#     print('More than five')

# for i in range(1, 11):
#     print(i)

# for i in reversed(range(0, 11, 2)):
#     print(i)
# print('HAPPY NEW YEAR!')

# word = 'pizza'
# # print(word.find('z'))
#
# # for symbol in word:
# #     print(f'{word.find(symbol)} - {symbol}')
# #
# # print(word[4])
#
# for i, s in enumerate(word):
#     print(f'{i} - {s}')
#
# test = ''
# test_1 = []
# test_2 = {}
# test_3 = 0
# test_4 = 0.0
# test_5 = None
# test_6 = ()
# print(bool(test_5))

# def sum_it(x, y):
#     result = x + y
#     return result
#
#
# print(sum_it(3, 7))
#
# a = sum_it(6, 98765)
# print(a)

# HW
# # 2.1
# health = int(input('Please enter a number: '))
# if health <= 0:
#     print('False')
# else:
#     print('True')

# 2.2
# num = int(input('Please enter a number: '))
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
# # или
# if num % 2:
#     print('Нечетное')
# else:
#     print('Четное')

# 2.3
# year = int(input('Введите год: '))
# if year > 0:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print('Год високосный')
#     else:
#         print('Год невисокосный')
# else:
#     print('Введите корректный год (больше 0)')

# 2.4
# text = input('Please enter something: ')
# num = int(input('Please enter a number: '))
# if num > 0:
#     for i in range(num):
#         print(text)
# else:
#     print('Number should be more than 0')

# 2.5
# num1 = int(input('Please enter a number: '))
# num2 = int(input('Please enter a number: '))
# op = input('Please choose an operation (+, -, *, /, //, %, **): ')
# if op == '+':
#     print(f'{num1} {op} {num2} = {num1 + num2}')
# elif op == '-':
#     print(f'{num1} {op} {num2} = {num1 - num2}')
# elif op == '*':
#     print(f'{num1} {op} {num2} = {num1 * num2}')
# elif op == '**':
#     print(f'{num1} {op} {num2} = {num1 ** num2}')
# elif op == '/':
#     if num2 != 0:
#         print(f'{num1} {op} {num2} = {num1 / num2}')
#     else:
#         print('No division by zero')
# elif op == '%':
#     if num2 != 0:
#         print(f'{num1} {op} {num2} = {num1 % num2}')
#     else:
#         print('No division by zero')
# elif op == '//':
#     if num2 != 0:
#         print(f'{num1} {op} {num2} = {num1 // num2}')
#     else:
#         print('No division by zero')

# num1 = int(input('Please enter a number: '))
# num2 = int(input('Please enter a number: '))
# op = input('Please choose an operation (+, -, *, /, //, %, **): ')
# if num2 == 0:
#     if op == '/':
#         try:
#             num1 / num2
#         except ZeroDivisionError:
#             print('No division by zero')
#     elif op == '//':
#         try:
#             num1 // num2
#         except ZeroDivisionError:
#             print('No division by zero')
#     elif op == '%':
#         try:
#             num1 % num2
#         except ZeroDivisionError:
#             print('No division by zero')
# else:
#     if op == '+':
#         print(f'{num1} {op} {num2} = {num1 + num2}')
#     elif op == '-':
#         print(f'{num1} {op} {num2} = {num1 - num2}')
#     elif op == '*':
#         print(f'{num1} {op} {num2} = {num1 * num2}')
#     elif op == '**':
#         print(f'{num1} {op} {num2} = {num1 ** num2}')
#     elif op == '/':
#         print(f'{num1} {op} {num2} = {num1 / num2}')
#     elif op == '%':
#         print(f'{num1} {op} {num2} = {num1 % num2}')
#     elif op == '//':
#         print(f'{num1} {op} {num2} = {num1 // num2}')

# num1  = int(input('Please enter a number: '))
# num2 = int(input('Please enter a number: '))
# op = input('Please choose an operation (+, -, *, /, //, %, **): ')
# if num2 == 0 and op == '/' or op == '//' or op == '%':
#     try:
#         num1 / num2
#     except ZeroDivisionError:
#         print('No division by zero')
# else:
#     if op == '+':
#         print(f'{num1} {op} {num2} = {num1 + num2}')
#     elif op == '-':
#         print(f'{num1} {op} {num2} = {num1 - num2}')
#     elif op == '*':
#         print(f'{num1} {op} {num2} = {num1 * num2}')
#     elif op == '**':
#         print(f'{num1} {op} {num2} = {num1 ** num2}')
#     elif op == '/':
#         print(f'{num1} {op} {num2} = {num1 / num2}')
#     elif op == '%':
#         print(f'{num1} {op} {num2} = {num1 % num2}')
#     elif op == '//':
#         print(f'{num1} {op} {num2} = {num1 // num2}')

# def pipe_fix(nums):
#     i = 0
#     while i < (nums[len(nums) - 1] - nums[0]):
#         if nums[i] != nums[i + 1] - 1:
#             nums.insert(i + 1, nums[i] + 1)
#         i += 1
#     return nums

# def pipe_fix(nums):
#     return [*range(nums[0], nums[len(nums) - 1] + 1)]
# def pipe_fix(nums):
#     return list(range(nums[0], nums[-1] + 1))
#
# num = [6, 12]
# print(pipe_fix(num))

# def split_and_merge(string_, separator):
#
#     def elements(chain, separator):
#         chain = string_.split()
#         i = 0
#         while i < len(chain):
#             chain[i] = separator.join(chain[i])
#             i += 1
#         return chain
#
#     return ' '.join(elements(string_, separator))
#
# print(split_and_merge('Hello Pook Look', '.'))

n = 2
m = 9
def sum_mul(n, m):
    if  n > 0 and m > 0:
        if n == m or n > m:
            return 0
        else:
            i = 1
            sum_1 = 0
            for i in range(n, m, i * n):
                sum_1 += i
            return sum_1
    else:
        return 'INVALID'
print(sum_mul(n, m))

# def who_is_paying(name):
#     return [name] if len(name) <= 2 else [name, name[0:2]]
#
# print(who_is_paying('dasha'))

# class_points = [41, 75, 72, 56, 80, 82, 81, 33]
# print(sum(class_points))

# x = "45385593107843568"
# def fake_bin(x):
#     i = 0
#     result = ''
#     while i < len(x):
#         if int(x[i]) < 5:
#             result += '0'
#         else:
#             result += '1'
#         i += 1
#     return result

# s = ''
# def string_to_array(s):
#     '''
#     this is a comment for this function
#     '''
#     return s.split(" ")
# print(string_to_array(s))

