import os
import sys
import xml.etree.ElementTree as ET
class TreatmentXML(object):
    def __init__(self):
        self.xml_keys = []

    def load_csv_1(self):
        temp_xml_keys = {}
        file_name = os.path.dirname(sys.argv[0]) + "\\data\\xml_data.xml"
        root = ET.parse(file_name).getroot()
        object_xml = root.findall('objects/object')
        text_object = root.findall('objects/object/value')

        for i in range(0, object_xml.__len__()):
            key = object_xml[i].attrib.get("name")
            val = text_object[i].text
            # test_dict.setdefault(key, []).append(val)
            temp_xml_keys.update({key: val})

        self.xml_keys.append(temp_xml_keys.copy())




