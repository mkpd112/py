# Basic python Programming
# Source YT : DEA AFRIZAL    URL : https://www.youtube.com/watch?v=n0tURC_xeyI&t=130s
# program has been modified from original source for personal training

# content : 
#     - variable
#     - if else condition
#     - library 
#     - data type
#     - looping
#     - system write
#     - I/O
#     - timer
#
#
# study case : guess a cat is hiding in the box


import random
import os
import time
from colorama import Fore   

  
name = input("enter your name :")
box = random.randint(1,6)
running = 'y'

while running == 'y' :
      os.system('cls')
      print(Fore.RESET + 
            f'''
            Hello, {name}! 
            please guess number where cat hide in?
            |1|          |3|          |5|
                  |2|          |4|          |6| 
                  
      ''')
          
      while True :
            answer = int(input(Fore.BLUE + 'Answer (1,2,3,4,5) :'))
            while True:
                  confirm = input("are you sure? [y/n]  :  ")
                  if confirm=='y' or confirm == 'n': break  
                  else : continue
            
            if confirm == 'n' :continue
            else : break
            
      
      if answer == box :
            print(Fore.GREEN + f'''         
            
            
              ∧_______∧
            ( = • · • = )
            /         づ♡   MEW . . . you're right! i'm in box [{box}]
            ''')
            running ="n"
            
      else :
            print(Fore.RED + f'''         
               ／＞　 フ
               | 　_　_| 
             ／` ミ＿xノ 
             /　　　　 |
             /　 ヽ　　 ﾉ
             │　　|　|　|
            ／￣| |　|　|     sorry {name}, your answer ({answer}) is wrong
            (￣ヽ＿_ヽ_)__)   
            ＼二) 
            ''')
            running = input("do you wanna play again?(y/n)")

print (Fore.RESET + "Thanks and Good bye!")

for i in [5,4,3,2,1]:
      print(f"close in {i}")
      time.sleep(1)
      
os.system('cls')