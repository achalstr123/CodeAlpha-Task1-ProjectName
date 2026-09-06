
# print("=" * 40)
# print("      🍽️ WELCOME TO  AG Resturent 🍽️")
# print("=" * 40)

# menu = {
#     "1": ("Paneer Butter Masala", 220),
#     "2": ("Veg Biryani", 180),
#     "3": ("Masala Dosa", 120),
#     "4": ("Veg Burger", 90),
#     "5": ("Pizza", 250),
#     "6": ("Cold Drink", 50),
#     "7": ("Ice Cream", 80)
# }

# print("\n--------- MENU CARD ---------")
# for key, value in menu.items():
#     print(f"{key}. {value[0]:25} ₹{value[1]}")

# total = 0

# while True:
#     choice = input("\nEnter Item Number (1-7): ")

#     if choice in menu:
#         qty = int(input("Enter Quantity: "))
#         amount = menu[choice][1] * qty
#         total += amount
#         print(f"{menu[choice][0]} Added! Amount = ₹{amount}")
#     else:
#         print("Invalid Item Number!")

#     more = input("Do you want to order more? (yes/no): ").lower()
#     if more != "yes":
#         break

# print("\n" + "=" * 40)
# print("           FINAL BILL")
# print("=" * 40)
# print(f"Total Amount = ₹{total}")
# print("🙏 Thank You! Visit Again 🙏")
# print("=" * 40)

# file = open("students.txt", "r")

# import argparse

# parser = argparse.ArgumentParser(description="Simple Command Line Utility")

# parser.add_argument("--name",help="Enter your name")

# args = parser.parse_args()

# if args.name:
#     print(f"Hello, {args.name}!")
# else:
#     print("Hello, World!")

# number=["Achal singh"]
# while(n:=len(number))>0:
#     print(number.pop())

# def reverse_string(s):
#     return s[::-1]

# text = input("Enter a string: ")

# print("Reversed String:", reverse_string(text))

# def palindrome(s):
#     s = s.lower()

#     if s == s[::-1]:
#         return True
#     else:
#         return False

# text = input("Enter String: ")

# if palindrome(text):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# arr=[10,20,30,40]
# arr.pop(2)
# # print(arr)
# arr.append(5)
# arr.sort()
# print(arr) 

# position =2
# value=25
# new=[0]*((len(arr))-1)
# for i in range(position):
#     new[i]=arr[i]
# new[position]=value

# for i in range(position,len(arr)):
#     new[i-1]=arr[i]
# print(new)        

# position =2
# value=25
# arr.pop(2)
# new=[0]*((len(arr))+1)
# for i in range(position):
#     new[i]=arr[i]
# new[position]=value

# for i in range(position,len(arr)):
#     new[i+1]=arr[i]
# print(new)        
# print(arr)
# arr=[?]
# print(max(arr))
# print(min(arr))
# arr.reverse()
# print(arr)
# print(sum(arr))
# arr=list(set(arr))
# arr.sort()
# print(arr[-4])

# students = []

# name = input("Enter Student Name: ")

# students.append(name)

# print(students)

# import time           #present time,day,date ke liye hai 
# print(time.ctime())

# import time
# for i in range(5, 0, -1):   #timer counter 
#     print(i)
#     time.sleep(1)

# print("Time Up!")
#PF-Tryout
#Creating a dictionary
# crew_details={
#             "Pilot":"Kumar",
#             "Co-Pilot":"Raghav",
#             "Head-Strewardess":"Malini",
#             "Stewardess":"Mala"
# }
# print(crew_details["Pilot"])

# print("\nIterating the dictionary using items function")
# for key,value in crew_details.items():
#     print(key,":",value)


# #Usually while working with dictionary, you will be interested in specific values. 
# #Let’s find the value of all pilots from crew_details.
# print("\nIterating the dictionary using keyword 'in'")
# for key in crew_details:
#     if(key=="Pilot" or key=="Co-Pilot"):
#         print(crew_details[key])
# #Note: Dictionary being unordered, the order of the values being displayed may vary during each execution of the above for loop.

# #Dictionaries are mutable
# crew_details["Pilot"]="James" # Here the value for key "Pilot" is being updated to "James"
# print("\nAfter modifying the value of Pilot:", crew_details["Pilot"])

# print("------------------------------------------------------------------")
# print("Before update:")
# # Usage of get method()
# print("Co-pilot:",crew_details.get("Co-Pilot"))

# #Usage of update method()
# crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})

# print("\nAfter update:")
# print("Co-pilot:",crew_details.get("Co-pilot"))
# print("Flight Attendant:",crew_details["Flight Attendant"])
#---------------------------------------------------------------------very important
# numbers=[10,20,30,40,50,60]
# print(numbers[:3])     # first 3
# print(numbers[2:])     # index 2 se end tak
# print(numbers[:])      # complete list
# print(numbers[::2])    # every second element
                                                    
# numbers=[10,20,30,40,50,60]
# numbers.insert(1,100) //insert krne ke liye hai koi bhi strings ho
# print(numbers)

# a=[1,2,3,4]
# b=[5,7,9,10]
# a.extend(b)      //extend ka matlab hai ki dono string ko combine kr deta hai
# print(a)

# n=[25,38,10,45,60,70]
# n.sort()   //ka matalb hai ki accending order me likhta hai
# print(n)

# n=[25,38,10,45,60,70]
# n.sort(reverse=True)  // ka matalb hai ki decending order me
# print(n)

#------------------------------------------------------------------------------------Imp for data analytics
# sale=[2400,3200,4999,1000]
# total=0
# for i in sale:
#     total+= i
# print("Total=",total)   
#+=================================================================================================================================================
 
                   #=====================Hangman Game=============

import random
words = ["python", "computer", "programming", "hangman", "developer"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_wrong_guesses - wrong_guesses}")
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)
