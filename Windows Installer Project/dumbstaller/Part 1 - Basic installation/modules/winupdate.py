import os
from admin import *




def win_update():
    os.system("powershell -ExecutionPolicy ByPass -Command Get-WUInstall -MicrosoftUpdate -AcceptAll")
    input()

if not isUserAdmin(): # if user is not admin then run as admin
    runAsAdmin()
   
 win_update()
