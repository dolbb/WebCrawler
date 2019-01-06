# =============================================================================
#           This file handles the system's files
# =============================================================================
import io,os

# -----------------------------------------------------
# file management constants:
# -----------------------------------------------------
DATA_FILE_PATH = '../data/'
DEFAULT_LINKS_FILE = '../data/startingLinks.txt'

# -----------------------------------------------------
# General file management functions:
# -----------------------------------------------------
# Convert a file to a set:
def fileToSet(filePath):
    resultSet = set()
    with io.open(filePath, 'r') as file:
        for line in file:
            resultSet.add(line.replace('\n',''))
        file.close()
    return resultSet

# Convert a set to a file:
def setToFile(linksSet, fileName):
    for link in sorted(linksSet):
       appendToFile(fileName, link)

# -----------------------------------------------------
# Project specific file management functions:
# -----------------------------------------------------
# For each project - make its own dictionary:
def createProjDir(projName):
    directory = DATA_FILE_PATH + projName
    if not os.path.exists(directory):
        print("Creating project: " + projName + '!')
        os.makedirs(directory)

# For a specific project - Create queue\crawled files
def createDataFiles(projName, baseUrl = ''):
    queue   = getQueueFilePath(projName)
    crawled = getCrawledFilePath(projName)
    #if not os.path.isfile(queue):
    overwriteFileWithData(queue, baseUrl)
    #if not os.path.isfile(crawled):
    overwriteFileWithData(crawled, '')
    if baseUrl == '':
        setToFile(fileToSet(DEFAULT_LINKS_FILE), queue)

def getQueueFilePath(projName):
    return DATA_FILE_PATH + projName + '/queue.txt'

def getCrawledFilePath(projName):
    return DATA_FILE_PATH + projName + '/crawled.txt'

# Overwrite a file with specific data:
def overwriteFileWithData(path, data):
    f = io.open(path, 'w+')
    f.write(data)
    f.close()

# add data to a file:
def appendToFile(path,data):
    with io.open(path, 'a+') as file:
        file.write(data + '\n')
        file.close()

def flushFile(path):
    overwriteFileWithData(path,'')


