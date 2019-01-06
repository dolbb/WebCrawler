# =============================================================================
#     spider class will crawl simultaneously with other spiders in pages
# =============================================================================
import FileManager
from urllib.request import urlopen
from HtmlHandler import LinkFinder
#from FileManager import *

class Spider:
#   class shared variables:    
    #in-app data management:
    projName    = ''
    baseUrl     = ''
    domainName  = ''
    queue   = set()
    crawled = set()    
    #database management:
    queueFile   = ''
    crawledFile = ''

#   class instances definitions and funcs:   
    def __init__(self, projName, baseUrl, domainName):
       Spider.projName    = projName  
       Spider.baseUrl     = baseUrl  
       Spider.domainName  = domainName    
       Spider.queueFile   = Spider.projName + '/queue.txt'
       Spider.crawledFile = Spider.projName + '/crawled.txt'
       Spider.boot()
       Spider.crawlPage('FirstSpider', Spider.baseUrl)

    def boot(self):
      FileManager.createProjDir(Spider.projName)
      createDataFile(Spider.projName, Spider.baseUrl)
      Spider.queue = filesToSet(Spider.queueFile)
      Spider.crawled = filesToSet(Spider.crawledFile)

       