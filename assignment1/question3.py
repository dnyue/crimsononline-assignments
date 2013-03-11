"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""
building_map = {}
### a. 
class Person:
    room_no = None
    building = None
    def __init__(self,first,last,gender):
        self.rename(first,last)
        self.surgery(gender)

    def rename(self,new_first,new_last):
        if not new_first[0].isupper() or not new_last[0].isupper():
            raise Exception("Invalid name")
        else:
            self.first = new_first
            self.last = new_last
            self.full = self.first + ' ' + self.last
    def surgery(self,new_gender):
        if not new_gender == "M" and not new_gender == "F":
            raise Exception("Invalid gender")
        else:
            self.gender = new_gender
    def __repr__(self):
        return self.full

### b. 
###  A person can only enter a building if the variable, stored with the person, reads person.builing = None.
### f. I only could think about how to do this using global variables, which is from what i understand a no no when using classes. Also, I was running out of time as i did this, so it may not actually work. The variables are intended to be stored in the dictionary "building_map"
class Building:
    def __init__(self,location):
        self.people = []
        self.location = locate(location)
        
    def locate(self):
        if building_map[location]:
            building_map[location].append(self)
        else:
            bulding_map[location] = [self]
        return location    
    def enter(self, person, room_no):
        if person.building:
            raise Exception("Already in a building.")
        if not person in self.people:
            self.people.append(person)
        person.room_no = room_no
        person.building = True
            
    def where_is(self, person):
        if person in self.people:
            return person.room_no
        else:
            print "That person is not in the building"

### c. the iter command makes it possible to iterate over people.
    def __iter__(self):
        return iter(self.people)
           

### d.            
class OfficeBuilding(Building):
    def __init__(self,employee_list,location):
        Building.__init__(self,location))
        self.list = employee_list

    def enter(self,person,room_no):
        if person in self.list:
            Building.enter(self, person, room_no)
        else:
            print "Sorry, they are not an employee."
### e.
class House(Building):
    def __init__(self,location):
        Building.__init__(self,location)

    def enter(self,person):
        Building.enter(self, person, None)
        
    def where_is(self):
        pass

    def at_home(self):
        return person in self.people

### g. 
class Building:
    def __init__(self,location):
        self.people = []
        self.location = location
        building_map[location] = self
        
    def enter(self, person, room_no):
        if person.building:
            raise Exception("Already in a building.")
        if not person in self.people:
            self.people.append(person)
        person.room_no = room_no
        person.building = True
            
    def where_is(self, person):
        if person in self.people:
            return person.room_no
        else:
            print "That person is not in the building"

    def __iter__(self):
        return iter(self.people)

    def __setitem__(self, room_no, person)
        enter(self,room_no,person)
