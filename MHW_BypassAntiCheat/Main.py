import os
import ctypes
import subprocess
from time import sleep

class MHW_Bypass:
    def BypassInternalAnticheat():
        print("Welcome to the Bypass Internal Anticheat for Game Monter Hunter World... Enjoy to use this Bypass!!!")
        os.system("start steam://rungameid/582010") #This Is Steam app ID this Game :D
        sleep(480) # 480 seconds it's 8 minutes :D
        process = subprocess.Popen("start {}".format(os.getcwd() + "\\Exec\\MHWResetCRC.exe"), executable="start {}".format(os.getcwd() + "\\Exec\\MHWResetCRC.exe"))
        process.wait(30) #Waiting 30 seconds to kill this process
        process.kill() #Killing This Process
        print("Successed Bypassed Internal AntiCheat... Made by RiritoNinigaya!!!")
def Main():
    MHW_Bypass.BypassInternalAnticheat()

if __name__ == "__main__":
    Main()