print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the God Of War.")
print("Your mission is to find the pandora box.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction= input("There are two bridges ahead, Choose either the left or right: ")
if direction == "left":
  bridge=input(print("You are on the The Great Serpent's bridge,\nYou need to find the serpent's horn to awaken the serpent\nDo you want to find the Horn\nAnswer with Yes or no"))
  if bridge=="Yes" or bridge=="yes" or bridge =="YES":
    serpent=input("The Serpent has awakend....ohssesshh\nThere are two options either you can run or you can face the serpent ")
    if serpent=="run" or serpent=="RUN" or serpent=="Run":
      print ("You coward.... The serpent will hunt the running prey....\nYour Quest ends here ")
    elif serpent =="face" or serpent=="Face" or serpent=="FACE":
      print("Whoola... The serpent has shown us the path for the pandora temple ")
      temple=input("There are three chambers ahead\n Fire   Water   Earth \n Choose any one chamber ")
      if temple=="Fire" or temple=="fire" or temple=="FIRE":
        print("Wrong Chamber. You have been burnt alive in the soul fire of Hades ")
      elif temple=="Water" or temple=="water" or temple=="WATER":
        print("Wrong Chamber. You have drowned in the water of poseidon ")
      elif temple=="Earth" or temple=="earth" or temple=="EARTH":
        print("You have found the Pandora's Box. Great job Champ ")
  else:
    print("No path to go ahead... Restart the game... Choose the correct options this time")
          
elif direction =="right" :
  boat=input("You are in the waters of Poseidon. Either you can wait for the royal posiedon travels or just have leisure swin across the all 7 oceans\nChoose either swim or wait ")
  if boat=="wait" or boat =="WAIT" or boat == "Wait":
    print("Your boat has arrived.... You can board in and travel to your destination ")
  elif boat=="swim" or boat=="Swim" or boat=="SWIM":
    swim=input("You Fool... Swiming in all 7 oceans will take eternity to reach.... Good luck with your quest... Still do you want to swim or go back ")
    if swim=="swim" or swim=="Swim" or swim=="SWIM":
      print("Yours illogical thinking has lead you to yours death due to starvation ")
    else:
      print("Good desision.. You have waited and got on the boat now your in Pandora's Temple")
      temple=input("There are three chambers ahead\n Fire   Water   Earth \n Choose any one chamber ")
      if temple=="Fire" or temple=="fire" or temple=="FIRE":
        print("Wrong Chamber. You have been burnt alive in the soul fire of Hades ")
      elif temple=="Water" or temple=="water" or temple=="WATER":
        print("Wrong Chamber. You have drowned in the water of poseidon ")
      elif temple=="Earth" or temple=="earth" or temple=="EARTH":
        print("You have found the Pandora's Box. Great job Champ ")