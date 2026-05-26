"""Abstractions should not depend upon details. Details should depend upon abstractions."""
from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class BackEnd(DataSource):
    def get_data(self):
        return "Data from the database"
