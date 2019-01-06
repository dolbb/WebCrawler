# =============================================================================
#           This file handles all prints to console
# =============================================================================
import sys,time

def cleanTerminal():
    print(chr(27) + "[2J")

def inlinePrint(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()
    
def dottedMessage(msg, numOfDots, speed):
    inlinePrint(msg)
    for i in range(numOfDots):
        inlinePrint(".")
        time.sleep(speed)
    
def openingMessage():
    DOTS_NUM = 3
    OM_TIME_BETWEEN_DOTS = .7
    cleanTerminal()
    dottedMessage("Starting Crawler", DOTS_NUM, OM_TIME_BETWEEN_DOTS)
