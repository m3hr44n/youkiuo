
#/usr/bin/python3
#Developed by hakfateam Contact Me : https://t.me/mk3em  && https://t.me/hakfateam
#import Liberary in Script

import itertools
import string
import colorama #this is not a buildin liberary in python you must be install on yor system with command : pip install colorama
import pyfiglet #this is not a buildin liberary in python you must be install on yor system with command : pip install pyfiglet

script_banner = pyfiglet.figlet_format('Youkiuo' , font='doom')

print(colorama.Fore.RED + "                  " + script_banner)

print(colorama.Fore.GREEN,'''                  https://t.me/hakfateam 
      
                     https://t.me/mk3em
         
             ------------------------------------
             ------------------------------------''')


def bruteforce_attack(password):
    
    chars = string.printable.strip()
    
    attempts = 0
   
    for length in range(1, len(password) + 1):
     
        for guess in itertools.product(chars, repeat=length):
      
            attempts += 1
       
            guess = ''.join(guess)
      
            if guess == password:
        
                return (attempts, guess)
   
    return (attempts, None)

password = input(colorama.Fore.GREEN + "Please Input The Password To Crack ==> ")

print(colorama.Fore.YELLOW + "Password Is Cracking PLease Wait" +" " +  password)

attempts, guess = bruteforce_attack(password)

if guess:
  
    print(colorama.Fore.RED + f"Password cracked in {attempts} attempts. The password is {guess}.")

else:
  
    print(colorama.Fore.MAGENTA + f"Password not cracked after {attempts} attempts.")
