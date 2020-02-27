import csv
import os
import sys


class BasicTsv(object):
    def __init__(self, json_data=None, csv_data=None, xml_data=None):

        self.all_data_list = []
        self.csv1_keys = csv_data.csv1_list
        self.csv2_keys = csv_data.csv2_list
        self.json_keys = json_data.fields
        self.xml_keys = xml_data.xml_keys

        self.all_keys()
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

    def ass_json(self):
        file_name = os.path.dirname(sys.argv[0]) + "\\data\\basic_results.tsv"

        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = [key for key in self.all_keys_list]
            write = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', dialect='excel-tab',
                                   lineterminator='\n')
            write.writeheader()
            for x in self.all_data_list:
                with open(file_name, 'a', newline='') as csvfile:
                    write.writerows([x])


    #     for keys in self.scv.keys():
    #         key_scv1 += keys + ", "
    #     key_scv1 = sorted(key_scv1.split())
    #     key_scv1 = ' '.join(key_scv1)
    #
    #     # self.append_data(key_scv1)
    #     print("key_scv1= ", key_scv1)
    #
    # def value_scv1(self, value_scv):
    #     value_scv1 = ""
    #     for val in self.scv.value():
    #         value_scv1 += val
    #
    #
    # def append_data(self, file_pach, ):
    #
    #     # file_name = os.path.dirname(sys.argv[0]) + "\\data\\basic_results.tsv"
    #     # with open(file_name, 'w') as csvfile:
    #     #     fieldnames = ["D1", "D2", ]
    #     #     write = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    #     #     write.writeheader()
    #     #     write.writerow({"D1": 10000})#на всякий
    #
    #     file_name = os.path.dirname(sys.argv[0]) + "\\data\\basic_results.tsv"
    #     with open(file_name, 'w') as csvfile:
    #         fieldnames = [key_scv1]
    #         write = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    #         write.writeheader()
    #
    # def save_vocabulary(self):
    #
    #     label_file = os.path.dirname(sys.argv[0]) + "\\data\\basic_results.tsv"
    #


        # with open(label_file, 'w', encoding='utf8', newline='') as tsv_file:
        #     tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\t')
        #
        #     for kay, count in self.scv.items():
        #         tsv_writer.writerow([kay])
        #
        #     for kay, val in self.scv.items():
        #         # sty = "\v"
        #         # tsv_writer.writerow([sty])
        #
        #         for ss in val:
        #             s2 = ''.join(ss)
        #             s2 = "\n" + s2
        #             l = s2.split(' ')
        #
        #             for i in itertools.zip_longest(*l, fillvalue=" "):
        #                 if any(j != " " for j in i):
        #                     print(" ".join(i))
        #             tsv_writer.writerow([s2])

        # print("end")


        # file_name = os.path.dirname(sys.argv[0]) + "\\data\\basic_results.tsv"
        # self.tsv_keys = self.value_scv.result_csv2.keys()
        # print(self.tsv_keys)
        # self.s = ""
        # self.kis = []
        #
        # for y in self.tsv_keys:
        #     self.kis.append(y)
        #
        #     self.s = self.s + y
        #     print("str= ", self.s)
        # self.kis.sort()
        #
        # print("kis= ", self.kis)
        #
        #
        # with open(file_name, 'wt') as out_file:
        #     tsv_writer = csv.writer(out_file, delimiter='\t')
        #     tsv_writer.writerow(self.kis)
            # for key, val in self.value_scv.result_csv2.items():
            #     tsv_writer.writerow([key])
                # tsv_writer.writerow([val])
                # tsv_writer.writerow(['Shelah', 'Math'])
                # tsv_writer.writerow(['Aumann', 'Economic Sciences'])
