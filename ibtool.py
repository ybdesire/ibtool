import xml.etree.ElementTree as ET
import sys
import os

__author__ = 'Bin YIN'
__email__ = 'ybdesire@gmail.com'

def parsePara():
    if sys.argv[1]=="--generate-strings-file":
        xibToStrings(sys.argv[2], sys.argv[3])
    elif sys.argv[1]=="--strings-file" and sys.argv[3]=="--write":
        print "not support --strings-file now"
    else:
        print "wrong useage"

def xibToStrings(stringsFileDestPath, xibSourcePath):
    #create a file with encoding "UTF8 without BOM" for support Mac *.strings file format
    #override the file if exist
    stringsFilePath = os.path.split(stringsFileDestPath)[0]
    stringsFileName = os.path.split(stringsFileDestPath)[1]
    if stringsFilePath != "":#if not at current working directory
        if not os.path.exists(stringsFilePath):#if path not exists
            os.makedirs(stringsFilePath)
    stringsFile = open(stringsFileDestPath,'w')
    #parse the *.xib file and extract all the strings to the cteated *.strings file
    tree = ET.parse(xibSourcePath)
    root = tree.getroot()
    for string in root.iter("string"):
        value = string.get("key")
        if value == "NSContents":
            if string.text is not None:
                stringsFile.write('\"' + string.text +'\"' + '=' + '\"' + string.text + '\"' + ';\r');#'\r' for Mac

def test():
    xibFile = sys.argv[1]
    tree = ET.parse(xibFile)
    root = tree.getroot()
    for string in root.iter("string"):
        value = string.get("key")
        if value == "NSContents":
            if string.text is not None:
                print string.text

if __name__=='__main__':
    parsePara()


