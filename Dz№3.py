# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите номер месяца: ")
month = int(user_input)

if month == 2: 
    print ('В этом месяце 28 дней')
    
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("В этом месяце 30 дней") 

# elif month == 1 and 3 and 5 and 7 and 8 and 10 and 12:
elif month in [1,3,5,7,8,10,12]:
    print("В этом месяце 31 день")
    
else:
    print("Номер месяца не корректен")

#     Можно еще так
# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))
