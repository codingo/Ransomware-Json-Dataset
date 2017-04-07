'''
AUTHOR: Michael Skelton
DATE: 28 February 2017

CREDIT: Generates a json dataset from the public 
Google Spreadsheet originally created by
Mosh (@nyxbone) and @cyb3rops.

See: http://goo.gl/b9R8DE
'''

from excel_to_json import excel_to_json
from download_file import download_file
from validate_json import is_json

SOURCESHEET = 'https://docs.google.com/spreadsheets' + \
                '/d/1TWS238xacAto-fLKh1n5uTsdijWdCEsGIM0Y0Hvmc5g/pub?output=xlsx'
OUTPUTSHEET = '../RansomwareOverview.xlsx'
JSONFILE = '../ransomware_overview.json'

def print_banner():
     print(' ____                                                         ____        _                 _   ')
     print('|  _ \ __ _ _ __  ___  ___  _ __ _____      ____ _ _ __ ___  |  _ \  __ _| |_ __ _ ___  ___| |_ ')
     print('| |_) / _` | \'_ \/ __|/ _ \| \'_ ` _ \ \ /\ / / _` | \'__/ _ \ | | | |/ _` | __/ _` / __|/ _ \ __|')
     print('|  _ < (_| | | | \__ \ (_) | | | | | \ V  V / (_| | | |  __/ | |_| | (_| | || (_| \__ \  __/ |_ ')
     print('|_| \_\__,_|_| |_|___/\___/|_| |_| |_|\_/\_/ \__,_|_|  \___| |____/ \__,_|\__\__,_|___/\___|\__|')
     print('Authored by Michael \'codingo\' Skelton (michael@codingo.com.au)')
     print('Generates a json dataset of known ransomware from the public Google Spreadsheet originally created by Mosh (@nyxbone) and @cyb3rops.')
def write_json_file(json_data, filename):
    print('[-] Writing file...')
    output = open(filename, 'w')
    output.writelines(json_data)

def generate_json(source_file, download_destination, json_file):
    print('[-] Downloading source spreadsheet...')
    download_file(source_file, download_destination)
    print('[-] Generating json file...')
    write_json_file(excel_to_json(download_destination), json_file)

def main():
    print_banner()
    generate_json(SOURCESHEET, OUTPUTSHEET, JSONFILE)
    print('[-] Validating json file...')
    print('Debug: ' + JSONFILE)
    if(is_json(JSONFILE)):
        print('[-] Successfully generated an updated dataset.')
    else:
        print('[-] Unable to validate json datafile, please review the sourcesheet and output.')
main()