#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'robertyul'

# traditional class
class UpperAttrMetaClass(type):
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        print cls.__dict__
        print UpperAttrMetaClass.__dict__;
        print cls == UpperAttrMetaClass;
        result = type(future_class_name, future_class_parents, uppercase_attr);
        return result;

class Employee():
    '所有员工的基类'
    empCount = 0

    __metaclass__ = UpperAttrMetaClass

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


Employee();