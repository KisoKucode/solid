"""Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies."""
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Faxable(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printable):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class ModernPrinter(Printable, Faxable, Scannable):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
