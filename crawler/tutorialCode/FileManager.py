# =============================================================================
#           This file handles the system's files
# =============================================================================
import os

def createProjDir(directory):
    if not os.path.exists(directory):
        print("Creating project dyrectory: " + directory)
        os.makedirs(directory)

def createDataFile(projPath, baseUrl):
    queue = projPath + '/queue.txt'
    crawled = projPath + '/crawled.txt'
    if not os.path.isfile(queue):
        writeFile(queue, baseUrl)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')
    
def writeFile(path, data):
    f = open(path, 'w+')
    f.write(data)
    f.close()
    
def appendToFile(path,data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        file.close()

def flushFile(path):
    open(path, 'w')
        
def fileToSet(fileName):
    results = set()
    with open(fileName, "r") as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

def setToFile(linksSet, fileName):
    flushFile(fileName)
    for link in sorted(linksSet):
       appendToFile(fileName, link)
     