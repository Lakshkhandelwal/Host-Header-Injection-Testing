import pycurl
from io import BytesIO
import certifi
from urllib.parse import urlparse
import socket
import os

def check_connectivity(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((str(host), int(port)))
        s.close()
    except socket.timeout:
        print("Failed to connect to %s:%s" %(host,port))
        return False
    except:
        print("Failed to connect to %s:%s" % (host, port))
        return False
    return True


output = open(os.getcwd()+"\output.csv","w")
output.write("URL,Response Code,Header Injection Count,Result")
output.write("\n")
inputfile = str(input("Enter the file path for the input File: "))
urllist = open(inputfile,"r")

for url in urllist:
    print(url)
    if not url.strip():
        print("Input Line is empty")
    else:
        url = url.strip()
        port = 80
        if urlparse(url)[0] == "https":
            port = 443
        elif urlparse(url)[0] == "http":
            port = 80
        if check_connectivity(urlparse(url)[1],port):
            try:
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(pycurl.CONNECTTIMEOUT, 30)
                c.setopt(pycurl.CAINFO, certifi.where())
                c.setopt(c.URL,str(url))
                c.setopt(pycurl.HTTPHEADER, ['Host: abcdtest1234567890'])
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                code = c.getinfo(pycurl.RESPONSE_CODE)
                c.close()
                the_page = buffer.getvalue()
                ustring = the_page.decode('iso-8859-1')
                count = ustring.count("abcdtest1234567890")
                if(count == 0):
                    output.write(str(url)+","+str(code)+","+str(count)+","+"Host Header Injection Not Successful")
                    output.write("\n")
                else:
                    output.write(str(url)+","+str(code)+","+str(count)+","+"Host Header Injection Successful")
                    output.write("\n")
            except:
                try:
                    count = 0
                    output.write(str(url)+","+str(code)+","+str(count)+","+"Host Header Injection Not Successful")
                    output.write("\n")
                except:
                    print("File System Error")
        else:
            try:
                count = 0
                output.write(str(url)+","+str(code)+","+str(count)+","+"Couldn't Connect to the URL")
                output.write("\n")
            except:
                print("File System Error")      
output.close()
urllist.close()
