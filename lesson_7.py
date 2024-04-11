# def search_substr(substr, st):
#     if substr.upper().issubset(st.upper()):
#         return 'Есть контакт!'
#     return 'Мимо!'

def search_substr(substr, st):
        return 'Есть контакт!' if substr.upper() in st.upper() else 'Мимо!'

# print(search_substr('dr', 'Pod6uga'))

# def first_last(letter, st):
#         if not letter in st:
#                 return (None, None)
#         l = []
#         for index, i in enumerate(st):
#                 if i == letter:
#                         l.append(index)
#         print(l)
#         return (l[0], l[-1])

# def first_last(letter, st):
#         index_1 = st.find(letter)
#         if index_1 < 0:
#                 return (None, None)
#         index_2 = st.rfind(letter)
#         return (index_1, index_2)
#
# print(first_last('u', 'hello'))

# def remover(st):
#         l = []
#         l_2 = []
#         for index, i in enumerate(st):
#                 l.append(index)
#                 if i == '@':
#                         l_2.append(index - 1)
#                         l_2.append(index)
#         l_3 = list(set(l_2).symmetric_difference(set(l)))
#         word = ''
#         for i in l_3:
#                 word += st[i]
#         return word

def remover(st):
        l = []
        for i in st:
                if i != '@':
                        l.append(i)
                else:
                        l.pop()
        return ''.join(l)

print(remover('прин@н@вел@т'))


