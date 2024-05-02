"""
Created by:
Hugo Herrador Segade h.herrador@udc.es
Pablo Montes Aldao pablomontes1@udc.es

Work licensed under a GPL 3.0 License (see LICENSE file)
"""


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
import time


def print_tree(T, p, d):
        """Print preorder representation of a binary subtree of T rooted at p at depth d.
           To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
        if p is not None:
            # use depth for indentation
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            print_tree(T, T.left(p), d+1) # left child depth is d+1
            print_tree(T, T.right(p), d+1) # right child depth is d+1


class Manager:
    """Class that simulates the functionality of the academies manager
    
    Attributes
    ----------
    academy_a: AVL or None
        AVL tree for Academy A courses. Initially None

    academy_b: AVL or None
        AVL tree for Academy B courses. Initially None
    
    aggregate: AVL
        AVL tree for the aggregate offer

    common: AVL
        AVL tree for the common offer
    
    done: list
        Auxiliar list to register which trees are already calculated
    """
    def __init__(self):
        """ Initializes an object with its attributes
        
        Attributes
        ----------
        academy_a: AVL or None
            AVL tree for Academy A courses. Initially None

        academy_b: AVL or None
            AVL tree for Academy B courses. Initially None

        aggregate: AVL
            AVL tree for the aggregate offer

        common: AVL
            AVL tree for the common offer

        done: list
            Auxiliar list to register which trees are already calculated
        """
        self.academy_a = None
        self.academy_b = None 
        self.aggregate = AVL()
        self.common = AVL()
        self.done = []


    def read_file(self, file) -> AVL:
        """Reads a file with the courses of an academy and stores those courses into an AVL tree. Then it prints and return that tree
        
        Parameters
        ----------
        file:
            txt file with the required data

        Returns
        -------
        AVL:
            AVL tree with the courses
        """
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
            
            print_tree(tree, tree.root(), 0)
            print(f"The file has been read successfully. {len(tree)} courses have been added")
            return tree
        
    
    def launch(self):
        """ Handles the first menu the user will face. It reads the file inputted by the user and stores the AVLs into their respective attributes.
        Then, it moves to the main menu of the program

        Returns
        -------
        None
        """
        for pos in ("first", "second"):
            message = f"""Please choose an option:
    1: Read the {pos} file
    q: Quit the program

    Your selection: """
            while True:
                code = input(message).strip().lower()
                if code in ("1", "q"):
                    break
                print("Sorry, that code was not recognised")

            if code == "q":
                print("Thanks for using our program")
                sys.exit()

            file = input(f"Please input the name of the {pos} file you want to read. Please note that the file must be located in the same directory as this program. \nFile name: ")
            if pos == "first":
                self.academy_a = self.read_file(file)
            else:
                self.academy_b = self.read_file(file)
                
        print("\n")
        self.main_menu()

    
    def main_menu(self):
        """ Handles the main menu of the program, where the user will be able to do some operatives and return to this menu

        Returns
        -------
        None
        """
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
        
        self.back_main()
    
    def comm_offer(self):
        """Calculates, shows and stores into an appropiate attribute the common offer (courses that are in both academies) for the academies in an AVL tree 

        Returns
        -------
        None
        """
        if 2 not in self.done: # it needs to be calculated yet
            for key in self.academy_a.keys():
                if key in self.academy_b.keys():
                    if self.academy_a[key] > self.academy_b[key]:
                        course = self.academy_a[key]
                        course.academy = "A" # to indicate which academy the course comes from
                    
                    else:
                        course = self.academy_b[key]
                        course.academy = "B"
                    
                    course.enrolment = self.academy_a[key].enrolment + self.academy_b[key].enrolment
                    self.common[key] = course

            print_tree(self.common, self.common.root(), 0)
            print(f"The tree has successfully been created. {len(self.common)} courses have been added")
            self.done.append(2)
        
        else:
            boolean = self.warning()
            if boolean:
                print_tree(self.common, self.common.root(), 0)
            
            self.back_main()

    
    def agg_offer(self):
        """ Calculates, shows and stores into the appropiate attribute the aggregate offer (courses that are in any of the two academies) for the academies in an AVL tree

        Returns
        -------
        None
        """
        if 1 not in self.done:
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
                        if self.academy_a[key] > self.academy_b[key]:
                            course = self.academy_a[key]
                            course.academy = "A"

                        else:
                            course = self.academy_b[key]
                            course.academy = "B"

                        course.enrolment = self.academy_a[key].enrolment + self.academy_b[key].enrolment
                        self.aggregate[key] = course

            print_tree(self.aggregate, self.aggregate.root(), 0)
            print(f"The tree has successfully been created. {len(self.aggregate)} courses have been added")
            self.done.append(1)

        else: # this has already been done before
            boolean = self.warning()
            if boolean:
                print_tree(self.aggregate, self.aggregate.root(), 0)
            
            self.back_main()


    def warning(self) -> bool:
        """ Lets the user know what he is trying to calculate is already stored and reasks if he wants to print the tree again
         
        Returns
        -------
        None
        """
        message = "Warning! This operation has already been performed.\nDo you want to print the tree again? [y/n] "
        while True:
            code = input(message).strip().lower()
            if code in ("y", "n"):
                break
            print("Sorry, the code was not recognised", end = "\n"*2)
        if code == "y":
            return True 
        
        if code == "n":
            return False
    

    def back_main(self):
        """ Slow transition to come back to the main menu, simulating a loading screen
        
        Returns
        -------
        None
        """
        message = "Going back to the main menu"
        dots = "."*5
        print(message, end = "", flush = True)
        for dot in dots:
            print(dot, end = "", flush = True)
            time.sleep(0.5)
        print("\n"*2)

        self.main_menu()
        


    def show_stats(self):
        """
        Using pandas, shows statistics about each academy:
        - Mean enrolment per language
        - Mean enrolment per level
        - Total possible revenue

        Returns
        -------
        None
        """
        print()
        

        data_a = [[course.name, course.language, course.level, course.enrolment, course.duration, course.price] for course in self.academy_a.values()]
        data_b = [[course.name, course.language, course.level, course.enrolment, course.duration, course.price] for course in self.academy_b.values()]

        df_a = pd.DataFrame(data_a, columns = ["name", "language", "level", "enrolment", "duration", "price"])
        df_b = pd.DataFrame(data_b, columns = ["name", "language", "level", "enrolment", "duration", "price"])

        for df in (df_a, df_b):
            # Identify each academy
            if df is df_a:
                name = "A"
            else:
                name = "B"

            message = f"Calculating stats for academy {name}"
            dots = "."*5
            print(message, end = "", flush = True)
            for dot in dots:
                print(dot, end = "", flush = True)
                time.sleep(0.5)
            print("\n"*2)

            
            print("*******************************\n"*2, end = "")
            print(f"   Stats for Academy {name}")
            print("*******************************\n"*2)
            # Mean enrolment per language
            group_col = "language"
            target_col = "enrolment"
            stats = df.groupby(group_col).agg({target_col :["mean"]})
            print ("##############################")
            print ("Average enrolment per language")
            print ("##############################\n")
            print (stats)
            print("\n")

            # Mean enrolment per level
            group_col = "level"
            target_col = "enrolment"
            stats = df.groupby(group_col).agg({target_col :["mean"]})
            print ("##############################")
            print ("  Average enrolment per level  ")
            print ("##############################\n")
            print (stats)
            print("\n")

            # Total possible revenue
            total_revenue = sum(df["enrolment"] * df["price"] * df["duration"])
            print ("##############################")
            print ("    Total possible revenue    ")
            print ("##############################\n")
            print (f"The total amount is {round(total_revenue, 2)}€")


            print("\n"*2)