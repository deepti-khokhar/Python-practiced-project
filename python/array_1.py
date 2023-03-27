#arr=[1,2,3,4,5]
#print(sum(arr,89))
arr=[6,9,6,2,89,34,23,98,45,22]
max=arr[0]
min=arr[0]
for i in range (1,10):
    if arr[i]>max:
     max=arr[i]
print(max)
if arr[i]<min:
    min=arr[i]
print(min)