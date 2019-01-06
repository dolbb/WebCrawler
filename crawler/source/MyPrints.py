# =============================================================================
#           This file handles all prints to console
# =============================================================================
import sys,time

def openingMessage(projName):
    aux_opening_2(projName)

def aux_opening_1():
    DOTS_NUM = 3
    OM_TIME_BETWEEN_DOTS = .5
    cleanLastTerminalPrint()
    dottedMessage("Starting Crawler", DOTS_NUM, OM_TIME_BETWEEN_DOTS)

def aux_opening_2(projName):
    inlinePrint('project ' + projName + ' initialized.' )

def cleanLastTerminalPrint():
    print(chr(27) + "[2J")
    
def inlinePrint(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    
def dottedMessage(msg, numOfDots, speed):
    inlinePrint(msg)
    for i in range(numOfDots):
        inlinePrint(".")
        time.sleep(speed)
