import xml.etree.ElementTree as ET
import sys
import os
import codecs


__author__ = 'Bin YIN'
__email__ = 'ybdesire@gmail.com'

def parsePara():
    if sys.argv[1]=="--generate-strings-file":
        xibToStrings(sys.argv[2], sys.argv[3])
    elif sys.argv[1]=="--strings-file" and sys.argv[3]=="--write":
        stringsToXib(sys.argv[2], sys.argv[4], sys.argv[5])
    else:
        print("wrong useage")

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
    stringsFile.close()
                
def stringsToXib(stringsFileSrcPath, enXibFileSrcPath, l10nXibFileDestPath):
    l10nXibFilePath = os.path.split(l10nXibFileDestPath)[0]
    l10nXibFileName = os.path.split(l10nXibFileDestPath)[1]
    if l10nXibFilePath != "":#if not at current working directory
        if not os.path.exists(l10nXibFilePath):#if path not exists
            os.makedirs(l10nXibFilePath)
    l10nXibFile = open(l10nXibFileDestPath,'w', encoding="utf-8")
    enXibFile = open(enXibFileSrcPath, 'r', encoding="utf-8")
    #parse the *.strings file and creat an dictionary
    stringsFile = open(stringsFileSrcPath, 'rU', encoding="utf-8")#'rU' for mac end-of-line '\r'
    stringsDict = dict()
    for line in stringsFile:
        key = line.split("=")[0].replace("\"","")
        value = line.split("=")[1].replace("\"","").replace(";", "").rstrip('\n')
        stringsDict[key] = value
    
    #parse the EN src xib file
    tree = ET.parse(enXibFileSrcPath)
    root = tree.getroot()
    for string in root.iter("string"):
        value = string.get("key")
        if value == "NSContents":
            if string.text is not None and string.text in stringsDict:
                string.text = stringsDict[string.text]
    tree.write(l10nXibFileDestPath, encoding="utf-8",xml_declaration=True)
    l10nXibFile.close()           

def parseXibAndGetStrings():
    xibFile = sys.argv[1]
    tree = ET.parse(xibFile)
    root = tree.getroot()
    for string in root.iter("string"):
        value = string.get("key")
        if value == "NSContents":
            if string.text is not None:
                print(string.text)

def test():
    stringsFile = open("test.txt", 'rU')
    stringsFile.seek(0)
    for line in stringsFile:
        print(line)
    stringsFile.close()

def fileSupportUnicode():
    #reload(sys)
    #sys.setdefaultencoding( "utf-8" )

    stringsFile = open("SFConfigWizardViewController.xib.strings", 'rU', encoding="utf-8")
    stringsDict = dict()
    for line in stringsFile:
        print(line)
        key = line.split("=")[0].replace("\"","")
        value = line.split("=")[1].replace("\"","").replace(";", "").replace("\r", "")
        print("key:value: " + key + ":" + value)
        stringsDict[key]=value
    destFile = open("testSC.xml", "w", encoding="utf-8")
    destFile.write(stringsDict["Go Back"])
    print(stringsDict["Go Back"])
    whatisthis(stringsDict["Go Back"])

def whatisthis(s):
    if isinstance(s, str):
        print("ordinary string")
    elif isinstance(s, unicode):
        print("unicode string")
    else:
        print("not a string")
        
if __name__=='__main__':
    parsePara()


