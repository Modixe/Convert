from Basic import BasicTsv
from ReadCsv import TreatmentCsv_1
from ReadJson import TreatmentJson
from ReadXml import TreatmentXML
from ReadYaml import TreatmentYaml

class PointOfEntry(object):
    def __init__(self):
        self.json = TreatmentJson()
        self.json.load()
        self.csv_1 = TreatmentCsv_1()
        self.csv_1.load_csv_1()
        self.csv_1.load_csv_2()
        self.xml = TreatmentXML()
        self.xml.load_csv_1()
        self.yaml = TreatmentYaml()
        self.yaml.load_yaml()
        # self.assembly_tuple(self.csv_1)

        self.basic_tsv = BasicTsv(self.json, self.csv_1, self.xml)


if __name__ == "__main__":
    window = PointOfEntry()
