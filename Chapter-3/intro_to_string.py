name="kai"
#string is immutable so we can't change any particular index of the string
print(name)
name="kaivan" #if we want to change string than we have to change whole string, we can't change particular index
print(name)
#name[0]='j' if we will try to do this than it will give error that 'str' object does not support item assignment

length = len(name)
print("lenght : ",length)

shortName = name[0:3] #this means that we will start from index 0 and end with index 3 but excluding 3
#index 3 will not be included so shortname will be kai
print(shortName)