"""This class contains the functions that answer to the questions from Q5 to Q20"""

from matplotlib import pyplot as plt
from functions import fileReading as fR
from collections import Counter
import pandas as pd
import seaborn as sn


class FromQ5ToQ20:
    __file_reading: fR
    __dict_of_file = {}

    def __init__(self, file_object: fR.FileReading):
        self.__file_reading = file_object
        self.__dict_of_file = self.__file_reading.get_dict_without_nan()

    def get_pie_chart_for_q5(self):
        """This function answers to the 5th question of assignment"""
        list_of_labels = []
        list_of_embarked_port_of_each_passenger = list(self.__dict_of_file.get("Embarked"))
        total_number_of_each_embarked_port = Counter(list_of_embarked_port_of_each_passenger)

        for key in total_number_of_each_embarked_port.keys():
            if str(key).__eq__("S"):
                list_of_labels.append("Southampton")
            elif str(key).__eq__("C"):
                list_of_labels.append("Cherbourg")
            elif str(key).__eq__("Q"):
                list_of_labels.append("Queenstown")

        # Below pie chart shows the greatest number of people embarked from (Southampton) and the least one (
        # Queenstown)
        plt.pie(list(total_number_of_each_embarked_port.values()), labels=list_of_labels, autopct='%1.1f%%')
        plt.show()

    def get_bar_chart_for_q6(self):
        """This function answers the 6th question of assignment"""
        list_of_labels = []
        list_of_pclasses_of_each_passenger = list(self.__dict_of_file.get("Pclass"))
        total_number_of_each_pclass = Counter(list_of_pclasses_of_each_passenger)

        for key in total_number_of_each_pclass.keys():
            if str(key).__eq__(1):
                list_of_labels.append(key)
            elif str(key).__eq__(2):
                list_of_labels.append(key)
            elif str(key).__eq__(3):
                list_of_labels.append(key)

        plt.bar(range(list_of_labels.__len__()), list(total_number_of_each_pclass.values()))
        plt.title("Number of passengers in each classes")
        plt.xticks(range(list_of_labels.__len__()), list_of_labels)
        plt.ylabel("Total number of passengers")
        plt.show()
        plt.close()

    def get_stacked_bar_chart_for_q7(self):
        list_of_labels = ["1", "2", "3"]
        temp_dict = self.__file_reading.get_dict_from_file()

        dict_of_females_in_each_class = pd.DataFrame.from_dict(temp_dict).groupby('Pclass')['Sex', 'Survived']
        dict_of_survived_died_in_1 = dict_of_females_in_each_class.get_group(1).groupby('Sex')['Survived'].get_group(
            'female')
        dict_of_survived_died_in_1 = Counter(dict_of_survived_died_in_1)

        dict_of_survived_died_in_2 = dict_of_females_in_each_class.get_group(2).groupby('Sex')['Survived'].get_group(
            'female')
        dict_of_survived_died_in_2 = Counter(dict_of_survived_died_in_2)

        dict_of_survived_died_in_3 = dict_of_females_in_each_class.get_group(3).groupby('Sex')['Survived'].get_group(
            'female')
        dict_of_survived_died_in_3 = Counter(dict_of_survived_died_in_3)

        list_of_survived_females_in_each_class = [dict_of_survived_died_in_1.get(1), dict_of_survived_died_in_2.get(1),
                                                  dict_of_survived_died_in_3.get(1)]
        list_of_died_females_in_each_class = [dict_of_survived_died_in_1.get(0), dict_of_survived_died_in_2.get(0),
                                              dict_of_survived_died_in_3.get(0)]

        print(f"# of females survived in each class:\n {list_of_survived_females_in_each_class}")
        print(f"# of females died in each class:\n {list_of_died_females_in_each_class}")

        plt.bar(list_of_labels, list_of_survived_females_in_each_class, color='g')
        plt.bar(list_of_labels, list_of_died_females_in_each_class, bottom=list_of_survived_females_in_each_class,
                color='r')
        plt.title("# of survived and died females in each classes")
        plt.ylabel("# of females")
        plt.legend(["Survived", "Died"])
        plt.show()

    def get_side_by_side_boxplot_for_q8_q9_q10(self):
        list_of_labels = ["Survived", "Died"]

        dict_of_survived_died_ages = pd.DataFrame.from_dict(self.__file_reading.get_dict_from_file()).groupby('Sex')[
            'Survived', 'Age']

        dict_of_survived_died_females_ages = dict_of_survived_died_ages.get_group('female').groupby('Survived')['Age']
        list_of_ages_of_survived_females = self.__file_reading.delete_nans_in_list(
            list(dict(dict_of_survived_died_females_ages.get_group(1)).values()))
        list_of_ages_of_died_females = self.__file_reading.delete_nans_in_list(
            list(dict(dict_of_survived_died_females_ages.get_group(0)).values()))

        dict_of_survived_died_males_ages = dict_of_survived_died_ages.get_group('male').groupby('Survived')['Age']
        list_of_ages_of_survived_males = self.__file_reading.delete_nans_in_list(
            list(dict(dict_of_survived_died_males_ages.get_group(1)).values()))
        list_of_ages_of_died_males = self.__file_reading.delete_nans_in_list(
            list(dict(dict_of_survived_died_females_ages.get_group(0)).values()))

        fig, ax = plt.subplots(nrows=1, ncols=2)
        ax[0].boxplot(x=[list_of_ages_of_survived_males, list_of_ages_of_died_males], labels=list_of_labels)
        ax[0].set_title("Male")
        ax[1].boxplot(x=[list_of_ages_of_survived_females, list_of_ages_of_died_females], labels=list_of_labels)
        ax[1].set_title("Female")
        plt.show()

        temp_list = {}
        temp_list2 = {}
        temp_list3 = {}
        index_value = 0
        for index_value in range(list_of_ages_of_died_males.__len__() + list_of_ages_of_survived_males.__len__()):
            temp_list.__setitem__(index_value, 'male')
            if index_value < list_of_ages_of_died_males.__len__():
                temp_list2.__setitem__(index_value, 0)
                temp_list3.__setitem__(index_value, list_of_ages_of_died_males[index_value])
            else:
                temp_list2.__setitem__(index_value, 1)
                temp_list3.__setitem__(index_value, list_of_ages_of_survived_males[
                    index_value - list_of_ages_of_died_males.__len__()])

        for value in range(list_of_ages_of_survived_females.__len__() + list_of_ages_of_died_females.__len__()):
            temp_list.__setitem__(index_value + value, 'female')
            if value < list_of_ages_of_died_females.__len__():
                temp_list2.__setitem__(index_value + value, 0)
                temp_list3.__setitem__(index_value + value, list_of_ages_of_died_females[value])
            else:
                temp_list2.__setitem__(index_value + value, 1)
                temp_list3.__setitem__(index_value + value,
                                       list_of_ages_of_survived_females[value - list_of_ages_of_died_females.__len__()])

        df = {'Sex': temp_list,
              'Survived': temp_list2,
              'Age': temp_list3}

        print(pd.crosstab(df['Sex'], df['Survived'], rownames=['Sex'], colnames=['Survived'], margins=True))

    def get_correlation_heatmap_for_q11_q12(self):
        temp = self.__file_reading.get_dict_from_file()
        df = {}
        df.__setitem__('Sex', temp.get('Sex'))
        df.__setitem__('Age', temp.get('Age'))
        df.__setitem__('Ticket', temp.get('Ticket'))
        df.__setitem__('Survived', temp.get('Survived'))
        df.__setitem__('Fare', temp.get('Fare'))

        dict_of_groups_of_tickets = {}
        index = 0
        for value in Counter(dict(df['Ticket']).values()):
            dict_of_groups_of_tickets.__setitem__(value, index)
            index += 1

        dict_of_enum_of_tickets = {}
        list_of_values = list(dict(df['Ticket']).values())

        for index in range(list_of_values.__len__()):
            dict_of_enum_of_tickets.__setitem__(index, dict_of_groups_of_tickets[list_of_values[index]])

        df.__setitem__('Ticket', dict_of_enum_of_tickets)

        index = 0
        dict_of_enum_of_genders = {}
        for value in list(dict(df['Sex']).values()):
            if value == 'female':
                dict_of_enum_of_genders.__setitem__(index, 0)
            else:
                dict_of_enum_of_genders.__setitem__(index, 1)
            index += 1

        df.__setitem__('Sex', dict_of_enum_of_genders)
        df = pd.DataFrame(df)
        df = df.dropna()

        print(df.to_string())
        sn.heatmap(pd.DataFrame(df).corr(), annot=True)
        plt.show()

    def get_age_of_youngest_passenger_for_q13(self):
        print(min(self.__dict_of_file['Age']))

    def get_average_fare_for_q14(self):
        print(f"The average fare is {pd.DataFrame(self.__file_reading.get_dict_from_file())['Fare'].mean()}")

    def get_oldest_passenger_survived_for_q15(self):
        df = pd.DataFrame(self.__file_reading.get_dict_from_file()).groupby('Survived')['Age'].get_group(1).to_dict()
        list_of_survived_ages = self.__file_reading.delete_nans_in_list(list(df.values()))
        print(f"The oldest passenger survived is {max(list_of_survived_ages)}")

    def get_the_oldest_age_female_survived_for_q16(self):
        df = pd.DataFrame(self.__file_reading.get_dict_from_file()).groupby('Sex')['Survived', 'Age'].get_group('female')
        df = df.groupby('Survived')['Age'].get_group(1).to_dict()
        list_of_ages_of_female_passengers_survived = self.__file_reading.delete_nans_in_list(list(df.values()))
        print(f"The oldest female passenger survived is {max(list_of_ages_of_female_passengers_survived)}")

    def get_number_of_under10_years_olds_wo_parents_for_q17(self):
        df = pd.DataFrame(self.__file_reading.get_dict_from_file()).groupby('Parch')['Age'].get_group(0).to_dict()
        list_of_ages_wo_parch = self.__file_reading.delete_nans_in_list(list(df.values()))
        list_of_under10_year_olds = [i for i in list_of_ages_wo_parch if i < 10]
        print(f"List of under-10-year-old passengers without parents: {list_of_under10_year_olds}\n")
        print("Surprisingly, there was only one child under 10 years old traveling without parents.\n"
              "I do not have any idea about why that child was on that ship, but the logical reasoning tells me"
              "\nthat the child was abandoned by her parents and was taken by one of the ship's member."
              "\nNormally, before getting on the ship, people are checked according to their ages and other criteria.")

    def get_histogram_of_ages_for_genders_survived_for_q18(self):
        df = pd.DataFrame(self.__file_reading.get_dict_from_file()).groupby('Sex')['Survived', 'Age']
        dict_for_male = df.get_group('male').groupby('Survived')['Age'].get_group(1)
        dict_for_female = df.get_group('female').groupby('Survived')['Age'].get_group(1)
        dict_for_male = dict_for_male.dropna().to_dict()
        dict_for_female = dict_for_female.dropna().to_dict()

        print(f"Dictionary of males: \n{dict_for_male}\n")
        print(f"Dictionary of females: \n{dict_for_female}\n")

        plt.hist(x=dict_for_female.values(), color="purple", label="Female", range=[0, 100], alpha=0.5)
        plt.hist(x=dict_for_male.values(), color="blue", label="Male", range=[0, 100], alpha=0.5)
        plt.legend(["Female", "Male"])
        plt.ylabel("# of people")
        plt.xlabel("age")
        plt.show()

    def get_highest_number_of_siblings_for_q19(self):
        list_of_number_siblings = self.__file_reading.delete_nans_in_list(self.__dict_of_file['SibSp'])
        highest_number_of_siblings = max(list_of_number_siblings)
        print(f"The highest number of siblings is {highest_number_of_siblings}")

    def get_scatter_plot_of_ages_and_fare_of_survived_passengers_for_q20(self):
        df = pd.DataFrame(self.__file_reading.get_dict_from_file()).groupby('Survived')['Age', 'Fare']
        dict_of_survived = df.get_group(1).dropna().to_dict()
        dict_of_died = df.get_group(0).dropna().to_dict()

        plt.scatter(x=list(dict(dict_of_survived['Age']).values()), y=list(dict(dict_of_survived['Fare']).values()), color="green")
        plt.scatter(x=list(dict(dict_of_died['Age']).values()), y=list(dict(dict_of_died['Fare']).values()), color="red", alpha=0.3)
        plt.legend(["Survived", "Died"])
        plt.ylabel("Fare")
        plt.xlabel("Age")
        plt.show()
