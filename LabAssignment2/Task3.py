# Airline Management System
# Has classes Person, Employee, Passenger, Flights and Booking


class Person(object):
    """
    Class for Person - has attributes like name, gender, contact details
    zip code and person type.
    """
    def __init__(self, fname, lname, gen, phone, mail, zip, type):
        """
        Default constructor.
        """
        self.first_name = fname
        self.last_name = lname
        self.gender = gen
        self.phone_no = phone
        self.email = mail
        self.zip_code = zip
        self.person_type = type

    def print_details(self):
        """
        Prints details for the Person class.
        """
        print('\nPerson Details')
        print('-------------------------------')
        print('Name : ' + self.first_name + ' ' + self.last_name)
        print('Phone : ' + self.phone_no)
        print('Postal Code : ' + str(self.zip_code))
        print('Gender : ' + self.gender)
        print('-------------------------------')


class Employee(Person):
    """
    Class for Employee - a subclass of class Person
    has additional attributes like salary, ssn, department and emp no.
    """
    total_employees = 0

    def __init__(self, fname, lname, gen, phone, mail, zip, sal, ssn, dept):
        """
        Default constructor
        """
        Person.__init__(self, fname, lname, gen, phone, mail, zip, 'Employee')
        self._salary = sal
        self.__emp_ssn = ssn
        self.deptartment = dept
        self.emp_no = self.set_emp_no()

    def set_emp_no(self):
        """
        Returns total number of employees
        This value is set as the employee no
        """
        self.__class__.total_employees += 1
        return self.__class__.total_employees

    def print_details(self):
        """
        Prints details for Employee class
        """
        print('-------------------------------')
        print('Employee No: ' + str(self.emp_no))
        print('Name : ' + self.first_name + ' ' + self.last_name)
        print('Phone : ' + self.phone_no)
        print('Postal Code : ' + str(self.zip_code))
        print('Department : ' + self.deptartment)
        print('Salary : ' + str(self._salary))
        print('-------------------------------')

    def print_total_employees(self):
        """
        Prints total no of employees
        """
        print('\nTotal no of employees : ' + str(self.__class__.total_employees))


class Passenger(Person):
    """
    Class for Passenger - a subclass of class Person
    has additional attributes like address, credit card and rewards no.
    """
    total_passengers = 0

    def __init__(self, fname, lname, gen, phone, mail, zip, add, cc):
        """
        Default constructor.
        """
        Person.__init__(self, fname, lname, gen, phone, mail, zip, 'Passenger')
        self.address = add
        self.__credit_card_no = cc
        self.rewards_no = self.set_rewards_no()

    def set_rewards_no(self):
        """
        Increments the class variable-total_passengers
        Sets the rewards no for the passenger
        """
        self.__class__.total_passengers += 1
        return self.__class__.total_passengers

    def print_details(self):
        """
        Prints details for the Passenger class
        """
        print('-------------------------------')
        print('Rewards No: ' + str(self.rewards_no))
        print('Name : ' + self.first_name + ' ' + self.last_name)
        print('Phone : ' + self.phone_no)
        print('Address : ' + self.address)
        print('Postal Code : ' + str(self.zip_code))
        print('Credit Card : ' + str(self.__credit_card_no))
        print('-------------------------------')

    def print_total_passengers(self):
        """
        Prints total no of passengers
        """
        print('\nTotal no of passengers : ' + str(self.__class__.total_passengers))


class Flights(object):
    """
    Class for Flights - has attributes like departing location, date and time, arriving location, date and time,
    and price
    """
    total_flights = 0

    def __init__(self, d_loc, a_loc, d_date, a_date, d_time, a_time, price):
        """
        Default constructor
        """
        self.depart_location = d_loc
        self.arrive_location = a_loc
        self.depart_date = d_date
        self.arrive_date = a_date
        self.depart_time = d_time
        self.arrive_time = a_time
        self.price = price
        self.flight_no = self.set_flight_no()

    def set_flight_no(self):
        """
        Returns total no of flights
        This value is return to be set as the flight no
        """
        self.__class__.total_flights += 1
        return self.__class__.total_flights

    def print_details(self):
        """
        Prints details for Flight class
        """
        print('-------------------------------')
        print('Flight No: ' + str(self.flight_no))
        print('Route : ' + self.depart_location + '-' + self.arrive_location)
        print('Departs on ' + self.depart_date + ' at ' + self.depart_time + 'pm , arrives on ' + self.arrive_date
              + ' at ' + self.arrive_time + 'pm')
        print('Cost : ' + str(self.price))
        print('-------------------------------')


