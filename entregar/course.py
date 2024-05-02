"""
Created by:
Hugo Herrador Segade h.herrador@udc.es
Pablo Montes Aldao pablomontes1@udc.es

Work licensed under a GPL 3.0 License (see LICENSE file)
"""


class Course:
    """Represents a course with its attributes and methods
    
    Attributes
    ----------
    name: str
        Name of the course
    
    duration: int
        Number of hours the course takes

    enrolment: int
        Number of students enrolled in the course
    
    level: str
        Level of the course
    
    language: str
        Language studied in the course

    price: float
        Price per hour and student
    
    academy: None or str
        Used to desambiguate which academy the course comes from, if necessary

    Methods
    -------
    None
    """
    def __init__(self, name, duration, enrolment, level, language, price):
        """ Initializes a course object with its attributes
        Attributes
        ----------
        name: str
        Name of the course
    
        duration: int
            Number of hours the course takes

        enrolment: int
            Number of students enrolled in the course

        level: str
            Level of the course

        language: str
            Language studied in the course

        price: float
            Price per hour and student
        """
        self.name = name
        self.duration = duration
        self.enrolment = enrolment
        self.level = level
        self.language = language
        self.price = price
        self.academy = None

    def __eq__(self, other: "Course"):
        return self.name == other.name and self.level == other.level and self.language == other.language
    
    def __gt__(self, other: "Course"):
        return self.price * self.enrolment * self.duration > other.price * other.enrolment * other.duration
    
    def __hash__(self):
        return hash((self.name, self.level, self.language))
    
    def __str__(self):
        if not self.academy:
            return f"{self.name}, {self.level}, {self.language}, {self.duration}, {self.price}"
        
        else:
            return f"{self.name}, {self.level}, {self.language}, {self.duration}, {self.price} (from Academy {self.academy})"

    
    
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

    @property
    def academy(self):
        return self._academy
    
    @academy.setter
    def academy(self, academy):
        if academy in (None, "A", "B"):
            self._academy = academy