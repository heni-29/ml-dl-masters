num = list(range(2000, 3201))
for i in num:
    if (i % 5 != 0) & (i % 7 == 0):
        print(i, end=',')