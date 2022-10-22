user_input = input("Введите номер месяца: ")
month = int(user_input)
if month == 2: 
    print ('В этом месяце 28 дней')
    
elif month == 4 and 6 and 9 and 11:
    print("В этом месяце 30 дней") 

elif month == 1 and 3 and 5 and 7 and 8 and 10 and 12:
    print("В этом месяце 31 день")
    
else:
    print("Номер месяца не корректен")