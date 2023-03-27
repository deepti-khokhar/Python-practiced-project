letter = '''Dear <|name|>
You are selected 
<|Date|>'''
name = input("enter your name \n")
date = input("enter the date \n")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)