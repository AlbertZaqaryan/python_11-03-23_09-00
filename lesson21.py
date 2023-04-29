# ----------------------------------------------------
# def ordinalDate(d, m, y):
#     day_count = 0
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     for i in range(m - 1):
#         day_count += days[i]
#     day_count += d
#     if y % 4 == 0 and y % 400 == 0 and y % 100 != 0:
#         day_count += 1
#     return day_count

# print(ordinalDate(17, 3, 2000))
# ----------------------------------------------------
# def func(y, day_count):
#     if y % 4 == 0:
#         days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     else:
#         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     m = 1
#     while day_count > days[0]:
#         day_count -= days[0]
#         m += 1
#         days.pop(0)
#     return f'{y}-{m}-{day_count}'
# print(func(2025, 60))
# ----------------------------------------------------
def prime_number(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def next_prime_number(mynumber):
    while True:
        if prime_number(mynumber):
            return mynumber
        else:
            mynumber += 1

print(next_prime_number(int(input('Enter number: '))))
