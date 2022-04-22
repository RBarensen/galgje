print("Welcome to Python galgje")
usertext = input("What is your name? ")
print("Hello", usertext)

print("What do you want to do?")

print("-Start")
print("-Instructions")
print("-Options")

inp = input("Enter a word:")
if inp == "Start":
  print("Alright, let's begin then!")
elif inp == "Instructions":
  print("Before the game starts, you can choose the options of the game. You can choose the length of the word you have to guess. Once you presses play, you have 8 tries to guess the right word, by choosing diffrent types of letters. If the letter is found in the word, it will be put on the dots. If the letter is not in the word, than the start of a picture will be drawn. If the picture is completed before you have finished the word than you lose. Have you guessed the word, than you win.")
elif inp == 3:
    inp = "spam"
else:
    print("Invalid input!")