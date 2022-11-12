# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
    }
song=[]
for i in range(3):
    song.append(random.choice(list(my_favorite_songs.items())))
k = 0
for name,time in song:
    k+=time
print(song)   
print('Три песни звучат',(k), 'минут')

# Отлично
