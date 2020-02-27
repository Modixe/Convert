import json
import os
import sys


class TreatmentJson(object):

    def load(self):
        file_name = os.path.dirname(sys.argv[0]) + "\\data\\json_data.json"

        if os.path.exists(file_name) == True:
            try:
                with open(file_name, encoding='utf-8') as data_file:
                    self.data = json.load(data_file, )
                self.__dict__ = self.data
            except IOError as e:
                print(u' ошибочка)))')
        else:
            print(" json файл не найден")


