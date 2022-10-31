"""These are test functions of the functions in functions_for_Q5_to_Q20.py"""

from functions import functions_for_Q5_to_Q20 as fQ5
from functions import fileReading as fR

__file = fR.FileReading("../train.csv")
__func = fQ5.FromQ5ToQ20(__file)


def fifth_method_test():
    """This is the 5th test function of the 5th question"""
    __func.get_pie_chart_for_q5()


def sixth_method_test():
    """This is the 6th test function of the 6th question"""
    __func.get_bar_chart_for_q6()


def seventh_method_test():
    """This is the 7th test function of the 7th question"""
    __func.get_stacked_bar_chart_for_q7()


def eighth_method_test():
    """This is the 8th, 9th and 10th test function of the 8th, 9th and 10th questions"""
    __func.get_side_by_side_boxplot_for_q8_q9_q10()


def ninth_method_test():
    """This is the 11th and 12th test function of the 11th and 12th questions"""
    __func.get_correlation_heatmap_for_q11_q12()


def thirteenth_method_test():
    """This is the 13th test function of the 13th question"""
    __func.get_age_of_youngest_passenger_for_q13()


def fourteenth_method_test():
    """This is the 14th test function of the 14th question"""
    __func.get_average_fare_for_q14()


def fifteenth_method_test():
    """This is the 15th test function of the 15th question"""
    __func.get_oldest_passenger_survived_for_q15()


def sixteenth_method_test():
    """This is the 16th test function of the 16th question"""
    __func.get_the_oldest_age_female_survived_for_q16()


def seventeenth_method_test():
    """This is the 17th test function of the 17th question"""
    __func.get_number_of_under10_years_olds_wo_parents_for_q17()


def eighteenth_method_test():
    """This is the 18th test function of the 18th question"""
    __func.get_histogram_of_ages_for_genders_survived_for_q18()


def nineteenth_method_test():
    """This is the 19th test function of the 19th question"""
    __func.get_highest_number_of_siblings_for_q19()


def twentieth_method_test():
    """This is the 20th test function of the 20th question"""
    __func.get_scatter_plot_of_ages_and_fare_of_survived_passengers_for_q20()
