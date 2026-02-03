"""
This module is created by Yogesh
This module contains below functions

greet(): can be used to greet someone
myfun(): can be used to add multiple numbers

Class defined:

employee: to create employee object
manager: to create manager object

"""

def greet():
    return "Hey Good Morning!"

def myfun(a,*b):
    c=a+sum(b)
    return c


class employee:
    name=" "
    age=18
    salary=10000
    def onboarding(self):
        print("Welcome to the company")
        return None
    def get_hike(self,percent):
        print("Current salary is ",self.salary)
        hike=percent*self.salary
        self.salary=self.salary + hike
        print("New Salary is ",self.salary)
        return self.salary
    def get_salary(self):
        print("Current Salary is ",self.salary)
        return None

class manager(employee):  #this is called inhertiance i.e. we can access all the methods from               class empployee in class manager 
    team_size=5
    businiess_domain="sales"
    age=20

    def hire_member(self,num_positions):
        print("Current team size is ",self.team_size)
        self.team_size=self.team_size + num_positions
        print("New team size is now ",self.team_size)