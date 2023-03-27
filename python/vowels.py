s=input("enter any string")
vowels=set("aeiou")
count=0
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)
