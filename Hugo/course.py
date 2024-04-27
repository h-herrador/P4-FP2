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
    
    def __gt__(self, other: "Course"):
        return self.price * self.enrolment * self.duration > other.price * other.enrolment * other.duration
    
    def __hash__(self):
        return hash((self.name, self.level, self.language, self.duration, self.price))

    
    
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



    

    