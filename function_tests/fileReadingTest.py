"""This file contains a test function that tests the functions in fileReading.py to assure that they work as expected"""

from functions import fileReading
import pandas as pd


# Tests the function "get_dict_from_file()" of fileReading.py
def get_dict_from_file_function_test():
    file = fileReading.FileReading("../train.csv")
    dict_data = file.get_dict_from_file()
    assert dict_data.__len__() is not 0
    pandas_data = pd.DataFrame.from_records(dict_data)
    print(pandas_data)


# Tests the function "get_dict_without_nan()) of fileReading.py
def get_dict_without_nan_value_from_file_func_test():
    file = fileReading.FileReading("../train.csv")
    dict_data = file.get_dict_without_nan()
    assert dict_data.__len__() is not 0
    print(dict_data)
