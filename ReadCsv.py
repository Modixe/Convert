import csv
import os
import sys


class TreatmentCsv_1(object):
    def __init__(self):
        self.csv1_list = []
        self.csv2_list = []

    def load_csv_1(self):
        csv1_keys = dict()
        file_name = os.path.dirname(sys.argv[0]) + "\\data\\csv_data_1.csv"
        reader = csv.DictReader(open(file_name))

        for row in reader:
            for key, val in row.items():
                csv1_keys.update({key: val})
                # self.csv1_keys.setdefault(key, val)
            self.csv1_list.append(csv1_keys.copy())

    def load_csv_2(self):
        csv2_keys = dict()
        file_name = os.path.dirname(sys.argv[0]) + "\\data\\csv_data_2.csv"
        reader = csv.DictReader(open(file_name))

        for row in reader:
            for key, val in row.items():
                csv2_keys.update({key: val})
                # self.csv1_keys.setdefault(key, val)
            self.csv2_list.append(csv2_keys.copy())
