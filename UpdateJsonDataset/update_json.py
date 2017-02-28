'''
AUTHOR: Michael Skelton
DATE: 28 February 2017

CREDIT: Generates a json dataset from the public Google Spreadsheet originally created by
Mosh (@nyxbone) and @cyb3rops.

See: http://goo.gl/b9R8DE
'''

from generate_json import excel_to_json
from download_file import download_file

SOURCESHEET = 'https://docs.google.com/spreadsheets/d/1TWS238xacAto-fLKh1n5uTsdijWdCEsGIM0Y0Hvmc5g/pub?output=xlsx'
OUTPUTSHEET = '../RansomwareOverview.xlsx'
JSONFILE = '../RansomwareOverview.json'

def write_json_file(input, filename):
    output = open(filename, 'w')
    output.writelines(input)



def generate_json(source_file, download_destination, json_file):
    download_file(source_file, download_destination)
    write_json_file(excel_to_json(download_destination), json_file)

generate_json(SOURCESHEET, OUTPUTSHEET, JSONFILE)