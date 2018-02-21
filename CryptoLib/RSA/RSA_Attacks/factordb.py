import requests
from bs4 import BeautifulSoup 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

status = {"C" :"Composite, no factors known",
         "CF":"Composite, factors known",
         "FF":"Composite, fully factored" ,
         "P" : "Definitely prime" ,
         "Prp": "Probably prime" ,
         "U" : "Unknown" ,
         "Unit": "Just for 1" ,
         "N" : "This number is not in database (and was not added due to your settings)" ,
         "*" : "Added to database during this request"}

baseUrl = "https://factordb.com/"



def interact(n):
    myVars = []
    r = requests.get(baseUrl+"index.php?query="+n,verify=False)
    html = r.content
    mylist =[]
    soup = BeautifulSoup(html,"lxml")
    tables = soup.findAll("table")
    for table in tables:
         if table.findParent("table") is None:
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                mylist.append(str(cells))
    data = mylist[3]
    data = data.split(",")
    soup2 = BeautifulSoup(data[0],"lxml")
    for row in soup2.findAll("td"):
        status = row.text

    links = []
    soupLinks = BeautifulSoup(data[2],"lxml")
    for row in soupLinks.findAll("a"):
        links.append(row["href"])
    l = len(links)
    myVars.append([status,links[l-2],links[l-1]])
    return myVars
def get_prime(p):
    r = requests.get(baseUrl+p,verify=False)
    html = r.content
    soup = BeautifulSoup(html,"lxml")
    try:
        value = soup.find('input', {'name': 'query'}).get('value')
        return value
    except:
        return False

        
def factordb(n):
    try:
        s,p,q = interact(str(n))[0]
        P = get_prime(p)
        Q = get_prime(q)
        return {'q':Q,'p':P,'status':str(s)}
    except Exception as e:
        print "[!] {E}\n[*] Internal Error ..".format(E=e)
