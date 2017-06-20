import os
import subprocess

print ('What program would you like to run?')

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f == "main.py":
        continue
    print ("\t >", f)
    
#file = "python " +  input()
file = input()

print('\n' + '*' * 80, "\n")

notepadPath = r"C:\Users\victoria_kay\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.exe"
#os.system(file)
subprocess.Popen([notepadPath, file])
