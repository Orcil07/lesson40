first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для первого примера:
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для второго примера:
second_result = (len(first[i]) != len(second[i]) for i in range(len(first)))


print(list(first_result))   
print(list(second_result))