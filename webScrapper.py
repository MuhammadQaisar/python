import re # Regular Expression Library
from urllib.request import urlopen # URL Library
url = "https://propakistani.pk/2021/05/03/fbr-raises-customs-of-mg-vehicles-by-14-5-percent/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

text = []

def Title_Pattern(): # Function for Title tag Pattern
    title_pattern = re.findall(r'<title>(.*?)</title>', str(html))
    for eachT in title_pattern:
        text.append(eachT)
        print(eachT)
        
        
Title_Pattern()
   
def Header_Pattern(): # Function for Header tag Pattern
    header_pattern = re.findall(r'<h1>(.*?)</h1>', str(html))
    for eachH in header_pattern:
        print(eachH)
    
Header_Pattern()

def Paragragh_pattern(): # Function for Paragraph tag Pattern
    paragraph_pattern = re.findall(r'<p>(.*?)</p>', str(html))
    for eachP in paragraph_pattern:
        text.append(eachP)
        print(eachP)
        
Paragragh_pattern()
           
with open("newfile.txt", "w") as output:
            output.writelines(text)
output.close()
