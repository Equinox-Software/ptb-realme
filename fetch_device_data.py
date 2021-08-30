import urllib
from collections import OrderedDict

from bs4 import BeautifulSoup

from constants import MODELS


def sort_models():
    print(str(dict(OrderedDict(sorted(MODELS.items(), key=lambda t: t[0])))).replace("(", "").replace(")", ""))


def fetch_device_data():
    searchlist = ["galaxy note", "nexus 10", "nexus 5", "galaxy ace", "moto g", "galaxy tab 2", "MID-97D"]
    for searchstr in searchlist:
        other = False
        searchstr = searchstr.replace(" ", "%20")
        searchlink = "http://www.gsmarena.com/results.php3?sQuickSearch=yes&sName=" + searchstr
        string = urllib.request.urlopen(searchlink).read().decode("ISO-8859-1")
        soup = BeautifulSoup(string, "lxml")
        if soup.title.string == "Phone Finder results - GSMArena.com":
            makerdiv = soup.find_all('div', attrs={'class': 'makers'})
            links = makerdiv[0].find_all('a')
            if len(links) != 0:
                link = "http://www.gsmarena.com/" + links[0].attrs['href']
                string = urllib.request.urlopen(link).read().decode("ISO-8859-1")
                soup = BeautifulSoup(string, "lxml")
            else:
                other = True
        if not other:
            title = soup.title.string
            name = title.split("-")[0]
            rest = title.split("-")[1]
            taborphone = rest.split(" ")[2]
        else:
            name = searchstr
            taborphone = "other"
        print("Name:", name)
        print("Type:", taborphone)


if __name__ == '__main__':
    sort_models()
