#!/usr/bin/env python
import os
import time
import random
words=['ant','art','attack','ball','bowling','cat','cuckoo','dog','dancing','eat','earth','father','fall','find','ground','garden','hill','hemlock','hockey','ice','island','jackal','jug','kangaroo','kitten','ladder','lord','mother','mug','norway','okay','parrot','puppy','pupil','que','rat','ratatouille','sit','sack','surrender','tin','tatoo','union','unity','ultraviolet','violet','watch','xaxophone','yoyo','zeebra','zenon']
new=[]
str=['MAGNIFICENT','SPLENDID','STUNNING','MARVELOUS','GLORIOUS','FINE','OUTSTANDING','SUPERB','AWESOME','EXQUISITE']
def intro():
    os.system("cls")
    print "Loading..."
    time.sleep(2)
    os.system('cls')
    print "\n\n\t\t\t\tWelcome to BRAIN TEASER!!"
    print "\n\t\t\t\t*************************"
    print "\n\n\n\n\t\t\t\t    Press Any Key!!!"
    raw_input("")
def menu():
    os.system("cls")
    print "\n\n\t\t\t\t*********************\n\t\t\t\t\tMENU:\n\t\t\t\t*********************\n\n\n\t\t\t\t\t1.Play \n\t\t\t\t\t2.Help\n\t\t\t\t\t3.About\n\t\t\t\t\t0.Exit"
    print "\n\n\t\t\t\t*********************\n\n\nEnter your choice:",
    choice=raw_input("")
    if choice=='1':
        lvl(1)
    elif choice=='2':
	manual()
    elif choice=='3':
	about()
    elif choice=='0':
	close()
    else:
        os.system("cls")
	print "Wrong choice..returning back to main menu!! "
	time.sleep(1.7)
        menu()		
def manual():
    os.system("cls")
    print "\t\t\t\t\tHow  to  play???\n\t\t\t\t\t****************\n\n\n\t Welcome  to  BRAIN  TEASER .Depending  on  the  level , a  number  of  words  will  be  displayed  on  the  screen . All  you  have  to  do  is  that  simply  memorize  those  words  and  type  the  same  words  in  their  correct  position  when  asked . Words  are  CASE  SENSITIVE . Since  the  game  consists  of  only  lower  case  words , if  you  enter  upper  case , your  game  will  be  over . So  be  careful  about  the  same .\n\n\n\t Now  coming  to  the  score , clearing  each  level  will  grant  you  100  points . So  score  maximum  points  and  become  the  ultimate  CHAMPION !! Good  luck !!"
    print "\n\nPress any key to return to main menu "
    raw_input("")
    menu()
def about():
    os.system("cls")
    print "\t\t\t\t\tABOUT!"
    print "\t\t\t\t\t******"
    print "\n\tBRAIN TEASER is a word memorizing game which is purely based on Python 2.7."
    print "This game is also a part of project for first year students under KTU."
    print "\n\nPress any key to return to main menu"
    raw_input("")
    menu()
def lvl(n):
    os.system("cls")
    print "\n\n\n\n\n\t\t\t\t\tLEVEL",n
    print "\t\t\t\t\t*******\n"
    i=0
    while i<n:
        new.append(random.choice(words))
	print new[i]
	i=i+1 
    print "\n\nRemember these words!!!!!"
    new_time(n)
    os.system("cls")
    print "Time to check your memory power!!Are you ready?"
    time.sleep(1.7)
    os.system("cls")
    print "Now enter the words in their same order as shown before.."
    print "Press any key to proceed.."
    raw_input("")
    os.system("cls")
    j=0
    while j<n:
        print "Enter the word no. ",j+1
	chr=raw_input("")
	if chr==new[j]:
            os.system("cls")
    	    print "Good job!!"
	    time.sleep(.8)
	    os.system("cls")
        elif chr=='':
            os.system("cls")
	    print "Enter the word correctly!!"
	    j=j-1
            time.sleep(1.7)
            os.system("cls")
	else:
	    disp_new()
            clr_new()           
            fail(n)
	    break
        j=j+1
    
    clr_new()
    nxt_lvl(n)
    return n
def disp_new():
    os.system("cls")
    print "Oops!!You got it wrong!\n"
    print "The correct words were:\n\n"
    i=0
    while i<len(new):
        print new[i]
        i=i+1
    print "\n\nPress any key!!!"
    raw_input("")
    os.system("cls")
def new_time(n):
    t=n*1.5
    time.sleep(t)
def clr_new():
    del new[:]
def nxt_lvl(n):
    if n<20:
	print random.choice(str),"!!!You've been promoted to next level!!!"
        time.sleep(1.3)
        print "\n\n\n\n\n\n\n\t\t\t\tSCORE=",n,"x 100 = ",n*100
        time.sleep(1.5)
        print "\n\n\t\t\t\t\b\bPress any key to continue..."
        raw_input("")
        lvl(n+1)
    else:
	os.system("cls")
	print "Well done,player!!You've completed the game!!Awesome!!"
        print "Congratulations!!You're the ultimate CHAMPION!!"
	time.sleep(2)
	print "\n\n\n\n\n\n\n\t\t\t\tTotal score: ",n," lvl x 100 = ",n*100
	time.sleep(3)  
	print "\n\n\t\t\t\tPress any key to go back to menu.."
	raw_input("")
	os.system("cls")
	menu()  
    return n
def fail(n):
    os.system("cls")
    print "Total score: ",n-1," lvl x 100 = ",(n-1)*100
    print "\n\n\n\n\n\t\t\t\t\tGAME OVER\n\n\n"
    time.sleep(2)
    print "\n\nPress any key to go back to menu"
    raw_input("")
    menu()
def close():
    os.system("cls")
    print "See you soon!"
    print "Exiting game..."
    time.sleep(1.7)
    exit()
os.system("cls")
intro()
menu()	
