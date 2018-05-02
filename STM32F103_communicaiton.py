#!/usr/bin/env Python
# -*- coding: utf-8 -*-

# author=chenzixuan
# operating 21-4-2018	23:00


import serial
import serial.tools.list_ports
import time
import threading
import binascii

plist = list(serial.tools.list_ports.comports())
if len(plist) > 0:
    print("*************************STM32F103 Serial Comunication system**********************************")
    ser = serial.Serial(plist[0][0], 9600, timeout=0.1)
    print('\n' + """Already have found a Port, PortName is """ + ser.portstr + '\n')
    print('\nBaundrate = ' + str(ser.baudrate) +
          ', Timeout = ' + str(ser.timeout) + '\n')
    try:
        while(1):
            print("***********************************************************************************************")
            print("Press Number you want below:")
            print('\n1.Sent hello message to STM32F103\n')
            print('\n2.You want to ask some question\n')
            print('\n3.You want to quit this program\n')
            print("***********************************************************************************************")

            order = input("Your order is :")
            if order == '1':  # 进入一号界面
                while(1):
                    print(
                        "***********************************************************************************************")
                    send = 'Hello World!' + '\r\n'

                    print(
                        "We have sent message(hello world!) to STM32,Here is its response:\n")
                    ser.write(send.encode('gbk'))
                    while(1):
                        bt = ser.readline()
                        if(len(bt) > 0):
                            if(bt[0] != 199):
                                print(str(bt.decode('gbk')))  # 开始监听
                                break

                    string = input("Press Enter to Back!")
                    break  # 撤回主屏幕

            elif order == '2':  # 进入二号界面
                while(1):
                    print(
                        "***********************************************************************************************")
                    print("Press Number you want below to ask STM32 questions:")
                    print("\n1.What's your name?\n")
                    print('\n2.How old are you?\n')
                    print('\n3.Type on your self!\n')
                    print('\n4.You want to quit this board\n')
                    print(
                        "***********************************************************************************************")

                    order_ = input("Your order is :")
                    print('\r\n')
                    if order_ == '1':
                        send_ = "Whats your name?" + '\r\n'
                        print('You have asked("What\'s your name?"). Answering:')
                        ser.write(send_.encode('gbk'))
                        while(1):
                            bt = ser.readline()
                            if(len(bt) > 0):
                                if(bt[0] != 199):
                                    # 开始监听
                                    print('\r\n' + str(bt.decode('gbk')))
                                    break
                    elif order_ == '2':
                        send__ = "How old are you?" + '\r\n'
                        print('You have asked("How old are you?"). Answering:')
                        ser.write(send__.encode('gbk'))
                        while(1):
                            bt = ser.readline()
                            if(len(bt) > 0):
                                if(bt[0] != 199):

                                    # 开始监听
                                    print('\r\n' + str(bt.decode('gbk')))
                                    break
                    elif order_ == '3':
                        send_user = input("Your question is :")
                        send_user_end=send_user+'\r\n'
                        print('\r\nThe STM32\'s answer is :')
                        ser.write(send_user_end.encode('gbk'))
                        while(1):
                            bt = ser.readline()
                            if(len(bt) > 0):
                                if(bt[0] != 199):

                                    # 开始监听
                                    print('\r\n' + str(bt.decode('gbk')))
                                    break
                    elif order_ == '4':
                        break
                    else:
                        print('You have pressed an unexpected number!')

            elif order == '3':  # 进入三号界面
                break

            else:
                print("You have pressed an unexpected number! Please Press again!")

    except Exception as e:
        print("***********************************************************************************************")
        print("Have found an Error:" + str(e))
    finally:
        ser.close()
else:
    print("***********************************************************************************************")
    print("Didn't find a Port!")
