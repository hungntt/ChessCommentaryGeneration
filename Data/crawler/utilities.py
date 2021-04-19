import urllib2
from bs4 import BeautifulSoup


class Utilities:
    @staticmethod
    def getSoupFromURL(url):
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)
        page = urllib2.urlopen(req)
        html_doc = page.read()
        soup = BeautifulSoup(html_doc, "lxml")
        return soup

    @staticmethod
    def getSoupFromHTML(html_doc):
        soup = BeautifulSoup(html_doc, "lxml")
        return soup

    @staticmethod
    def soupToText(ele):
        tmp = [s.extract() for s in ele(['style', 'script', '[document]', 'head', 'title'])]
        return ele.get_text()

    @staticmethod
    def getDivOfClass(soup, class_value, recursive=True):
        mydivs = soup.findAll("div", {"class": class_value}, recursive=recursive)
        return mydivs

    @staticmethod
    def getDivAll(soup, recursive=True):
        mydivs = soup.findAll("div", recursive=recursive)
        return mydivs

    @staticmethod
    def getTableOfClass(soup, class_value, recursive=True):
        mydivs = soup.findAll("table", {"class": class_value}, recursive=recursive)
        return mydivs

    @staticmethod
    def getImgAll(soup):
        mydivs = soup.findAll("img")
        return mydivs

    @staticmethod
    def getDivOfID(soup, id_value, recursive=True):
        mydivs = soup.findAll("div", {"id": id_value}, recursive=recursive)
        return mydivs

    @staticmethod
    def getHREF(soup, class_value):
        mydivs = soup.findAll("div", {"class": class_value})
        ret = []
        for mydiv in mydivs:
            mydiv_a = mydiv.find("a", {"class": "rg_l"})
            ret.append(mydiv_a['href'])
        return ret

    @staticmethod
    def getAsciiOnly(txt):
        ret = ''.join([ch for ch in txt if ord(ch) <= 128])
        return ret


'''
	def getTextClass(self,url):
		soup = self.getSoup(url)
		mydivs = soup.findAll("div", { "class" : "section-inner layoutSingleColumn" })
		ret = ""
		for mydiv in mydivs:
			ret = ret + soupToText(mydiv)
		return ret
'''
