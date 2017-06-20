import string
import random

possibleStrings = string.ascii_letters + string.digits + ".,!?:;"
letterList = []
count = 0

sen = input("Enter your target sentence: ")

for x in range(0, len(sen)):
        letterList.append(random.choice(possibleStrings))
        
while True:

    print (''.join(letterList))
    
    for x in range(0, len(sen)):
        if letterList[x] != sen[x]:
            letterList[x] = random.choice(possibleStrings)
        
    count+=1
    if ''.join(letterList) == sen:
        break

print (''.join(letterList))
print ("{} lines were generated for {}!", count, sen)    
    
