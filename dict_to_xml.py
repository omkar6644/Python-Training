#import dicttoxml
from dicttoxml import dicttoxml
dict = {"Team": "CSK", "Captain": "Dhoni", "Players":[{"Name": "Ms Dhoni", "Jersy No": 7},
                                                      {"Name": "Raina", "Jersy No": 3},
                                                      {"Name": "Jadeja", "Jersy No": 20},
                                                {"Name": "Du Plessis", "Jersy No": 13}]}

#convert dict to xml
xml=dicttoxml(dict)
#open or create a xml file in write mode
xmlfile = open("ipl_xml.xml", "w")
xmlfile.write(xml.decode())
xmlfile.close()