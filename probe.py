
from audioop import add
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
my_list=[]
for i in range(3):
    my_list.append(random.choice(my_favorite_songs)) 
k = 0
for name,time in my_list:
    
    k+=time
print(my_list)   
print(k)
           



