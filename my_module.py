from random import randint

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



