#1

#defining a functions
# def print_codanics():
#      print("We are learning with ammar")
#      print("We are learning with ammar")
#      print("We are learning with ammar")
    
# print_codanics()

#2
# def print_code():
#     text= "we are learning python with ammar "
#     print(text)
#     print(text)
#     print(text)

# print_code()

#3
# def print_code(text):
#     print(text)
#     print(text)
#     print(text)

# print_code("We are learning python")

#4
#defining a function with if elif and else statement

# def school_calculator(age):
#     if age==5:
#         print("Hammad can join the school")
#     elif age>5:
#         print("Hammad should go to higher school")
#     else:
#         print("Hammad is still a baby")

# school_calculator(5)

#defining a function of future 
# def future_age(age):
#     new_age= age+20
#     return new_age
#     print(new_age)
#     # print(new_age)
# furture_age=future_age(3)
# print(furture_age)

#i understand functions really well

# def repeat_ali_4times():
#     text= ("ALI")
#     print(text)
#     print(text)
#     print(text)
#     print(text)

# repeat_ali_4times()


#practice again 
# text= input("what do you want to write 5 times")
# def write_4_times(text):
#     print(text)
#     print(text)
#     print(text)
#     print(text)

# write_4_times(text)
name=input("What is your name? ")
age=int(input("What is your age ? "))
greetings= ("Hello")

def school_extrance_calculator(age):
    print(greetings,name)
    if age>=5 and age<9:
        print("You are welcome to school")
    elif age<5:
        print("You are not eligible")
    elif age>=10 and age<15:
        print("You should go to higher school")
    else:
        print("you should go to university")

school_extrance_calculator(age)
