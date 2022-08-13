from html.parser import HTMLParser
class MyHTMLPraser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for ele in attrs:
            print('->', ele[0], '>', ele[1])
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for ele in attrs:
            print('->', ele[0], '>', ele[1])
parser=MyHTMLPraser()
for _ in range(int(input())):
    parser.feed(input())
            