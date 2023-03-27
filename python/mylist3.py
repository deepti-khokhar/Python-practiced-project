mylist=[23,12,34,56,21]
ele=55
flag=0

for i in mylist:
    if(i==ele):
        print("element found")
        flag=1
        break
if(flag==0):
    print("element not found")
