# Ransomware-Resources
A collection of resources to help in the detection, mitigation and prevention of ransomware.

##JSON Dataset

JSON dataset work is based upon the many efforts of Mosh (@nyxbone) and @cyb3rops who manage the Ransomware Summary public spreadsheet that is co-hosted in this repository but originally sourced on Google docs at http://goo.gl/b9R8DE. Spreadsheet data remains the intellectual property of Mosh and is taken 'as-is' and processed into a JSON output to allow its use in various shell or programming operations. Spreadsheet is cloned within this repository for redundancy purposes.

###Updating the dataset
To update the dataset first clone this repository and then run 'python ./UpdateJsonDataset/update_json.py'

The latest version of the Ransomware Summary spreadsheet will then be downloaded and processed into a local json output which will be found in the core folder of your local repository along with a copy of the latest version of the spreadsheet. To change the source and destinations for local files edit the constants found in the header of the 'update_json.py' file.
