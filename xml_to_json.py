#import json
import json
#import xmltodict
import xmltodict

#open a xml file 
with open('json_to_xml.xml') as f:
    #convert xml to dictionary
    data = xmltodict.parse(f.read())
f.close()

#convert dictionary to json 
json_data=json.dumps(data)
print(json_data)
