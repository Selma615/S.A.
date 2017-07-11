# testing.. OKAY WERE GOOD! :)
# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
Name = raw_input("enter your name: ")
Birthday = raw_input('did your birthday happen?:')
Age = raw_input("enter your age:")
Age = int(Age)
if Birthday == "no":
 Age= Age + 1
else:
 Age + 0
birthyear= 2017 - Age
year = birthyear + 100
print year
raw_input("is when you will turn 100! ")