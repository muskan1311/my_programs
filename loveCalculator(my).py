# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

j = 0
z = 0
for i in name1.upper()+name2.upper():
    if i in "TRUE":
        j= j+1
        # print(j)
    if i in "LOVE":
        z +=1
        # print(z)

x= int(str(j)+ str(z))   
if x<10 or x>90:   
   print(f"Your score is {x}, you go together like coke and mentos.")  
elif x>=40 and x<=50:
    print(f"Your score is {x}, you are alright together.")
else:
    print(f"Your score is {x}.")


