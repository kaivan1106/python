name="kaivan" #string is case sensitive

print(len(name)) #length of a string

print(name.endswith("van")) #true
print(name.endswith("nam")) #false

print(name.startswith("kai")) #true
print(name.startswith("jai")) #false

print(name.count("a")) #total no. of "a" in a string

print(name.capitalize()) #first character will be capital

print(name.upper()) #whole name will be in uppercase
print(name.lower()) #whole name will be in lowercase

s="hello world"
print(s.find("world")) #give the starting index of that word
print(s.replace("world","kaivan")) #replace the word world with kaivan
print(s.title()) #will capitalize firt character of all the words present in the string

a="    kaivan      taswala       "
print(a)
print(a.strip()) #strip will remove all the leading and trailing whitespace
print(a.lstrip()) #remove leading soace
print(a.rstrip()) #remove trailing space

b="42"
print(b.zfill(5)) #length of b is 2 but we wrote 5 in zfill() so 3 spaces are extra and that will be fill by 0 in left

