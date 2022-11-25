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
otp=random.randint(000000,100000) #module from random
username=input(' • Username : ') #for input user username
noe('Welcome',username);time.sleep(1) #welcome to user login
noe('\nYour OTP :',otp) #output from random
password=input(' • OTP : ') #for input user otp
anim('Please wait...') #from oading to your destiny
if password==str(otp):
   time.sleep(2)
   noe('\n[green]Login Succes[reset]')
   time.sleep(2); #your destiny or exit
else:
     password!=str(otp)
     time.sleep(2)
     noe('\n[red]Login failed, check again your otp[reset]')
     time.sleep(2); #failed or wrong otp
