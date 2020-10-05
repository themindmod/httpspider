#!/usr/bin/python3

import requests, subprocess, colored
from colored import stylize
#initializing variable
speed = 0
scelta = ""
final = []
counter = 0
count = 0
percorso = input("Path of the list:  ")
desiderio = input("Convert from masscan report? y/n:  ")
ricerca = input("String to search:  ")
askspeed = input("Fast Scan? y/n:  ")
#fastscan set the timeout of the get requests
if askspeed == "y":
	speed = 0.3
else:
	speed = 2
#define the clean up function for the masscan's reports
def func1(x):
	if x == "y":
		command1 = "cat " + percorso +" | grep -i '80/tcp' | grep -v '8080' > /tmp/truetemp.txt"
		modifica = subprocess.check_output(command1,shell=True)
		command2 = "cat truetemp.txt | awk '{print $6}' > /tmp/truetemp2.txt"
		modifica2 = subprocess.check_output(command2, shell=True)
		command3= "for i in $(cat truetemp2.txt) ; do echo \"http://$i\"; done > /tmp/truefinal.txt"
		modifica3 = subprocess.check_output(command3, shell=True)
		return "truefinal.txt"
	else:
		return percorso

#open the func1 returned file, clean up from newlines and make a list
with open(func1(desiderio), "r") as filelista:
	listone = (filelista.readlines())
listone2 = []
for i in listone:
	i = i.strip("\n")
	listone2.append(i)
print(stylize("[+] Loaded "+ str(len(listone2))+" address..", colored.fg("green_3b")))
splitchoose = input("Want to split the list?  y/n (default n):  ")
if splitchoose == "y":
	startindex = input("Start index:  ")
	endindex = input("End index of " + str(len(listone2))+ " ips  (start at "+ str(startindex)+"): ")
	while True:
		try:
			listone3 = listone2[int(startindex):int(endindex)]
			break
		except:
			startindex = input("Invalid index, insert Start index:  ")
			endindex = input("End index of " + str(len(listone2))+ " ips  (start at "+ str(startindex)+"):  ")
else:
	listone3 = listone2
for i in listone3:
	counter += 1
	print("Testing the address: " + i + "   Job: "+str(counter)+"/"+str(len(listone3))+ " "+ str(round(1/(int(len(listone3))/counter)*100, 2))+"%"+ stylize("      Found count: "+ str(count), colored.fg("green_3b")))
	try:
		x = requests.get(i, timeout=speed)
		print("Status Code: "+ str(x.status_code))
		y = x.text
		if y.find(ricerca) != -1:
			print(stylize("Found "+ricerca+" at address:  " + i, colored.fg("yellow")))
			final.append(i)
			count += 1
		else:
			print(stylize("Connected, but not found", colored.fg("yellow")))
		x.close()
	except requests.ConnectionError:
		print(stylize("ConnectionError", colored.fg("red")))
	except:
		print(stylize("GenericError", colored.fg("red")))
if count != 0:
	print(stylize("IP found:  " + str(count), colored.fg("green_3b")))
	print(stylize("[+] Data written in "+ ricerca +"-result.txt", colored.fg("green_3b")))
else:
	print(stylize("[-] Nothing found :(  nothing to write...", colored.fg("red")))

with open(ricerca +"-result.txt", "w") as finalresult:
	for q in final:
			finalresult.write(q+"\n")
	finalresult.close()
closingcommand = "rm -f truetemp.txt truetemp2.txt truefinal.txt"
closingdo = subprocess.check_output(closingcommand, shell=True)