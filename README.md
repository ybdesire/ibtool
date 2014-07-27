ibtool
=========

Mac tool ibtool for windows platform
Written by Python(3.1.4)

##### 1. *.xib to *.strings
```
ibtool.py --generate-strings-file destFile.xib.strings resFile.xib
```
Extract the UI strings at 'resFile.xib' to 'destFile.xib.strings'.

##### 2. *.strings to *.xib
```
ibtool.py --strings-file translated.xib.strings  --write en\enResFile.xib destL10nFile.xib  
```
Create a localized file with the translation at 'translated.xib.strings' and template at 'en\enResFile.xib'

Attention: this tool cannot replace Mac ibtool since it only extract the hard code strings marked with "NSContents" up to now.