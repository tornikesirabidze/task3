name= "tornike"
surname="sirabidze"
age=20
age+=3
my_sentence="სახელი " "{} გვარი " "{} ასაკი ""{} " .format(name, surname, age )
print(my_sentence)
my_name=input("enter your name:  ")
my_surname=input("enter your surname:  ")
my_age=int(input("ener your age:  "))
print("my name is {} my surname is {} my age is {}".format(my_name, my_surname, my_age)) 
my_age+=5
print("after 5 years im now {} yers old ".format(my_age))

number1=int(input("raime ricxvi : "))
number2=int(input("raime ricxvi : "))
product= number1*number2 
if product >100:
    print(product)
else:print( "you lose") 
