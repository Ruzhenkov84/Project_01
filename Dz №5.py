n = 5
arr =[] 
for i in range(n):
    arr.append(randint(1,1000))
for i in range(n-1):
    for k in range(n-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("min = ",arr[1]) 

print("max = ",arr [n-1])

song=[]
for i in range(3):
    song.append(random.choice(list(my_favorite_songs)))
print(song)
k=0
for name,time in song:
    k+=time
    print(sum(k))

