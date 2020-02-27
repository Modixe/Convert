import os
import sys


class TreatmentYaml(object):
    def __init__(self):
        self.Yaml_list = []

    def load_yaml(self):
        yaml_keys = dict()
        file_name = os.path.dirname(sys.argv[0]) + "\\data\\yaml_data.yaml"
        if os.path.exists(file_name) == True:
            try:
                # ......

                pass

            except IOError as e:
                print(u' ошибочка: ', e)
        else:
            print("yaml файл не найден")


