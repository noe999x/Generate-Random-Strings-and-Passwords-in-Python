import random,time,os,rich,sys,uuid

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
fakekey=uuid.uuid4() #this import from uuid
username=input(' • Username : ') #for input user username
noe('Welcome',username);time.sleep(1) #welcome to user login
noe('\nYour apikey :',fakekey) #output from uuid
password=input(' • Apikey : ') #for input user apikey
anim('Please wait...') #from loading to your destiny
if password==str(fakekey):
   time.sleep(2)
   noe('\n[green]Login Succes[reset]')
   time.sleep(2); #your destiny or exit
else:
     password!=str(fakekey)
     time.sleep(2)
     noe('\n[red]Login failed, check again your apikey[reset]')
     time.sleep(2); #failed or wrong apikey
