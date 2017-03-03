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
        ransomware_values = ransomware_sheet.row_values(rownum)

        if ransomware_values[6] == "":
            name = ransomware_values[0]
            gre = [name]
        elif "," in ransomware_values[6]:
            e = ransomware_values[6].split(",")
            ge = [ransomware_values[0]]
            gre = e+ge
        else:
            gre = [ransomware_values[0], ransomware_values[6]]

        wares['name'] = gre
        wares['extensions'] = ransomware_values[1]
        wares['extensionPattern'] = ransomware_values[2]
        wares['ransomNoteFilenames'] = ransomware_values[3]
        wares['comment'] = ransomware_values[4]
        wares['encryptionAlgorithm'] = ransomware_values[5]
        wares['decryptor'] = ransomware_values[7]
        if ransomware_values[8] == "":
            wares['resources'] = [ransomware_values[9]]
        elif ransomware_values[9] == "":
            wares['resources'] = [ransomware_values[8]]
        else:
            wares['resources'] = [ransomware_values[8], ransomware_values[9]]
        wares['screenshots'] = ransomware_values[10]

        for r in range(1, detection_sheet.nrows):
            detection_values = detection_sheet.row_values(r)

            if ransomware_values[0] == detection_values[0]:
                wares['microsoftDetectionName'] = detection_values[1]
                wares['microsoftInfo'] = detection_values[2]
                wares['sandbox'] = detection_values[3]
                wares['iocs'] = detection_values[4]
                wares['snort'] = detection_values[5]

        c_list.append(wares)

    # Serialize the list of dicts to JSON
    return json.dumps(c_list, indent=4)
