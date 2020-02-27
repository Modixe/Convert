import csv
import os
import sys


class AdvancedTsv(object):
    def __init__(self, json_data=None, csv_data=None, xml_data=None):

        self.all_data_list = []
        self.csv1_keys = csv_data.csv1_list
        self.csv2_keys = csv_data.csv2_list
        self.json_keys = json_data.fields
        self.xml_keys = xml_data.xml_keys

        self.all_keys()
        self.summ_values()
        self.ass_json()

    def all_keys(self):
        self.all_keys_list = []
        csv1_keys_list = self.csv1_keys
        csv2_keys_list = self.csv2_keys
        json_keys_list = self.json_keys
        xml_keys_list = self.xml_keys

        self.all_data_list.extend(json_keys_list)
        self.all_data_list.extend(xml_keys_list)
        self.all_data_list.extend(csv1_keys_list)
        self.all_data_list.extend(csv2_keys_list)

        for x in self.all_data_list:
            for z in x.keys():
                self.all_keys_list.append(z)

        self.all_keys_list = list(set(self.all_keys_list))
        self.all_keys_list.sort()
    def summ_values(self):



        print("summ")

    def ass_json(self):
        file_name = os.path.dirname(sys.argv[0]) + "\\data\\advanced_results.tsv"

        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = [key for key in self.all_keys_list]
            write = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', dialect='excel-tab',
                                   lineterminator='\n')
            write.writeheader()
            for x in self.all_data_list:
                with open(file_name, 'a', newline='') as csvfile:
                    write.writerows([x])