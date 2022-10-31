"""This class contains the functions that answer to the questions from Q1 to Q4"""
import math

from functions import fileReading
from typing import List, Dict


class FromQ1ToQ4:
    __file_to_read: fileReading
    __dict_for_Q1 = {}
    __dict_for_missing_values_for_Q4 = {}

    def __init__(self, file_object: fileReading):
        self.__file_to_read = file_object

    def get_first_ith_passengers_data_for_q1(self, number_of_passengers: int):
        self.__dict_for_Q1 = self.__file_to_read.get_dict_from_file()
        temp_dict = {}
        for key in self.__dict_for_Q1.keys():
            dict_for_passenger_id: Dict = self.__dict_for_Q1.get(key)
            list_of_values = list(dict_for_passenger_id.values())[:number_of_passengers]
            temp_dict.__setitem__(key, list_of_values)

        return temp_dict

    # This is a static function (since it depends on nothing but its argument) of a class which returns all the
    # keys in passed dictionary.
    @staticmethod
    def get_keys_of_dict_for_q2(dict_with_keys: Dict):
        return dict_with_keys.keys()

    @staticmethod
    def get_size_of_values_of_key_in_dict_for_q3(dict_with_keys: Dict, key_name: str):
        list_of_values = list(dict(dict_with_keys.get(key_name)).values())

        if list_of_values is not None:
            return list_of_values.__len__()
        else:
            return 0

    # Returns dictionary which indicates keys and their number of missing values in original dictionary passed by a user
    @staticmethod
    def get_dict_of_missing_values_for_q4(dict_with_keys: Dict, list_of_keys_to_check: List[str]):
        temp_dict = {}

        for key in dict_with_keys.keys():
            # Checks if the passed list of keys are found in dict_with_keys.
            if list_of_keys_to_check.__contains__(key):
                # If found, those keys and their values are copied to a temporary dictionary
                list_of_values: List = list(dict(dict_with_keys.get(key)).values())
                missing_values_number = [i for i in range(list_of_values.__len__()) if not isinstance(list_of_values[i], str) and math.isnan(list_of_values[i])] \
                    .__len__()

                temp_dict.__setitem__(key, missing_values_number)

        return temp_dict

