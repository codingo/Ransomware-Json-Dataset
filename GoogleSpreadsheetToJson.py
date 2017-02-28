'''
AUTHOR: Michael Skelton
DATE: 28 February 2017

CREDIT: Generates a json dataset from the public Google Spreadsheet originally created by
Mosh (@nyxbone) and @cyb3rops.

See: http://goo.gl/b9R8DE
'''


import urllib.request
import pandas as pd
from prettyJSON import formatInput as formatJson

SOURCESHEET = 'https://docs.google.com/spreadsheets/d/1TWS238xacAto-fLKh1n5uTsdijWdCEsGIM0Y0Hvmc5g/pub?output=xlsx'
OUTPUTSHEET = 'RansomwareOverview.xlsx'
JSONFILE = 'RansomwareOverview.json'

# download and save ransomware overview file locally
try:
    urllib.request.urlretrieve(SOURCESHEET, OUTPUTSHEET)
except IOError:
    print('An error occured trying to write an updated spreadsheet. Do you already have it open?')
except urllib.error.URLError:
    print('An error occured trying to download the file. Please check the source and try again.')

sheet = pd.read_excel(open(OUTPUTSHEET,'rb'), sheetname='Ransomware')

output = open(JSONFILE, 'w')
output.writelines(formatJson(sheet.to_json()))
