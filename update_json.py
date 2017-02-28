'''
AUTHOR: Michael Skelton
DATE: 28 February 2017

CREDIT: Generates a json dataset from the public Google Spreadsheet originally created by
Mosh (@nyxbone) and @cyb3rops.

See: http://goo.gl/b9R8DE
'''


import pandas as pd
from pretty_json import formatInput as formatJson
from download_file import download_file

SOURCESHEET = 'https://docs.google.com/spreadsheets/d/1TWS238xacAto-fLKh1n5uTsdijWdCEsGIM0Y0Hvmc5g/pub?output=xlsx'
OUTPUTSHEET = 'RansomwareOverview.xlsx'
JSONFILE = 'RansomwareOverview.json'

def generate_json():
    download_file(SOURCESHEET, OUTPUTSHEET)

    sheet = pd.read_excel(open(OUTPUTSHEET,'rb'), sheetname='Ransomware')

    output = open(JSONFILE, 'w')
    output.writelines(formatJson(sheet.to_json()))

generate_json()