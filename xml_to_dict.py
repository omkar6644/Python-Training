#import xmltodict
import xmltodict

#open a xml file
with open('json_to_xml.xml')as f:
    #convert xml to dict
    dict=xmltodict.parse(f.read())
print(dict)
