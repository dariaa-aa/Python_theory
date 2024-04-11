# file_name = 'test_file'
#
# file = open(file_name, 'r', encoding='utf-8')
# content = file.read()
# content = file.readline()
# while content != '':
#     print(content.strip())
#     content = file.readline()
# for i in file:
#     print(i.strip())
# content = file.readlines()
# content_1 = [i.strip() for i in file.readlines()]
# content_2 = []
# for i in file:
#     content_2.append(i.strip())
# print(content_2)
# file.close()
import json

# file_name = 'test_file_1'
# # file = open(file_name, "w", encoding='utf-8')
# file = open(file_name, mode="a", encoding='utf-8')
# file.write('\nHello Hello')
# file.close()

# file_name = 'test_file_1'
# with open(file_name, mode='r', encoding='utf-8') as f:
#     content = [i.strip() for i in f.readlines()]
#
# for i in content:
#     print(i)
#
# file_name = 'words.txt'
#
# with open(file_name, mode='r', encoding='utf-8') as file:
#     lst = set()
#     for word in file:
#         word_1 = word.strip()
#         if word_1[-2:].upper() == 'ЕЯ':
#             lst.add(word_1.upper())
#
# for word in sorted(lst, key=lambda x: (len(x), x)):
#     print(word)

import json
import os.path

json_file = """
    {
        "key1": 1,
        "key2": 2    
    }
    """

# json.dumps() - преобразует объект в формат json
# json.dump() - преобразует объект в формат json и записывает в файл
#
# json.loads() - преобразует json-строку в питоновский объект
# json.load() - преобразует json-файл в питоновский объект

# json_file_1 = json.loads(json_file)
#
# print(type(json_file))
# print(type(json_file_1))
# for key, value in json_file_1.items():
#     print(key, value)
# print(json_file_1["key2"])

dct = {
    "name": "Dasha",
    "age": 23,
    "profession": "AQA"
}

dct_1 = json.dumps(dct)
print(type(dct))
print(type(dct_1))

def return_file_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    return file_path

file_name_3 = 'json.json'
path = return_file_path(file_name_3)

with open(path, 'w') as f:
    json.dump(dct, f)

with open(path, 'r') as f_1:
    a = json.load(f_1)

# print(a)

