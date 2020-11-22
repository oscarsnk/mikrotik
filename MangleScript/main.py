from mikrotik_api import Api
from os import system
import time


def menu():
    system("cls")
    print('-- Mikrotik Mangle Scripting --')
    print('1.- Default Configs')
    print('2.- Ip, user, password')
    print('3.- Ip, user, password, port')
    menu_option = input("Option : ")
    time.sleep(1)
    system("cls")
    if menu_option == '1':
        first_option()
    elif menu_option == '2':
        second_option()
    elif menu_option == '3':
        third_option()
    else:
        print('Invalid option.-')


def first_option():
    print('-- Mikrotik Mangle Scripting --')
    router = Api('192.168.88.1')
    time.sleep(1)
    system("cls")
    router_query(router)


def second_option():
    print('-- Mikrotik Mangle Scripting --')
    ipRouter = input('Mikrotik IP Address: ')
    userRouter = input('Mikrotik User: ')
    passwordRouter = input('Mikrotik Password: ')
    time.sleep(1)
    system("cls")
    router = Api(f'{ipRouter}', user=f'{userRouter}', password=f'{passwordRouter}')
    router_query(router)


def third_option():
    print('-- Mikrotik Mangle Scripting --')
    ipRouter = input('Mikrotik IP Address: ')
    userRouter = input('Mikrotik User: ')
    passwordRouter = input('Mikrotik Password: ')
    portRouter = input('Mikrotik Port: ')
    time.sleep(1)
    system("cls")
    router = Api(f'{ipRouter}', user=f'{userRouter}', password=f'{passwordRouter}', port=f'{portRouter}')
    router_query(router)


def router_query(router):
    while True:
        print('-- Mikrotik Mangle Scripting --')
        ipAddress = input('IP Client : ')
        clientName = input('Client : ')
        firstScript = f'/ip/firewall/mangle/add\n=chain=prerouting\n=src-address={ipAddress}' \
                      f'\n=action=mark-packet\n=new-packet-mark={clientName}-UP\n=comment={clientName}'
        secondScript = f'/ip/firewall/mangle/add\n=chain=postrouting\n=dst-address={ipAddress}' \
                       f'\n=action=mark-packet\n=new-packet-mark={clientName}-DOWN\n=comment={clientName}'
        exFirst = router.talk(firstScript)
        exSecond = router.talk(secondScript)
        if exFirst == [] and exSecond == []:
            print(" -- Added --")
            time.sleep(1)
            system("cls")
        else:
            print("-- Error --")
            time.sleep(1)
            system("cls")


#   init func
menu()
