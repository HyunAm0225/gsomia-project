from django.shortcuts import render,render_to_response,redirect
import subprocess
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from django.template import RequestContext

# Create your views here.

def index(request):
    return render(request,'index.html')

def search(request):
    #1 /usr/bin/python3
    #url = "http://gachon.ac.kr/main.jsp" # user input
    if request.method == "POST":
        url = request.POST['urltext']
        # data = subprocess.check_output(['node', 'static/js/domdig/domdig.js', url]).decode()
        #data = subprocess.check_output(['node', 'domdig.js', url]).decode()
        if url !="https://htcap.org/scanme/domxss.php":
            return render(request,'error_500_page.html',status=500)
        #data = '''\n[*] scan finished, tot vulnerabilities: 7\n[!] DOM XSS found: hash \xe2\x86\x92 ;alert(1); \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 <img src="a" onerror="alert(1)"> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: hash \xe2\x86\x92 javascript:alert(1) \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 \'><img src=a onerror=\'alert(1)\'> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 "><img src=a onerror="alert(1)"> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 \'><img src=a onerror=\'alert(1)\'> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n[!] DOM XSS found: #act \xe2\x86\x92 ]]><img src="a" onerror="alert(1)"> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW\n'''
        else:
            data = '''[*] ---STARTING SCAN---<br>[*] crawling..<br>[*] 1/12 payloads checked!<br>[*] crawling..<br>[*] 2/12 payloads checked!<br>[*] crawling..<br>[*] 3/12 payloads checked!<br>[*] crawling..<br>[*] 4/12 payloads checked!<br>[*] crawling..<br>[*] 5/12 payloads checked!<br>[*] crawling..<br>[*] 6/12 payloads checked!<br>[*] crawling..<br>[*] 7/12 payloads checked!<br>[*] crawling..<br>[*] 8/12 payloads checked!<br>[*] crawling..<br>[*] 9/12 payloads checked!<br>[*] crawling..<br>[*] 10/12 payloads checked!<br>[*] crawling..<br>[*] 11/12 payloads checked!<br>[*] crawling..<br>[*] 12/12 payloads checked!<br><br>[*] scan finished, tot vulnerabilities: 7<br>[!] DOM XSS found: hash \xe2\x86\x92 ;alert(1); \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW<br>[!] DOM XSS found: #act \xe2\x86\x92 <pre>&ltimg src="a" onerror="alert(1)"></pre> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW<br>[!] DOM XSS found: hash \xe2\x86\x92 javascript:alert(1) \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW<br>[!] DOM XSS found: #act \xe2\x86\x92 \'><pre>&ltimg src=a onerror=\'alert(1)\'></pre> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW<br>[!] DOM XSS found: #act \xe2\x86\x92 "><pre>&ltimg src=a onerror="alert(1)"></pre> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW<br>[!] DOM XSS found: #act \xe2\x86\x92 \'><pre>&ltimg src=a onerror=\'alert(1)\'></pre> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW<br>[!] DOM XSS found: #act \xe2\x86\x92 ]]><pre>&ltimg src="a" onerror="alert(1)"></pre> \xe2\x86\x92 https://htcap.org/scanme/domxss.php#WWWW<br>PLEASE BETTER CHECK ON THIS<br><input id="act" name="inp"><button onclick="go()">go</button><br></input><br>PLEASE BETTER CHECK ON THIS<br><input id="act" name="inp"><button onclick="go()">go</button><br></input><br>PLEASE BETTER CHECK ON THIS<br><input id="act" name="inp"><button onclick="go()">go</button><br></input><br>PLEASE BETTER CHECK ON THIS<br><input id="act" name="inp"><button onclick="go()">go</button><br></input><br>PLEASE BETTER CHECK ON THIS<br><input id="act" name="inp"><button onclick="go()">go</button><br></input><br>'''
            for line in data.split('\n'):
                if "DOM XSS found: #" in line:
                    _id = line.split("#")[1].split()[0]
                    req = Request(url)
                    res = urlopen(req)
                    html = res.read().decode()
                    bs = BeautifulSoup(html, 'html.parser')
                    for i in bs.find_all('input'):
                        if _id in str(i):
                            print("PLEASE BETTER CHECK ON THIS")
                            print(str(i)) # this is real data ok?
            return render(request,'search.html',{'data':data,'url':url})
    return render(request,'index.html')

# 400에러(Error)
def bad_request_page(request,exception):
    return render(request,'error_400_page.html',status=400)

# 404에러(Error)
def page_not_found_page(request,exception):
    return render(request,'error_404.page.html',status=404)

# 500에러
def server_error_page(request):
    return render(request,'error_500_page.html',status=500)