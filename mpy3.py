import subprocess as sub
import playsound
import os
from mutagen.mp3 import MP3
import time
sub.call("clear")
os.chdir("plyst")
dir_list = os.listdir(os.getcwd())


class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

print(bcolors.PURPLE)
logo = '''
                                                                                  link:
███╗   ███╗██████╗ ██╗   ██╗██████╗ 			 __| |____________________________________________| |__
████╗ ████║██╔══██╗╚██╗ ██╔╝╚════██╗     		(__   ____________________________________________   __)
██╔████╔██║██████╔╝ ╚████╔╝  █████╔╝                 	   | |github: https://github.com/redKatz          | |  
██║╚██╔╝██║██╔═══╝   ╚██╔╝   ╚═══██╗    	      	   | |instagram: https://www.instagram.com/katz.py| |
██║ ╚═╝ ██║██║        ██║   ██████╔╝  		         __| |____________________________________________| |__
╚═╝     ╚═╝╚═╝        ╚═╝   ╚═════╝		        (__   ____________________________________________   __)
						           | |                                            | |

						        

'''

				  
print(logo)
print(bcolors.ENDC)
print("Playlist found:\n")
print(bcolors.WARNING)
for a, b in enumerate(dir_list, 1):
	print('-{} [{}]'.format(a, b))
print(bcolors.ENDC)
scelta_plyst = input("\nNumber of playlist you want to use: ")

sub.call("clear")
print(bcolors.PURPLE)
print(logo)
print(bcolors.ENDC)
if scelta_plyst == "1":
	plyst = dir_list[0]
elif scelta_plyst == "2":
	plyst = dir_list[1]
print("\nSong in "+plyst+":")
os.chdir(plyst)
dir_list = os.listdir(os.getcwd())
print(bcolors.WARNING)
for a, b in enumerate(dir_list, 1):
	print('-{} [{}]'.format(a, b))
print(bcolors.ENDC)
canzone_domanda = input("Number of track you want to start with: ")
if canzone_domanda == "1":
	canzone = dir_list[0]
elif canzone_domanda == "2":
	canzone = dir_list[1]
c = int(canzone_domanda)
c = c-1
while True:	
	try:
		canzone = dir_list[c]
		sub.call("clear")
		print(bcolors.PURPLE)
		print(logo)
		print(bcolors.ENDC)
		tosec = (int((MP3(canzone).info.length))/60)
		fintosec = round(tosec, 2)
		print("Now you are listening: "+bcolors.BOLD+bcolors.UNDERLINE+bcolors.PURPLE+canzone+bcolors.ENDC+" length -->"+ " "+bcolors.BOLD+bcolors.UNDERLINE+str(fintosec)+bcolors.ENDC)
		playsound.playsound(canzone)
		c = c+1
		time.sleep(2)
	except IndexError:
		restart_re = input("\n\nThe playlist id finished do you want restart playlist? y/n: ")
		if restart_re == "y":
			print(bcolors.BOLD+bcolors.OKBLUE+bcolors.UNDERLINE+"\nThe playlist restart in"+bcolors.ENDC)
			print(bcolors.WARNING+"\n3")
			time.sleep(0.5)
			print("2")
			time.sleep(0.4)
			print("1"+bcolors.ENDC)
			time.sleep(0.2)
			c = 0
			continue
		elif restart_re == "n":
			bye = '''
			     ; 
     ;;
     ;';.
     ;  ;;
     ;   ;;
     ;    ;;    
     ;    ;;
     ;   ;'					  
     ;  ' 
,;;;,;                     
;;;;;;          Ｇｏｏｄ ｂｙｅ
`;;;;'
'''
			print(bcolors.PURPLE+bye+bcolors.ENDC)
			break
		else:
			print("\nyou did somenthing wrong")
			break


