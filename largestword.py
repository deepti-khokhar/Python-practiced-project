# import 
# s = sorted(s, key = len)
 
    
# print(s[-1])
 

# if __name__ == "__main__":
 
#     # Given string
#     s = "be confident and be yourself"
 
#     # Split the string into words
#     l = list(s.split(" "))
 
# largestWord(l)
import keyword


# mystring=input("enter any sentence ")
# word_mystring=mystring.split()
# word_mystring=max(mystring,len=keyword)
# print("the max word in the string",word_mystring)
# pos=word_mystring.index(word_mystring)
# print("the index position of the string",word_mystring)

# def find_longest_word(word_list):  
#     longest_word = ''  
       

# words = input('Please enter a few words')  
# word_list = words.split()  
# find_longest_word(word_list)
str=input("enter any string")
s=str.split()
print("thr rlement splitting ",s)
max=0
for ele in s:
    if len(ele)>max:
        max=len(ele)
        max_word=ele
print("the longest word in the string is",max_word)
print("the length of the element is",len(max_word))