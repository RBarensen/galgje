import random

woorden = ["champion", "eagles", "promise", "stripes", "pavement", "motorcycle", "square", "mountain", "waterfall",]
galg = [
  "---------",
  "|       |",
  "|       O",
  "|       |",
  "|      -+-",
  "|       |",
  "|      / \\",
  "|",
  "|",
  "------------"
]

print("Welcome to Python galgje")
usertext = input("What is your name? ")
print("Hello", usertext)

def speel():
   woordkeuze = random.choice(woorden) 
   woord = (woordkeuze)
   pogingen =' '
   beurten = 10
   while beurten > 0:
     lettersover = 0
     geradenwoord =' '
     for char in woord:
       if char in pogingen:
         geradenwoord=geradenwoord + (char)
       else:
         geradenwoord=geradenwoord+ ('_')
         lettersover += 1
     print ('Word:',geradenwoord, '.Letters that have already been guessed:', pogingen)                             
     if lettersover == 0:
       print("You have won!")
       opnieuwwin=str(input("Play again? Type yes or no"))
       if opnieuwwin == "no":
        print("Thanks for playing")
        exit()
       elif opnieuwwin == "yes":
        speel()
         
     print 
     poging = input ('Guess the letter:')

     pogingen += poging
     if poging not in woord:
       beurten -= 1
      
       galglayout = beurten
       levens=(10-beurten)
       while levens>0:
         print (galg[galglayout])
         galglayout +=1
         levens -=1
       print ("")

       print ("Unfortunately, that is wrong!")
       print ('You have', + beurten, 'lives left')
       if beurten == 0:
         print ('Too bad!', usertext, 'You have lost!, the word was:', woord)
         opnieuwverlies=str(input("Play again? Type yes or no"))
         if opnieuwverlies == "no":
           print("Thanks for playing")
           exit()
         elif opnieuwverlies == "yes":
           speel()

print("What do you want to do?")

print("-to start, type: Start")
print("-to show the instructions, type: Instructions")


inp = input("Enter a word:")
if inp == "Start":
  print("Alright, let's begin then!")
  speel()
  
     
elif inp == "Instructions":
 print("Before the game starts, you can choose the options of the game. You can choose the length of the word you have to guess. Once you presses play, you have 10 tries to guess the right word, by choosing diffrent types of letters. If the letter is found in the word, it will be put on the dots. If the letter is not in the word, than the start of a picture will be drawn. If the picture is completed before you have finished the word than you lose. Have you guessed the word, than you win. Is that clear?") 
 antwoord = input("yes / no")
 if antwoord == "yes":
  print("Let's start the game then!")
  speel()
 elif antwoord == "no":
  print("Here are the instructions again")
  print("Before the game starts, you can choose the options of the game. You can choose the length of the word you have to guess. Once you presses play, you have 8 tries to guess the right word, by choosing diffrent types of letters. If the letter is found in the word, it will be put on the dots. If the letter is not in the word, than the start of a picture will be drawn. If the picture is completed before you have finished the word than you lose. Have you guessed the word, than you win.")
  print ("Now, let's start the game!")
  speel()
 

 