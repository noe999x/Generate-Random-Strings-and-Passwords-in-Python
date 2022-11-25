import random,time,os,rich,sys

#for rich print as me
from rich import print as noe

#For animation text
def anim(strings):
    for x in strings:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.03)

#Clear
def clearall():
    os.system('clear')

clearall()
code  = ''.join((random.choice('abcdefghijklmn') for i in range(10))) #module from import random
username=input(' • Username : ') #for input user username
noe('Welcome',username);time.sleep(1) #welcome to user login
noe('\nYour code :',code) #output from random
password=input(' • Code : ') #for input user apikey
anim('Please wait...') #from oading to your destiny
if password==str(code):
   time.sleep(2)
   noe('\n[green]Login Succes[reset]')
   time.sleep(2); #your destiny or exit
else:
     password!=str(code)
     time.sleep(2)
     noe('\n[red]Login failed, check again your code[reset]')
     time.sleep(2); #failed or wrong code password
