from html.parser import HTMLParser
class MyHTMLPraser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr,value in attrs:
            print("->", attr, ">",value)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">",value)
html=''
for i in range(int(input())):
    html +=input().strip()+ '\n'
parser=MyHTMLPraser()
parser.feed(html)
parser.close()