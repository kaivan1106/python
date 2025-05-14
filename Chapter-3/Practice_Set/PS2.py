#write a program to fill in a letter template given below with name and date
letter = '''Dear <|name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|name|>","kaivan").replace("<|Date|>","20 December, 2024"))
