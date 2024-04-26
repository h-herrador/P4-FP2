import sys
from avl_tree import *
from binary_search_tree import *
from binary_tree import *
from linked_positional_binary_tree import *
from linked_queue import *
from map_base import *
from positional_binary_tree import *
from positional_tree import *
from traversal_examples import *

class Course:
    def __init__(self, name, duration, enrolment, level, language, price):
        self.name = name
        self.duration = duration
        self.enrolment = enrolment
        self.level = level
        self.language = language
        self.price = price

    def __eq__(self, other: "Course"):
        return self.name == other.name and self.level == other.level and self.language == other.language 
    
    def __hash__(self):
        return hash((self.name, self.level, self.language))

    
    
    @property
    def name(self):
        return self._name 
    
    
    @name.setter 
    def name(self, name):
        if isinstance(name, str) and name != "":
            self._name = name 
    

    @property 
    def duration(self):
        return self._duration
    
    @duration.setter 
    def duration(self, duration):
        if isinstance(duration, int):
            if duration >= 0:
                self._duration = duration 
    

    @property
    def enrolment(self):
        return self._enrolment
    
    @enrolment.setter
    def enrolment(self, enrolment):
        if isinstance(enrolment, int):
            if enrolment >= 0:
                self._enrolment = enrolment 
    

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        if isinstance(level, str) and level != "":
            self._level = level
    

    @property
    def language(self):
        return self._language
    
    @language.setter 
    def language(self, language):
        if isinstance(language, str) and language != "":
            self._language = language 


    @property 
    def price(self):
        return self._price 

    @price.setter 
    def price(self, price):
        if isinstance(price, float):
            if price >= 0:
                self._price = price

class Reader:
    def read_file(self, file):
        with open(file) as txt:
            reader = txt.read()
            tree = BinaryTree()
            for line in reader.split("\n"):
                if not(line.lstrip().startswith("#")):
                    name, duration, enrolment, level, language, price = line.split(",")
                    course = Course(name = name, duration = int(duration), enrolment = int(enrolment), level = level, language = language, price = float(price))
                    #print(type(tree))
                    #print([getattr(course, attr) for attr in ('name', 'duration', 'enrolment', 'level', 'language', 'price')])
                    tree = BinaryTree(element = course, right = tree)
                print(tree)
            return tree

if __name__ == "__main__":
    reader = Reader()
    reader.read_file(sys.argv[1])


    

    