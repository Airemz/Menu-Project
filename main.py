# Name: Sadiq Rahman
# Class Assignment: Point of Sale Project
# ICS4U

# This program creates a menu and orders from user input

# Assignment Completed Date: 10,02,2021
from tkinter import *
import sys
import os
# Variables
food=[]
items=[]
drinks=[]
order=[]
attempts=3
subtotal=0
discount=0
extra=0

#Display image
root=Tk()
p = PhotoImage(file="naruto.png")
w1 = Label(root, image=p, height=400, width=10000).pack()
root.wm_attributes('-fullscreen', 'True')

#Using try, except to remove error after using exit()
try:

  # Welcome statement
  print("""
                                                                          
                                                                          ▒█░░▒█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▀█▀ █▀▀ █░░█ ░▀░ █▀▀█ █▀▀█ █░█ █░░█ 　 ▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀ █▀▀▄ 
                                                                          ▒█▒█▒█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 　 ▒█░ █░░ █▀▀█ ▀█▀ █▄▄▀ █▄▄█ █▀▄ █░░█ 　 ▒█▄▄▀ █▄▄█ █░▀░█ █▀▀ █░░█ 
                                                                          ▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ▄█▄ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ▀░▀ ░▀▀▀ 　 ▒█░▒█ ▀░░▀ ▀░░░▀ ▀▀▀ ▀░░▀                                     """)
  print("                                                                                                                    𝙏𝙝𝙚 𝙗𝙚𝙨𝙩 𝙧𝙚𝙨𝙩𝙖𝙪𝙧𝙖𝙣𝙩 𝙞𝙣 𝙆𝙤𝙣𝙤𝙝𝙖!")
  print("\n\n\n\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴡᴇʟᴄᴏᴍᴇ! "+ "\033[0m")
  print("\033[3m"+"\033[1;37m" + "As you enter the restaurant, Uncle Teuchi asks you for the UBER DUPER secret password(ICS4U1)"+"\033[0m")

  # Password Funtion
  while (attempts>0):
    password=str(input("\n\033[3m"+"\033[1;37m"+"You reply with:   "+ "\033[0m"))

    if password=="ICS4U1":
      break

    else:
      print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴛʜᴀᴛ ɪꜱ ɴᴏᴛ ᴛʜᴇ ᴘᴀꜱꜱᴡᴏʀᴅ 😠"+"\033[0m")
      attempts-=1
      
      #Scene when user has run out of attempts
      if attempts==0:
        print("\n\033[3m"+"\033[1;37m" + "Uncle Tetsu nervoulsy backs towards Naruto"+"\033[0m")
        print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ... ᴘʟᴇᴀꜱᴇ ꜱᴘᴀʀᴇ ᴍʏ ʟɪꜰᴇ! "+"\033[0m")
        print("\033[1;33m"+"𝘕𝘢𝘳𝘶𝘵𝘰: 𝘔𝘰𝘷𝘦 𝘈𝘴𝘪𝘥𝘦 𝘜𝘯𝘤𝘭𝘦, 𝘐'𝘭𝘭 𝘥𝘦𝘢𝘭 𝘸𝘪𝘵𝘩 𝘵𝘩𝘦𝘮. 𝘞𝘪𝘯𝘥 𝘚𝘵𝘺𝘭𝘦: 𝘙𝘢𝘴𝘦𝘯 𝘚𝘩𝘶𝘳𝘪𝘬𝘦𝘯"+"\033[0m")
        print("\n\033[3m"+"\033[1;37m" + "you were obliterated from existence💀"+"\033[0m")
        print("\033[7m"+"\033[1;37m" + "bad ending..."+"\033[0m")

        sys.exit()

      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ɪ'ᴍ ɢᴏɪɴɢ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ %d ᴍᴏʀᴇ ᴛʀɪᴇꜱ" % attempts +"\033[0m")

  os.system('clear')

  #Display menu
  print("\033[1;34m"+"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                                                                    
                                                                                                                          ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
                                                                                                                          ████╗░████║██╔════╝████╗░██║██║░░░██║
                                                                                                                          ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
                                                                                                                          ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
                                                                                                                          ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
                                                                                                                          ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""+  """

█▀█ ▄▀█ █▀▄▀█ █▀▀ █▄░█
█▀▄ █▀█ █░▀░█ ██▄ █░▀█   

1. Spicy Thai Miso                                                                        $8.00                                                                                     
2. Chicken Curry                                                                          $6.50                                                                                     
3. Sautéed Vegetable                                                                      $3.99
4. Fried Fish                                                                             $4.99
5. Naruto Uzumaki Special                                                                 $7.50
0. That will be all Teuchi-Sama 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""+ "\033[0m" )
  print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ɪ ꜱᴇᴇ ʏᴏᴜ ᴀʀᴇ ᴏɴᴇ ᴡɪᴛʜ ᴋᴏɴᴏʜᴀ"+"\033[0m")
  print("\033[3m"+"\033[1;37m"+"uncle Teuchi is impressed "+ "\033[0m")
  print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ʜᴇʀᴇ, ᴛᴀᴋᴇ ᴀ ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ᴍᴇɴᴜ ᴀɴᴅ ᴛᴇʟʟ ᴍᴇ ᴡʜᴀᴛ ɪ ᴄᴀɴ ɢᴇᴛ ʏᴀ'"+"\033[0m")

  #Menu function
  while True:
    

    #Input statement
    selection=int(input("\033[3m"+"\033[1;37m"+"You salivatigly ask for:   "+ "\033[0m"))

    #If input isn't in range, restart loop
    if (selection>5 or selection<0):
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ꜱᴏʀʀʏ ᴡᴇ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴀᴛ ʜᴇʀᴇ. ᴄᴀɴ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏᴘᴛɪᴏɴꜱ"+"\033[0m")
    
    #Exit loop if input is 0
    elif selection==0:
        break

    #If input is valid, input statement for amount
    else:
      amount=int(input("\033[1;31m" + "ᴛᴇᴜᴄʜɪ: ᴀɴᴅ ʜᴏᴡ ᴍᴀɴʏ ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ?     " + "\033[0m"))

    #Display what user just ordered and add to list
    if selection==1:
      print("\033[1;31m" + "ᴛᴇᴜᴄʜɪ: %d ꜱᴘɪᴄʏ ᴛʜᴀɪ ᴍɪꜱᴏ ʀᴀᴍᴇɴ ᴄᴏᴍɪɴɢ ʀɪɢʜᴛ ᴜᴘ" % amount + "\033[0m" )
      while(amount!=0):
        food.append("Miso")
        amount-=1
    
    elif selection==2:
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: %d ᴄʜɪᴄᴋᴇɴ ᴄᴜʀʀʏ ʀᴀᴍᴇɴ ᴄᴏᴍɪɴɢ ʀɪɢʜᴛ ᴜᴘ"  % amount +"\033[0m")
      while(amount!=0):
        food.append("Curry")
        amount-=1
        
    elif selection==3:
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: %d ꜱᴀᴜᴛÉᴇᴅ ᴠᴇɢᴇᴛᴀʙʟᴇ ʀᴀᴍᴇɴ ᴄᴏᴍɪɴɢ ʀɪɢʜᴛ ᴜᴘ" % amount+"\033[0m")
      while(amount!=0):
        food.append("Vegetable")
        amount-=1
      
    elif selection==4:
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: %d ꜰʀɪᴇᴅ ꜰɪꜱʜ ʀᴀᴍᴇɴ ᴄᴏᴍɪɴɢ ʀɪɢʜᴛ ᴜᴘ" % amount+"\033[0m" )
      while(amount!=0):
        food.append("Fish")
        amount-=1
        
    elif selection==5:
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: WOW! My favourite! %d ɴᴀʀᴜᴛᴏ ᴜᴢᴜᴍᴀᴋɪ ꜱᴘᴇᴄɪᴀʟ ʀᴀᴍᴇɴ ᴄᴏᴍɪɴɢ ʀɪɢʜᴛ ᴜᴘ" % amount+"\033[0m")
      while(amount!=0):
        food.append("Naruto")
        amount-=1

    print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴄᴀɴ ɪ ɢᴇᴛ ʏᴏᴜ ᴀɴʏᴛʜɪɴɢ ᴇʟꜱᴇ ᴛᴏᴅᴀʏ?")

  
  os.system('clear')

  #Drinks menu
  print("\033[1;34m"+"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                                                                    
                                                                                                                          ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
                                                                                                                          ████╗░████║██╔════╝████╗░██║██║░░░██║
                                                                                                                          ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
                                                                                                                          ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
                                                                                                                          ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
                                                                                                                          ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

█▀▄ █▀█ █ █▄░█ █▄▀ █▀
█▄▀ █▀▄ █ █░▀█ █░█ ▄█
1. Passion Fruit Bubble Tea                                                             $8.00 
2. Green Tea                                                                            $6.50 
3. Mango drink                                                                          $3.99
4. Coke                                                                                 $4.99
5. Water                                                                                $7.50
0. That will be all Teuchi-Sama 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
  #Input if user would like drink or not, if no moves onto seating type
  print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏʜ ᴅʀɪɴᴋꜱ? ꜰᴏʀɢɪᴠᴇ ᴍᴇ, ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴅʀɪɴᴋ ᴍᴇɴᴜ. ᴄᴀɴ ɪ ɢᴇᴛ ʏᴏᴜ ꜱᴏᴍᴇᴛʜɪɴ' ")
  selection3=input("\033[3m"+"\033[1;37m"+"You quickly respond(Yes/No):    "+ "\033[0m")

  #Iinput drinks
  if (selection3=="Yes"):
    print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ꜱᴜʀᴇ ᴛʜɪɴ'. ᴡʜᴀᴛ ᴄᴀɴ ɪ ɢᴇᴛ ʏᴀ':    ")
    while True:

      selection2=int(input("\033[3m"+"\033[1;37m"+"You salivatingly reply:    "+ "\033[0m"))
  
      if (selection2>5 or selection2<0):
        print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ɪ ᴅɪᴅɴ'ᴛ ᴄᴀᴛᴄʜ ᴛʜᴀᴛ. ᴄᴏᴜʟᴅ ʏᴏᴜ ꜱᴀʏ ɪᴛ ᴏɴᴇ ᴍᴏʀᴇ ᴛɪᴍᴇ")
        
      #Repeats function until user selects 0
      elif selection2==0:
          break

      if selection2==1:
        print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏɴᴇ ᴘᴀꜱꜱɪᴏɴ ꜰʀᴜɪᴛ ʙᴜʙʙʟᴇ ᴛᴇᴀ ᴄᴏᴍɪɴɢ ᴜᴘ!")
        drinks.append("Passion Fruit Bubble Tea")
  
      elif selection2==2:
        print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏɴᴇ ɢʀᴇᴇɴ ᴛᴇᴀ ᴄᴏᴍɪɴɢ ᴜᴘ!")
        drinks.append("Green Tea")
          
      elif selection2==3:
        print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏɴᴇ ᴍᴀɴɢᴏ ᴅʀɪɴᴋ ᴄᴏᴍɪɴɢ ᴜᴘ!")
        drinks.append("Mango Drink")
        
      elif selection2==4:
        print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏɴᴇ ʙᴏᴛᴛʟᴇ ᴏꜰ ᴄᴏᴋᴇ ᴄᴏᴍɪɴɢ ᴜᴘ!")
        drinks.append("Coke")
        
      elif selection2==5:
        print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏɴᴇ ᴄᴜᴘ ᴏꜰ ᴡᴀᴛᴇʀ ᴄᴏᴍɪɴɢ ᴜᴘ!")
        drinks.append("Water")

      print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴀɴᴏᴛʜᴇʀ ᴅʀɪɴᴋ ꜰᴏʀ ʏᴀ'?")
      
  os.system('clear')

#Adding food to subtotal so that subtotal value can be used for seating type function
  if ("Miso" in food):
    items.append(food.count("Miso"))
    subtotal+=(items[-1]*8)

  if ("Curry" in food):
    items.append(food.count("Curry"))
    subtotal+=(items[-1]*6.5)

  if ("Vegetable" in food):
    items.append(food.count("Vegetable"))
    subtotal+=(items[-1]*3.99)

  if ("Fish" in food):
    items.append(food.count("Fish"))
    subtotal+=(items[-1]*4.99)

  if ("Naruto" in food):
    items.append(food.count("Naruto"))
    subtotal+=(items[-1]*7.5)

#Adding drinks to subtotal for same reason
  if ("Passion Fruit Bubble Tea" in drinks):
    items.append(drinks.count("Passion Fruit Bubble Tea"))
    subtotal+=(items[-1]*8)

  if ("Green Tea" in drinks):
    items.append(drinks.count("Green Tea"))
    subtotal+=(items[-1]*6.5)

  if ("Mango Drink" in drinks):
    items.append(drinks.count("Mango Drink"))
    subtotal+=(items[-1]*3.99)

  if ("Coke" in drinks):
    items.append(drinks.count("Coke"))
    subtotal+=(items[-1]*4.99)
   
  if ("Water" in drinks):
    items.append(drinks.count("Water"))
    subtotal+=(items[-1]*7.5)

#Function to calculate total cost      
  def total(a,b,c):
    b2=a*b
    total=(a-b2+c)*1.13
    return(total)
    

#Seating Type inputed and if statements to put correct parameters into total function
  for x in range(0,10):
    print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏᴋ! ꜱᴏ ᴀʀᴇ ʏᴀ' ᴇᴀᴛɪɴɢ ʜᴇʀᴇ? ᴛʜᴇʀᴇ? ᴏʀ ᴀᴛ ʏᴀ' ʜᴏᴜꜱᴇ? ᴡᴇ'ᴠᴇ ɢᴏᴛ ꜱᴏᴍᴇ ᴅꜱᴄᴏᴜɴᴛꜱ ᴀɴᴅ ꜱᴏᴍᴇ ꜰᴇᴇꜱ 😊")
    print("\033[1;34m"+"""
    1. Dine in
    2. Take-out (10% discount)
    3. Delivery (if subtotal is under $25, $3.50 delivery fee)
    """)
    seating=int(input("\033[3m"+"\033[1;37m"+"You humbly request to:     "+ "\033[0m"))

    if seating==1:
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ɢᴏᴛ ɪᴛ. ꜱᴏ ʏᴀ ᴇᴀᴛɪɴɢ ʜᴇʀᴇ.")
      t=total(subtotal,0,0)
      break

    if seating==2:
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ʟᴜᴄᴋʏ ʏᴏᴜ! ᴡᴇ ɢᴏᴛ ᴀ ᴅɪꜱᴄᴏᴜɴᴛ ꜰᴏʀ ᴛᴀᴋᴇ ᴏᴜᴛᴇʀꜱ'")
      t=total(subtotal,0.10,0)
      discount="10%"
      break
      
    if seating==3:
      if subtotal<25:
        print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴀʜ. ꜱᴏʀʀʏ ʙᴜᴅ ᴛʜᴇʀᴇ'ꜱ ɢᴏɪɴɢ ᴛᴏ ʙᴇ ᴀ ᴅᴇʟɪᴠᴇʀʏ ꜰᴇᴇ")
        t=total(subtotal,0,3.5)
      else:
        print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ɢᴏᴛ ɪᴛ. ꜱɪɴᴄᴇ ʏᴏᴜ ʙᴏᴜɢʜᴛ ꜱᴏ ᴍᴜᴄʜ ɴᴏ ᴅᴇʟɪᴠᴇʀʏ ꜰᴇᴇ ꜰᴏʀ ʏᴏᴜ😊")
        t=total(subtotal,0,0)
      break
    
    else:
      print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ꜱᴏʀʀʏ ᴅɪᴅɴ'ᴛ ᴄᴀᴛᴄʜ ᴛʜᴀᴛ. ᴄᴏᴜʟᴅ ʏᴏᴜ ꜱᴀʏ ɪᴛ ᴏɴᴇ ᴍᴏʀᴇ ᴛɪᴍᴇ")

#Final Receipt
  print("\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ʀᴇᴄᴇɪᴘᴛ!")
  print("\033[1;34m" + """
                                                                                                            
                                                                                                        ▀█▀ █▀▀ █░░█ ░▀░ █▀▀█ █▀▀█ █░█ █░░█ 　 ▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀ █▀▀▄ 
                                                                                                        ▒█░ █░░ █▀▀█ ▀█▀ █▄▄▀ █▄▄█ █▀▄ █░░█ 　 ▒█▄▄▀ █▄▄█ █░▀░█ █▀▀ █░░█ 
                                                                                                        ▄█▄ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ▀░▀ ░▀▀▀ 　 ▒█░▒█ ▀░░▀ ▀░░░▀ ▀▀▀ ▀░░▀

  """)

  print("""

                                                                                                                                █▀█ █▀▀ █▀▀ █▀▀ █ █▀█ ▀█▀
                                                                                                                                █▀▄ ██▄ █▄▄ ██▄ █ █▀▀ ░█░
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  """)
  #Check which items were ordered and print them out  
  if ("Miso" in food):
    items.append(food.count("Miso"))
    print("%d Spicy Thai Miso Ramen for                               $8.00 each" % items[-1])
  if ("Curry" in food):
    items.append(food.count("Curry"))
    print("%d Chicken Curry Ramen for                                 $6.50 each " % items[-1])
  if ("Vegetable" in food):
    items.append(food.count("Vegetable"))
    print("%d Sautéed Vegetable Ramen for                             $3.99 each" % items[-1])
  if ("Fish" in food):
    items.append(food.count("Fish"))
    print("%d Fried Fish Ramen for                                    $4.99 each" % items[-1])
  if ("Naruto" in food):
    items.append(food.count("Naruto"))
    print("%d Naruto Uzumaki Special Ramen for                        $7.50 each" % items[-1])
  if ("Passion Fruit Bubble Tea" in drinks):
    items.append(drinks.count("Passion Fruit Bubble Tea"))
    print("%d Passion Fruit Bubble Tea for                            $8.00 each" % items[-1])
  if ("Green Tea" in drinks):
    items.append(drinks.count("Green Tea"))
    print("%d Green Tea for                                           $6.50 each" % items[-1])
  if ("Mango Drink" in drinks):
    items.append(drinks.count("Mango Drink"))
    print("%d Mango Drink for                                         $3.99 each" % items[-1])
  if ("Coke" in drinks):
    items.append(drinks.count("Coke"))
    print("%d Bottle(s) of Coke for                                   $4.99 each" % items[-1])
  if ("Water" in drinks):
    items.append(drinks.count("Water"))
    print("%d Cup(s) of water for                                     $7.50 each" % items[-1])
  print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  

  print("\nYour subtotal is:                                         $%.2f" % subtotal)
  print("Your discount is:                                          %s" % discount)
  print("Your extra charges is:                                     %s" % extra)
  print("Your TOTAL is:                                            $%.2f" % t)

  if ("Naruto" in food):
      print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴡᴏᴡ! ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ʙᴜʏɪɴɢ ꜱᴏ ᴍᴀɴʏ ɴᴀʀᴜᴛᴏ ᴜᴢᴜᴍᴀᴋɪ ꜱᴘᴇᴄɪᴀʟ. ɪ'ʟʟ ʙᴇ ꜱᴜʀᴇ ᴛᴏ ᴛᴇʟʟ ʟᴏʀᴅ ʜᴏᴋᴀɢᴇ ᴀʙᴏᴜᴛ ʏᴏᴜ!")
      print("\033[1;33m"+"𝘕𝘢𝘳𝘶𝘵𝘰: 𝘏𝘦𝘺 𝘜𝘯𝘤𝘭𝘦 𝘛𝘦𝘶𝘤𝘩𝘪. 𝘞𝘩𝘰 𝘪𝘴 𝘵𝘩𝘪𝘴?"+"\033[0m")
      print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴏʜ ɴᴀʀᴜᴛᴏ! ᴡᴇ ᴡᴇʀᴇ ᴊᴜꜱᴛ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ ʏᴏᴜ. ᴛʜɪꜱ ᴘᴇʀꜱᴏɴ ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ʙɪɢɢᴇꜱᴛ ꜰᴀɴ. ᴛʜᴇʏ ᴏʀᴅᴇʀᴇᴅ ᴛʜᴇ ɴᴀʀᴜᴛᴏ ᴜᴢᴜᴍᴀᴋɪ ꜱᴘᴇᴄɪᴀʟ ʀᴀᴍᴇɴ.")
      print("\033[1;33m"+"𝘕𝘢𝘳𝘶𝘵𝘰: 𝘞𝘩𝘢𝘵! 𝘕𝘰 𝘸𝘢𝘺! 𝘠𝘰𝘶 𝘬𝘯𝘰𝘸 𝘸𝘩𝘢𝘵, 𝘫𝘶𝘴𝘵 𝘧𝘰𝘳 𝘵𝘩𝘢𝘵. 𝘠𝘰𝘶 𝘤𝘢𝘯 𝘣𝘦 𝘵𝘩𝘦 𝘯𝘦𝘹𝘵 𝘩𝘰𝘬𝘢𝘨𝘦! 𝘎𝘰𝘰𝘥 𝘭𝘶𝘤𝘬😊"+"\033[0m")
      print("\033[3m"+"\033[1;37m"+"You are shooketh and thus died from excitement"+ "\033[0m")
      print("\033[7m"+"\033[1;37m" + "secret ending..."+"\033[0m")

  else: 
    print("\n\033[1;31m"+"ᴛᴇᴜᴄʜɪ: ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴅɪɴɪɴɢ ᴡɪᴛʜ ᴜꜱ ᴛᴏᴅᴀʏ!")
    print("\033[3m"+"\033[1;37m"+"You feel appleased"+ "\033[0m")
    print("\033[7m"+"\033[1;37m" + "good ending... but theres better"+"\033[0m")
   
except:
  pass

root.mainloop()

  