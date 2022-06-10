import random

woorden = ["champion", "eagles", "promise", "stripes", "pavement", "motorcycle", "square", "mountain", "waterfall", "NIGGERS"]
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

print("What do you want to do?")

print("-to start, type: Start")
print("-to show the instructions, type: Instructions")


inp = input("Enter a word:")
if inp == "Start":
  print("Alright, let's begin then!")
  speel = True 
  while speel:
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
       opnieuw=str(input("Play again? Type yes or no"))
       if opnieuw == "no":
        speel = False
        break
       else:
         speel = True
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
       print ('You still have', + beurten, 'lives')
       if beurten == 0:
         print ('Too bad!', usertext, 'You have lost!, the word was:', woord)
         opnieuw=str(input("Play again? Type yes or no"))  
         if opnieuw == "no":
          speel = False
          break
     



    

elif inp == "Instructions":
  print("Before the game starts, you can choose the options of the game. You can choose the length of the word you have to guess. Once you presses play, you have 8 tries to guess the right word, by choosing diffrent types of letters. If the letter is found in the word, it will be put on the dots. If the letter is not in the word, than the start of a picture will be drawn. If the picture is completed before you have finished the word than you lose. Have you guessed the word, than you win.")
else:
    print("Invalid input!")
  
 
