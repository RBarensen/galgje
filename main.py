print("Welcome to Python galgje")
usertext = input("What is your name? ")
print("Hello", usertext)

print("What do you want to do?")

print("-Start")
print("-Instructions")
print("-Options")

inp = input("Enter a word:")
if inp == "Start":
  print("Alrtight, let's begin then!")
elif inp == 2:
    inp = "bar"
elif inp == 3:
    inp = "spam"
else:
    print("Invalid input!")