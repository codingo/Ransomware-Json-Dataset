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

def write_json_file(input, filename):
    output = open(filename, 'w')
    output.writelines(formatJson(sheet.to_json()))

def excel_to_json(filename):
    return pd.read_excel(open(filename,'rb'), sheetname='Ransomware')

def generate_json():
    download_file(SOURCESHEET, OUTPUTSHEET)
    write_json_file(excel_to_json(OUTPUTSHEET), JSONFILE)

generate_json()