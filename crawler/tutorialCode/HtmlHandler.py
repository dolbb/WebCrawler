# =============================================================================
#           This file will do every HTML handling needed for the crawler
# =============================================================================
from html.parser import HTMLParser
from urllib import parse

# define linkFinder with inheritance from HTMLParser.
class linkFinder(HTMLParser):
    
    def __init__(self, base_url, page_url):
        super.__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.link = set()

    # when calling HTMLParser.feed() it will call this function for each tag
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
                    
    def page_links(self):
        return self.links
                    
    def error(self,message):
        pass
                        