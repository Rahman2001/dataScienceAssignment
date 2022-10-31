import pandas as pd
import math
from typing import List


class FileReading:
    """This class reads all data in .csv file, prints them out to the console and demonstrates data mapping using
    to_dict() function """

    __dictionary = {}
    __dictionary_without_nan = {}

    # Retrieves all data from the .csv file and prints them out to the console
    def __init__(self, file_path_name: str):
        self.__read_file(file_path_name)

    def __read_file(self, file_path: str):
        with open(file_path) as file:
            pandas_file = pd.read_csv(file)
            self.__dictionary = pandas_file.to_dict()

    # Returns the dictionary of the data in file
    def get_dict_from_file(self):
        return self.__dictionary

    # Returns a dictionary of the data in file without nan values
    def get_dict_without_nan(self):
        for key in self.__dictionary.keys():
            list_without_nan = []
            temp_list = list(dict(self.__dictionary.get(key)).values())
            for value in temp_list:
                if not isinstance(value, str) and not math.isnan(value):
                    list_without_nan.append(value)
                    continue
                if isinstance(value, str):
                    list_without_nan.append(value)
            self.__dictionary_without_nan.__setitem__(key, list_without_nan)
        return self.__dictionary_without_nan

    @staticmethod
    def delete_nans_in_list(list_of_values: List):
        updated_list = []
        for value in list_of_values:
            if not isinstance(value, str) and not math.isnan(value):
                updated_list.append(value)
            elif isinstance(value, str):
                updated_list.append(value)
        return updated_list
