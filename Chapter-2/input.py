#whenever we will take input from a user, by default input type will be string
# a = input ("enter any number") here user will enter a no. but type of a will be string

a = input("enter number a : ")
b = input("enter number b : ")

print("number a : ",a) #let's assume a = 5
print("number b : ",b) #let's assume b = 7
print("a + b : ", a+b) # so addition of this two value should be 12 but it will be 57 because type of a and b is string and they will be concated

#so if you want to take input as a int than you need to do this
c = int(input("enter number c : "))
d = int(input("enter number d : "))

print("number c : ",c) #let's assume a = 5
print("number d : ",d) #let's assume b = 7
print("c + d : ", c+d) # so addition of this two value will be 12