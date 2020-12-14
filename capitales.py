# usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import random
from colorama import Fore, Style,init

page= requests.get("https://jeretiens.net/tous-les-pays-du-monde-et-leur-capitale/");

#random changes
soup=BeautifulSoup(page.text,features="lxml")
rightList=[]
secondRightList=[]
print("Type \"blank\" to get all the capitals without saving them, otherwise just press ENTER" );
run=input()
blank= False
if run=="blank":
	blank=True
else:
	with open("./rightList","r") as file:
		for line in file.readlines():
			line=line.strip()
			elementCount=0
			finalElement={}
			while line != "":
				index=line.index("%")
				if elementCount==0:
					finalElement["country"]=line[:index].strip()
				elif elementCount==1:
					finalElement["capital"]=line[:index].strip()
				elif elementCount==2:
					finalElement["memo"]=line[:index].strip()
				else:
					finalElement["continent"]=line[:index].strip()
				index=index+1
				elementCount=elementCount+1
				line=line[index:]
			rightList.append(finalElement)

	with open("./secondRightList","r") as file:
		for line in file.readlines():
			line=line.strip()
			elementCount=0
			finalElement={}
			while line != "":
				index=line.index("%")
				if elementCount==0:
					finalElement["country"]=line[:index].strip()
				elif elementCount==1:
					finalElement["capital"]=line[:index].strip()
				elif elementCount==2:
					finalElement["memo"]=line[:index].strip()
				else:
					finalElement["continent"]=line[:index].strip()
				index=index+1
				elementCount=elementCount+1
				line=line[index:]
			secondRightList.append(finalElement)
finalArray=[]
counter=0
secondCounter=0
elements=soup.find_all("tr")
for element in elements:
	pack=element.find_all("td")
	el={
		"country":pack[0].text.strip(),
		"capital":pack[1].text.strip(),
		"memo":pack[2].text.strip().replace("\n",""),
		"continent":pack[3].text.strip()
		}
	if el not in rightList and el not in secondRightList:
		finalArray.append(el)
while True:
	if not blank:
		print(counter)
		print("Rights: ",len(rightList),"Confirmed: ",len(secondRightList),"Total: ", len(rightList)+len(secondRightList),"/199")
		if (secondCounter==5 and counter==3 and len(secondRightList)!=0):
			secondCounter=0
			counter=0
			question=random.randint(0,len(secondRightList)-1)
			el=secondRightList[question]
			print("Capitale de :",Fore.YELLOW+el["country"]+Style.RESET_ALL)
			answer=input()
			if(answer==el["capital"].strip()):
				print("Right answer ! the continent is: "+Fore.BLUE +el["continent"]+Style.RESET_ALL)
				print("Memo:"+ Fore.RED+el["memo"]+"\n"+Style.RESET_ALL)
				secondRightList.pop(question)
				continue
			else:
				print("\nFalse, the answer is: "+Fore.GREEN,el["capital"],Style.RESET_ALL+"in: ",Fore.BLUE,el["continent"]+Style.RESET_ALL)
				string=str(el["country"]+"%"+el["capital"]+"%"+el["memo"]+"%"+el["continent"]+"%\n")
				print("Memo: ",Fore.RED+el["memo"],"\n",Style.RESET_ALL)
				with open("./secondRightList",'r') as secondRightFile:
						lines=secondRightFile.readlines()
				with open("./secondRightList",'w') as secondRightFile:
					for line in lines:
						if line != string:
							secondRightFile.write(line)
				with open("./rightList",'a') as rightFile:
					rightFile.write(string)
				secondRightList.pop(question)
				rightList.append(el)
				continue
			
		elif counter==3 and len(rightList)!=0:
			counter=0
			secondCounter=secondCounter+1
			question=random.randint(0,len(rightList)-1)
			el=rightList[question]
			print("Capitale de :",Fore.YELLOW+el["country"]+Style.RESET_ALL)
			answer=input()
			if(answer==el["capital"].strip()):
				print("Right answer ! the continent is: "+Fore.BLUE +el["continent"]+Style.RESET_ALL)
				print("Memo:"+ Fore.RED+el["memo"]+"\n"+Style.RESET_ALL)
				with open("./secondRightList",'a') as file:
					string=str(el["country"]+"%"+el["capital"]+"%"+el["memo"]+"%"+el["continent"]+"%\n")
					secondRightList.append(el)
					file.write(string)
					with open("./rightList",'r') as rightfile:
						lines=rightfile.readlines()
					with open("./rightList",'w') as rightFile:
						for line in lines:
							if line != string:
								rightFile.write(line)
				rightList.pop(question)
				continue
			else:
				print("\nFalse, the answer is: "+Fore.GREEN,el["capital"],Style.RESET_ALL+"in: ",Fore.BLUE,el["continent"]+Style.RESET_ALL)
				print("Memo: ",Fore.RED+el["memo"],"\n",Style.RESET_ALL)
				with open("./rightList",'r') as rightfile:
						lines=rightfile.readlines()
				with open("./rightList",'w') as rightFile:
					string=str(el["country"]+"%"+el["capital"]+"%"+el["memo"]+"%"+el["continent"]+"%\n")
					for line in lines:
						if line != string:
							rightFile.write(line)
				rightList.pop(question)
				finalArray.append(el)
				continue
		else :
			question=random.randint(0,len(finalArray)-1)
			el=finalArray[question]
			print("Capitalle de :",Fore.YELLOW+el["country"]+Style.RESET_ALL)
			answer=input()
			if(answer==el["capital"].strip()):
				counter=counter+1
				print("Right answer ! the continent is: "+Fore.BLUE +el["continent"]+Style.RESET_ALL)
				print("Memo:"+ Fore.RED+el["memo"]+"\n"+Style.RESET_ALL)
				with open("./rightList","a") as file:
					string=str(el["country"]+"%"+el["capital"]+"%"+el["memo"]+"%"+el["continent"]+"%\n")
					rightList.append(el)
					file.write(string)
				finalArray.pop(question)
				continue
			else:
				print("\nFalse, the answer is: "+Fore.GREEN,el["capital"],Style.RESET_ALL+"in: ",Fore.BLUE,el["continent"]+Style.RESET_ALL)
				print("Memo: ",Fore.RED+el["memo"],"\n",Style.RESET_ALL)
				continue
	else:
		question=random.randint(0,len(finalArray)-1)
		el=finalArray[question]
		print("Capitalle de :",Fore.YELLOW+el["country"]+Style.RESET_ALL)
		answer=input()
		if(answer==el["capital"].strip()):
			print(len(finalArray)+"/199")
			counter=counter+1
			print("Right answer ! the continent is: "+Fore.BLUE +el["continent"]+Style.RESET_ALL)
			print("Memo:"+ Fore.RED+el["memo"]+"\n"+Style.RESET_ALL)
			finalArray.pop(question)
			continue
		else:
			print("\nFalse, the answer is: "+Fore.GREEN,el["capital"],Style.RESET_ALL+"in: ",Fore.BLUE,el["continent"]+Style.RESET_ALL)
			print("Memo: ",Fore.RED+el["memo"],"\n",Style.RESET_ALL)
			continue
