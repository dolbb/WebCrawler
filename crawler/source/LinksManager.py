from html.parser import HTMLParser

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    self.links.add(value)

    def pageLinks(self):
        return self.links

    def error(self, message):
        pass

def getAllLinksFromPage(htmlLink):
    try:
        with open(htmlLink, 'r') as f:
            lf = LinkFinder('',htmlLink)
            lf.feed(f.read())
            f.close()
            return lf.pageLinks()
    except Exception as e:
        print(str(e))
        return set()