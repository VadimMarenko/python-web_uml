from abc import ABC, abstractmethod

class AbstractUserInterface(ABC):

   @abstractmethod
   def display_contacts(self, contacts):
      pass
   
   @abstractmethod
   def display_notes(self, notes):
      pass
   
   @abstractmethod
   def display_help(self, commands):
      pass