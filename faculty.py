class Faculty:
    def __init__(self, name, address, rank, email, age, weight, height, color, salary):
        self._name = name
        self._address = address
        self._rank = rank
        self._email = email
        self._age = age
        self._weight = weight
        self._height = height
        self._color = color
        self._salary = salary

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_rank(self):
        return self._rank

    def set_rank(self, rank):
        self._rank = rank

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary
        
    def get_class(self):
        _rankName = "None"
        if(self.get_rank() == 1 or self.get_rank == 2 ):
            _rankName = "D"
        elif(self.get_rank() == 3 or self.get_rank == 4):
            _rankName = "C"
        elif(self.get_rank() == 5 ):
            _rankName = "B"
        elif(self.get_rank() == 6  or self.get_rank == 7 ):
             _rankName = "A"
        else:
            _rankName = "Unclassified"
        return _rankName
    def __str__(self):
         return f'''Faculty Name        :\t{self._name}
Faculty Address     :\t{self._address}
Faculty Rank        :\t{self._rank}
Faculty Salary      :\t{self._salary}
Email Address       :\t{self._email}
Age                 :\t{self._age}
Weight              :\t{self._weight}
Height              :\t{self._height}
Color               :\t{self._color}\n-----------------------------------------------------'''