class Booking(Passenger, Flights):
    """
    Class for Booking details - a subclass of Passenger and Flights
    has additional attributes such as booking date and booking ref no.
    """

    total_bookings = 0

    def __init__(self, fname, lname, gen, phone, mail, zip, add, cc, d_loc, a_loc, d_date, a_date, d_time, a_time, price, b_date):
        """
        Default constructor
        """
        Passenger.__init__(self, fname, lname, gen, phone, mail, zip, add, cc)
        Flights.__init__(self, d_loc, a_loc, d_date, a_date, d_time, a_time, price)
        self.booking_date = b_date
        self.booking_ref_no = self.get_ref_no()

    def get_ref_no(self):
        """
        Returns total no of bookings
        This value is returned to be set as the booking ref no
        """
        self.__class__.total_bookings += 1
        return 'B' + str(self.__class__.total_bookings)

    def print_details(self):
        """
        Prints details for Booking class
        """
        print('-------------------------------')
        print('Passenger Name : ' + self.first_name + ' ' + self.last_name)
        print('Booking Reference No : ' + self.booking_ref_no)
        print('Booking Date : ' + self.booking_date)
        print('Flight No: ' + str(self.flight_no))
        print('Route : ' + self.depart_location + '-' + self.arrive_location)
        print('Departs on ' + self.depart_date + ' at ' + self.depart_time + 'pm , arrives on ' + self.arrive_date
              + ' at ' + self.arrive_time + 'pm')
        print('Cost : ' + str(self.price))
        print('-------------------------------')


def get_input():
    """
    Asks user to choose an option
    Returns the input as a digit
    """
    print('\n-----------------------------')
    print('Welcome to Southwest Airlines')
    print('-----------------------------\n')
    print('Press 1 : Employee Details')
    print('Press 2 : Passenger Details')
    print('Press 3 : Flight Details')
    print('Press 4 : Booking Details')
    print('Press 5 : Exit\n')
    inp = input('Enter your choice : ')

    if not(inp.isdigit()):
        return None

    return int(inp)


"""
Initializing values for Employee, Passenger, Flights and Booking through default constructor
"""

elist = []
e1 = Employee('Xi', 'Wa', 'F', '999-222-1110', 'xiwa@sw.com', '55555', 120000, 'X123', 'Air')
e2 = Employee('Vi', 'Da', 'M', '918-345-3456', 'vida@sw.com', '10021', 50000, 'Z999', 'Ground')
elist.append(e1)
elist.append(e2)

plist = []
p1 = Passenger('Avni', 'Mehta', 'F', '919-919-9191', 'avni@mail.com', 66209, 'Overland Park KS', 12345678901234)
p2 = Passenger('Hardik', 'Mehta', 'M', '919-000-9999', 'hardik@mail.com', 64001, 'Kansas City MO', 43567823453445)
p3 = Passenger('XYZ', 'Mehta', 'M', '816-000-9999', 'xyz@mail.com', 66209, 'Kansas City KS', 34566782345344)
plist.append(p1)
plist.append(p2)
plist.append(p3)

flist = []
f1 = Flights('KCI', 'LAX', '10/01/2017', '10/01/2017', '6:53', '8:50', '140')
f2 = Flights('KCI', 'LAX', '10/02/2017', '10/02/2017', '4:30', '8:50', '180')
f3 = Flights('KCI', 'LAX', '10/02/2017', '10/03/2017', '7:30', '1:20', '240')
f4 = Flights('LAX', 'KCI', '10/11/2017', '10/11/2017', '5:20', '9:50', '145')
f5 = Flights('LAX', 'KCI', '10/12/2017', '10/12/2017', '3:30', '11:50', '185')
f6 = Flights('LAX', 'KCI', '10/12/2017', '10/13/2017', '4:30', '1:20', '245')
flist.append(f1)
flist.append(f2)
flist.append(f3)
flist.append(f4)
flist.append(f5)
flist.append(f6)

blist = []
b1 = Booking('Avni', 'Mehta', 'F', '919-919-9191', 'avni@mail.com', 66209, 'Overland Park KS', 12345678901234, 'KCI', 'LAX', '10/01/2017', '10/01/2017', '6:53', '8:50', '140', '9/16/2017')
b2 = Booking('Hardik', 'Mehta', 'M', '919-000-9999', 'hardik@mail.com', 64001, 'Kansas City MO', 43567823453445, 'KCI', 'LAX', '10/01/2017', '10/01/2017', '6:53', '8:50', '140', '9/16/2017')
b3 = Booking('Avni', 'Mehta', 'F', '919-919-9191', 'avni@mail.com', 66209, 'Overland Park KS', 12345678901234, 'LAX', 'KCI', '10/11/2017', '10/11/2017', '5:20', '9:50', '145', '9/16/2017')
b4 = Booking('Hardik', 'Mehta', 'M', '919-000-9999', 'hardik@mail.com', 64001, 'Kansas City MO', 43567823453445, 'LAX', 'KCI', '10/11/2017', '10/11/2017', '5:20', '9:50', '145', '9/16/2017')
blist.append(b1)
blist.append(b2)
blist.append(b3)
blist.append(b4)


"""
Based on the input, display details for the class 
"""
c = None
while c != 5:
    c = get_input()
    if c == 1:
        print('\nEmployee Details')
        for i in range(len(elist)):
            elist[i].print_details()
        e1.print_total_employees()
    elif c == 2:
        print('\nPassenger Details')
        for i in range(len(plist)):
            plist[i].print_details()
        p1.print_total_passengers()
    elif c == 3:
        print('\nFlight Details')
        for i in range(len(flist)):
            flist[i].print_details()
    elif c == 4:
        print('\nBooking Details')
        for i in range(len(blist)):
            blist[i].print_details()
    elif c == 5:
        print('\nThank you for visiting Southwest Airlines. Good bye.')
    else:
        print('Invalid Option. Try again.')

