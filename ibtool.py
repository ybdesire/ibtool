import xml.etree.ElementTree as ET
import sys

__author__ = 'Bin YIN'
__email__ = 'Bin.Yin@citrix.com'


def main():
    xibFile = sys.argv[1]
    tree = ET.parse(xibFile)
    root = tree.getroot()
    for string in root.iter('string'):
        value = string.get('key')
        if value == "NSContents":
            if string.text is not None:
                print string.text

if __name__=='__main__':
    main()


