import random,time,os,rich,sys,secrets

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
token=secrets.token_hex(12) #module import from secrets
username=input(' • Username : ') #for input user username
noe('Welcome',username);time.sleep(1) #welcome to user login
noe('\nYour token :',token) #output from secrets module
password=input(' • Token : ') #for input user apikey
anim('Please wait...') #from oading to your destiny
if password==str(token):
   time.sleep(2)
   noe('\n[green]Login Succes[reset]')
   time.sleep(2); #your destiny or exit
else:
     password!=str(token)
     time.sleep(2)
     noe('\n[red]Login failed, check again your token[reset]')
     time.sleep(2); #failed or wrong token
