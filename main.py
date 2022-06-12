import random

#Woordenlijst
woorden = ["champion", "eagles", "promise", "stripes", "pavement", "motorcycle", "square", "mountain", "waterfall",]

#zo komt de galg eruit te zien
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

#Introductie
print("Welcome to Python galgje")
usertext = input("What is your name? ")
print("Hello", usertext)

#Spel spelen dmv functie
def speel():

   #kiest woord
   woordkeuze = random.choice(woorden) 
   woord = (woordkeuze)

   #beginsettings
   pogingen =' '
   beurten = 10

   #maakt loop als je levens hebt
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

     #als je alle letters hebt geraden
     if lettersover == 0:
       print("You have won!")

       #wil je opnieuw
       opnieuwwin=str(input("Play again? Type yes or no"))

       #stopt functie
       if opnieuwwin == "no":
        print("Thanks for playing")
        exit()

       #herstart functie
       elif opnieuwwin == "yes":
        speel()

     #gaat verder met functie
     print 

     #regelt aantal beurten bij foute gok
     poging = input ('Guess the letter:')
     pogingen += poging
     if poging not in woord:
       beurten -= 1

       #regelt tekening galg
       galglayout = beurten
       levens=(10-beurten)
       while levens>0:
         print (galg[galglayout])
         galglayout +=1
         levens -=1
       print ("")
       print ("Unfortunately, that is wrong!")

       #vertelt aantal levens
       print ('You have', + beurten, 'lives left')

       #vertelt dat je hebt verloren
       if beurten == 0:
         print ('Too bad!', usertext, 'You have lost!, the word was:', woord)

         #vraagt of je opnieuw wil
         opnieuwverlies=str(input("Play again? Type yes or no"))
         #sluit loop af
         if opnieuwverlies == "no":
           print("Thanks for playing")
           exit()

         #herstart functie en spel
         elif opnieuwverlies == "yes":
           speel()

#geeft keuze over wat te doen
print("What do you want to do?")
print("-to start, type: Start")
print("-to show the instructions, type: Instructions")
inp = input("Enter a word:")

#start gelijk spel
if inp == "Start":
  print("Alright, let's begin then!")
  speel()
  
#toont instructies
elif inp == "Instructions":
 print("Before the game starts, you can choose the options of the game. You can choose the length of the word you have to guess. Once you presses play, you have 10 tries to guess the right word, by choosing diffrent types of letters. If the letter is found in the word, it will be put on the dots. If the letter is not in the word, than the start of a picture will be drawn. If the picture is completed before you have finished the word than you lose. Have you guessed the word, than you win. Is that clear?") 

 #vraagt of het duidelijk
 antwoord = input("yes / no")

 #instructies duidelijk, start spel 
 if antwoord == "yes":
  print("Let's start the game then!")
  speel()

 #toont instructies opnieuw en start spel   
 elif antwoord == "no":
  print("Here are the instructions again")
  print("Before the game starts, you can choose the options of the game. You can choose the length of the word you have to guess. Once you presses play, you have 8 tries to guess the right word, by choosing diffrent types of letters. If the letter is found in the word, it will be put on the dots. If the letter is not in the word, than the start of a picture will be drawn. If the picture is completed before you have finished the word than you lose. Have you guessed the word, than you win.")
  print ("Now, let's start the game!")
  speel()
 

 