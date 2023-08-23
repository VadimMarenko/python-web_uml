from abc import ABC, abstractmethod


class AbstractUserInterface(ABC):
    @abstractmethod
    def display_contacts(self, arg, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def sort_notes(self, arg, notes):
        pass

    @abstractmethod
    def display_help(self, commands):
        pass
