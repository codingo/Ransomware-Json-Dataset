import simplejson as json
import xlrd
from collections import OrderedDict

def formatJson(input):
    return json.dumps(json.loads(input), indent=4)

def excel_to_json(filename):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(0)

    # List to hold dictionaries
    c_list = []

    # Iterate through each row in worksheet and fetch values into dict
    for rownum in range(1, sh.nrows):
        cars = OrderedDict()
        row_values = sh.row_values(rownum)
        cars['Name'] = row_values[0]
        cars['Extensions'] = row_values[1]
        cars['Patterns'] = row_values[2]
        cars['RansomNoteFilenames'] = row_values[3]
        cars['Comment'] = row_values[4]
        cars['EncryptionAlgorithm'] = row_values[5]
        cars['AlternateNames'] = row_values[6]
        cars['Decryptor'] = row_values[7]
        cars['AdditionalInfo1'] = row_values[8]
        cars['AdditionalInfo2'] = row_values[9]
        cars['Screenshots'] = row_values[10]

        c_list.append(cars)

    # Serialize the list of dicts to JSON
    return formatJson(json.dumps(c_list))