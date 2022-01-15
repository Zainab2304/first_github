name= input("What is your name ? ")
print(name)
age= int(input("What is your age? "))
print(age)
print(type(age))

if age==24:
    print(name,"You are still young bro")
elif age<24:
    print(name, "Bachay you are still a baby")
elif age>24 and age<100:
    print(name ,"saab Babay ho rhe ho , shadi krwa lo")
elif age>=100 and age<200:
    print(name, "Mar ja bhai ") 
else:
    print("Tu mar chuka hai ")