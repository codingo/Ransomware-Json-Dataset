import xlrd
from collections import OrderedDict
import simplejson as json
import urllib.request

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

wb = xlrd.open_workbook(OUTPUTSHEET)
sh = wb.sheet_by_index(0)
mw = wb.sheet_by_index(2)
# List to hold dictionaries
c_list = []
	
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
	cars = OrderedDict()
	row_values = sh.row_values(rownum)
	
	
	if row_values[6]=="":
		name = row_values[0]
		gre=[name]
	elif "," in row_values[6]:
		e=row_values[6].split(",")
		ge = [row_values[0]]
		gre=e+ge
	else:
		gre=[row_values[0],row_values[6]]
	print (gre)
	cars['Name'] = gre
	cars['Extensions'] = row_values[1]
	cars['Extension Pattern'] = row_values[2]
	cars['Ransom Note Filename(s)'] = row_values[3]
	cars['Comment'] = row_values[4]
	cars['Encryption Algorithm'] = row_values[5]
	cars['Decryptor'] = row_values[7]
	if row_values[8]=="":
		cars['Resources'] = [row_values[9]]
	elif row_values[9]=="":
		cars['Resources']=[row_values[8]]
	else:
		cars['Resources'] = [row_values[8], row_values[9]]
	cars['Screenshots'] = row_values[10]
	
	for r in range(1, mw.nrows):
		rowe = mw.row_values(r)
		
		if row_values[0] == rowe[0]:
			cars['Microsoft Detection Name']=rowe[1]
			cars['Microsoft Info'] = rowe[2]
			cars['Sandbox'] = rowe[3]
			cars['IOCs'] = rowe[4]
			cars['Snort'] = rowe[5]
	
	c_list.append(cars)

# Serialize the list of dicts to JSON
j = json.dumps(c_list)

# Write to file
with open(JSONFILE, 'w') as f:
	f.write(j)

f.close()
