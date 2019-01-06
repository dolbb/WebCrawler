import FileManager
import MyPrints
import LinksManager
import time

class Crawler:

    # crawler management:
    projName = ''
    startingTime = 0
    queue = set()
    crawled = set()
    finishedFlag = False

    # database management:
    queueFile = ''
    crawledFile = ''

    # initialization methods:
    def __init__(self, projName):
        self.projName       = projName
        self.queueFile      = FileManager.getQueueFilePath(projName)
        self.crawledFile    = FileManager.getCrawledFilePath(projName)
        self._initProject()

    def _initProject(self):
        proj = self.projName
        FileManager.createProjDir(proj)
        FileManager.createDataFiles(proj)
        MyPrints.openingMessage(proj)

    # crawling command - seconds is the runtime top limit:
    def crawl(self, secondsToRun = 1):
        self.startingTime = time.time()
        # Iterate for as long as wanted or until finished:
        while secondsToRun > time.time() - self.startingTime and not self.finishedFlag:
            # Get all queued links from file to set:
            self.queue = FileManager.fileToSet(self.queueFile)
            if len(self.queue) == 0:
                self.finishedFlag = True
            # Clear the queue file:
            FileManager.flushFile(self.queueFile)
            # For each link in the queue set:
            for link in self.queue:
                # Get all links inside current link's page, and save to queue file:
                FileManager.setToFile(LinksManager.getAllLinksFromPage(link), self.queueFile)
                # Save current link to crawled set:
                self.crawled.add(link)
            # Save crawled set into file:
            FileManager.setToFile(self.crawled, self.crawledFile)
            # Clear the crawled set from links:
            self.crawled.clear()
        tmpSet = FileManager.fileToSet(self.crawledFile)
        FileManager.flushFile(self.crawledFile)
        FileManager.flushFile(self.queueFile)
        FileManager.setToFile(tmpSet, self.crawledFile)
