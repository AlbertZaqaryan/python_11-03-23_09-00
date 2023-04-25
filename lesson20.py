# number = {
#    '1' : '.,?;',
#    '2' : 'ABC',
#    '3' : 'DEF',
#    '4' : 'GHI',
#    '5' : 'JKL',
#    '6' : 'MNO',
#    '7': 'PQRS',
#    '8' : 'TUV',
#    '9' : 'WXYZ',
#    '10' : ' ',
# }

# text = 'PYTHON'
# for i in text:
#     for j in number:
#         if i in number[j]:
#             print(j * (number[j].index(i) + 1), end='')


# import random
# from pprint import pprint

# bingo = {
#     'B':[random.randint(1, 15) for _ in range(5)],
#     'I':[random.randint(16, 30) for _ in range(5)],
#     'N':[random.randint(31, 45) for _ in range(5)],
#     'G':[random.randint(46, 60) for _ in range(5)],
#     'O':[random.randint(61, 75) for _ in range(5)]
# }

# count_x = True
# while count_x:
#     user_input = input('Enter for generate new number!!')
#     new_number = random.randint(1, 75)
#     for i in bingo:
#         if new_number in bingo[i]:
#             bingo[i][bingo[i].index(new_number)] = 'X'
#             print(i)
#         if bingo[i].count('X') == 5:
#             count_x = False
#             print('---------------- END GAME --------------------')
#     pprint(bingo)


# ------------------------- SET ---------------------------
# set1 = {}
# print(type(set1))


# set1 = set()
# print(type(set1))


# set1 = {1, 7, 4, 5, 8, 1, 2, 2, 1}
# print(set1)


# mylist = [7, 4, 4, 4, 5, 8, 9, 6, 1, 2, 3, 1, 4]
# print(list(set(mylist)))

# myset1 = {1, 7, 4, 5, 6, 9}
# myset2 = {0, 4, 21}
# print(myset2.issubset(myset1))
# print(myset1.issuperset(myset2))
# print(myset1.isdisjoint(myset2))
# myset1.add(100)
# print(myset1)
# myset1.discard(5)
# print(myset1)
# -----------------------------------------------------------------




