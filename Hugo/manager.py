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
from course import Course

class Manager:
    def __init__(self):
        self.academy_a = None
        self.academy_b = None 
        self.academy_c = None


    def read_file(self, file):
        with open(file) as txt:
            reader = txt.read()
            for line in reader.split("\n"):
                if line:
                    if not(line.lstrip().startswith("#")):
                        try:
                            name, duration, enrolment, level, language, price = line.split(",")
                            course = Course(name = name, duration = int(duration), enrolment = int(enrolment), level = level, language = language, price = float(price))
                            tree[hash(course)] = course
                        except:
                            print("There's been an issue with the provided data. Please check the file is in the correct format and try again.")
                            sys.exit()
                print(tree)
            print(f"The file has been read successfully. {len(tree)} courses have been added")
            return tree
        
    
    def launch(self):
        for academy in (self.academy_a, self.academy_b):
            while True:
                code = input(self.message_1).strip().lower()
                if code in ("1", "q"):
                    break
                print("Sorry, that code was not recognised")
    
            if code == "q":
                print("Thanks for using our program")
                sys.exit()
            
            file = input("Please input the name of the file you want to read. Please note that the file must be located in the same directory as this program. \nFile name: ")
            academy = self.read_file(file)
        self.main_menu()

        
    
    def launch(self):
        pass