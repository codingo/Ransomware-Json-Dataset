import simplejson as json
import xlrd
from collections import OrderedDict

def excel_to_json(filename):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(0)

    # List to hold dictionaries
    c_list = []

    # Iterate through each row in worksheet and fetch values into dict
    for rownum in range(1, sh.nrows):
        wares = OrderedDict()
        row_values = sh.row_values(rownum)
        wares['Name'] = row_values[0]
        wares['AlternateNames'] = row_values[6]
        wares['Extensions'] = row_values[1]
        wares['Patterns'] = row_values[2]
        wares['RansomNoteFilenames'] = row_values[3]
        wares['Comment'] = row_values[4]
        wares['EncryptionAlgorithm'] = row_values[5]
        wares['Decryptor'] = row_values[7]
        wares['AdditionalInfo1'] = row_values[8]
        wares['AdditionalInfo2'] = row_values[9]
        wares['Screenshots'] = row_values[10]

        c_list.append(wares)

    # Serialize the list of dicts to JSON
    return json.dumps(c_list, indent=4)