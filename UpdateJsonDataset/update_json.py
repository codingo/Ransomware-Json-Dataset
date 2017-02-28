'''
AUTHOR: Michael Skelton
DATE: 28 February 2017

CREDIT: Generates a json dataset from the public Google Spreadsheet originally created by
Mosh (@nyxbone) and @cyb3rops.

See: http://goo.gl/b9R8DE
'''

import pandas as pd
import simplejson as json
import xlrd
from collections import OrderedDict

from pretty_json import formatInput as formatJson
from download_file import download_file

SOURCESHEET = 'https://docs.google.com/spreadsheets/d/1TWS238xacAto-fLKh1n5uTsdijWdCEsGIM0Y0Hvmc5g/pub?output=xlsx'
OUTPUTSHEET = '../RansomwareOverview.xlsx'
JSONFILE = '../RansomwareOverview.json'

def write_json_file(input, filename):
    output = open(filename, 'w')
    output.writelines(input)

def excel_to_json(filename):
    wb = xlrd.open_workbook(OUTPUTSHEET)
    sh = wb.sheet_by_index(0)

    # List to hold dictionaries
    c_list = []

    # Iterate through each row in worksheet and fetch values into dict
    for rownum in range(1, sh.nrows):
        cars = OrderedDict()
        row_values = sh.row_values(rownum)
        cars['RansomwareName'] = row_values[0]
        cars['KnownExtensions'] = row_values[1]
        cars['KnownPatterns'] = row_values[2]
        cars['RansomNoteFilenames'] = row_values[3]
        cars['Comment'] = row_values[4]
        cars['EncryptionAlgorithm'] = row_values[5]
        cars['AlsoKnownAs'] = row_values[6]
        cars['Decryptor'] = row_values[7]
        cars['AdditionalInfo1'] = row_values[8]
        cars['AdditionalInfo2'] = row_values[9]
        cars['Screenshots'] = row_values[10]

        c_list.append(cars)

    # Serialize the list of dicts to JSON
    return formatJson(json.dumps(c_list))

def generate_json(source_file, download_destination, json_file):
    download_file(source_file, download_destination)
    write_json_file(excel_to_json(download_destination), json_file)

generate_json(SOURCESHEET, OUTPUTSHEET, JSONFILE)