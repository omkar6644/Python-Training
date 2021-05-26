#import json
import json as j

#import xmlTree
import xml.etree.cElementTree as e
#open a json file in read mode
with open("ipl.json") as json_format_file: 
  d = j.load(json_format_file)

#create Root
r = e.Element("IPL")
#Create Subelement
e.SubElement(r,"Team").text = d["Team"]
e.SubElement(r,"Captain").text = d["Captain"]
e.SubElement(r,"Home").text = str(d["Home"])
e.SubElement(r,"Cups").text = str(d["Cups"])

#build xml tree
a = e.ElementTree(r)
#create a xml file
a.write("json_to_xml.xml")