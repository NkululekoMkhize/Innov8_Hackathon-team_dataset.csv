from pymongo import MongoClient

class Storage:
    def __init__(self):
        self.__mongo_client = MongoClient('localhost', 27017)
        self.__db = self.__mongo_client['unemployed_data']

    def get_province_unemployed_stats(self, year):
        return self.__db[f'province_unemployed_stats_{year}'].find_one()

    def get_education_unemployed_stats(self, year):
        return self.__db[f'education_unemployed_stats_{year}'].find_one()

    def get_unemployment_by_gender(self, year):
        return self.__db[f'gender_unemployed_stats_{year}'].find_one()

    def get_unemployment_by_race(self, year):
        return self.__db[f'race_unemployed_stats_{year}'].find_one()