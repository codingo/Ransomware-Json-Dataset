import simplejson as json
import xlrd
from collections import OrderedDict


def excel_to_json(filename):
    workbook = xlrd.open_workbook(filename)
    ransomware_sheet = workbook.sheet_by_index(0)
    detection_sheet = workbook.sheet_by_index(2)

    # List to hold dictionaries
    c_list = []

    # Iterate through each row in worksheet and fetch values into dict
    for rownum in range(1, ransomware_sheet.nrows):
        wares = OrderedDict()
        row_values = ransomware_sheet.row_values(rownum)

        if row_values[6] == "":
            name = row_values[0]
            gre = [name]
        elif "," in row_values[6]:
            e = row_values[6].split(",")
            ge = [row_values[0]]
            gre = e+ge
        else:
            gre = [row_values[0], row_values[6]]

        wares['name'] = gre
        wares['extensions'] = row_values[1]
        wares['extensionPattern'] = row_values[2]
        wares['ransomNoteFilenames'] = row_values[3]
        wares['comment'] = row_values[4]
        wares['encryptionAlgorithm'] = row_values[5]
        wares['decryptor'] = row_values[7]
        if row_values[8] == "":
            wares['resources'] = [row_values[9]]
        elif row_values[9] == "":
            wares['resources'] = [row_values[8]]
        else:
            wares['resources'] = [row_values[8], row_values[9]]
        wares['screenshots'] = row_values[10]

        for r in range(1, detection_sheet.nrows):
            rowe = detection_sheet.row_values(r)

            if row_values[0] == rowe[0]:
                wares['microsoftDetectionName'] = rowe[1]
                wares['microsoftInfo'] = rowe[2]
                wares['sandbox'] = rowe[3]
                wares['iocs'] = rowe[4]
                wares['snort'] = rowe[5]

        c_list.append(wares)

    # Serialize the list of dicts to JSON
    return json.dumps(c_list, indent=4)
