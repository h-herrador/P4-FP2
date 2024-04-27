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
import pandas as pd

class Manager:
    def __init__(self):
        self.academy_a = None
        self.academy_b = None 
        self.aggregate = AVL()
        self.common = AVL()


    def read_file(self, file):
        with open(file) as txt:
            reader = txt.read()
            tree = AVL()
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
        message = """Please choose an option:
    1: Read the file
    q: Quit the program

    Your selection: """
        for boolean in (True, False):
            while True:
                code = input(message).strip().lower()
                if code in ("1", "q"):
                    break
                print("Sorry, that code was not recognised")

            if code == "q":
                print("Thanks for using our program")
                sys.exit()

            file = input("Please input the name of the file you want to read. Please note that the file must be located in the same directory as this program. \nFile name: ")
            if boolean:
                self.academy_a = self.read_file(file)
            else:
                self.academy_b = self.read_file(file)
        self.main_menu()

    
    def main_menu(self):
        message = """Please choose an option:
    1: Show a new tree, performing the "aggregate offer" operation
    2: Show a new tree, performing the "common offer" operation
    3: Show stats about the academies
    q: Quit the program
            
    Your selection: """
        while True:
            code = input(message).strip().lower()
            if code in ("1", "2", "3", "q"):
                break
            print("Sorry, the code was not recognised")
        
        if code == "q":
            print("Thanks for using our program")
            sys.exit()

        elif code == "1":
            self.agg_offer()
        
        elif code == "2":
            self.comm_offer()

        elif code == "3":
            self.show_stats()
    
    
    def comm_offer(self):
        for key in self.academy_a.keys():
            if key in self.academy_b.keys():
               course = max(self.academy_a[key], self.academy_b[key])
               course.enrolment = self.academy_a[key].enrolment + self.academy_b[key].enrolment
               self.common[key] = course
        
        print(f"The tree has successfully been created. {len(self.common)} courses have been added")


    
    def agg_offer(self):
        for key in self.academy_a.keys():
            if key not in self.academy_b.keys():
                self.aggregate[key] = self.academy_a[key]

        for key in self.academy_b.keys():
            if key not in self.academy_a.keys():
                self.aggregate[key] = self.academy_b[key]
        
        if self.common:
            for index in self.common.keys():
                self.aggregate[index] = self.common[index]

        else:
            for key in self.academy_a.keys():
                if key in self.academy_b.keys():
                   course = max(self.academy_a[key], self.academy_b[key])
                   course.enrolment = self.academy_a[key].enrolment + self.academy_b[key].enrolment
                   self.aggregate[key] = course

        print(f"The tree has successfully been created. {len(self.aggregate)} courses have been added")


    def show_stats(self):
        data_a = [[course.name, course.language, course.level, course.enrolment, course.price] for course in self.academy_a]
        data_b = [[course.name, course.language, course.level, course.enrolment, course.price] for course in self.academy_b]

        df_a = pd.DataFrame(data_a, columns = ["name", "language", "level", "enrolment", "price"])
        df_b = pd.DataFrame(data_b, columns = ["name", "language", "level", "enrolment", "price"])

        for df in (df_a, df_b):
            pass # Implement pandas statistics logic


        
