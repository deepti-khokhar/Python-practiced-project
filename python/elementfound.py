mylist=[23,21,22,44,23,89,23,89,23]
ele=23
count=0
 
for i in mylist:
    if(i==ele):
        count=count+1
print("{} element has occured {}".format(i,count))
