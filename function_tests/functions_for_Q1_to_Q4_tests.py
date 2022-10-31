"""This file contains the tests of both classes functions_for_Q1_to_Q4.py and functions_for_Q5_to_Q20.py"""

from functions import fileReading, functions_for_Q1_to_Q4
import pandas as pd


def first_method_test():
    """The function below tests the first method (get_first_ith_passengers_data_for_q1()) of fileReading class."""

    file = fileReading.FileReading("../train.csv")
    func = functions_for_Q1_to_Q4.FromQ1ToQ4(file)
    passenger_dict = func.get_first_ith_passengers_data_for_q1(6)
    assert passenger_dict.__len__() is 12
    pandas_data = pd.DataFrame.from_records(passenger_dict)
    print(pandas_data.to_string())


def second_method_test():
    """The function below tests the second method (get_keys_of_dict_for_q2()) of fileReading class."""

    file = fileReading.FileReading("../train.csv")
    func2 = functions_for_Q1_to_Q4.FromQ1ToQ4(file)
    assert func2.get_keys_of_dict_for_q2(file.get_dict_from_file()).__len__() is 12
    print(func2.get_keys_of_dict_for_q2(file.get_dict_from_file()))


def third_method_test():
    """The function below tests the third method (get_size_of_values_of_key_in_dict_for_q3()) of fileReading class"""

    file = fileReading.FileReading("../train.csv")
    func3 = functions_for_Q1_to_Q4.FromQ1ToQ4
    size = func3.get_size_of_values_of_key_in_dict_for_q3(file.get_dict_from_file(), "PassengerId")
    print(f"PassengerId column has the size of {size}\n")


def forth_method_test():
    """The function below tests the forth method (get_dict_of_missing_values_for_q4()) of fileReading class"""

    file = fileReading.FileReading("../train.csv")
    func4 = functions_for_Q1_to_Q4.FromQ1ToQ4
    dict_for_func4 = file.get_dict_from_file()
    list_of_keys = ["Age", "Cabin", "Embarked"]
    dict_for_func4 = func4.get_dict_of_missing_values_for_q4(dict_for_func4, list_of_keys)
    for key in dict_for_func4:
        print(f"{key} has {dict_for_func4.get(key)} missing values")
