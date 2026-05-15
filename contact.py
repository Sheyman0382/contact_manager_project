#!/usr/bin/python3
"""Contact manager module"""
import csv
import os


class Contact:
    """contanct manager class"""
    FILE_NAME = "contacts.csv"

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @property
    def name(self):

        """beyond just initializing, controls hw name is used"""
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @property
    def phone_number(self):
        """controls internally how phone number behaves"""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not type(value) is str:
            raise TypeError("phone_number must be a string")
        if len(value) != 11 or not value.isdigit():
            raise ValueError("mobile number must be equal to 11 digits")
        self.__phone_number = value

    def __str__(self):
        return "{} \n{}".format(self.name, self.phone_number)

    def to_dictionary(self):
        """returns dictionary attributes of each objects"""
        return {"name": self.name, "phone_number": self.phone_number}

    @classmethod
    def from_dictionary(cls, dictionary):
        return cls(
            dictionary["name"],
            dictionary["phone_number"]
        )
