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
        if not type(value) is str:
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
        if len(value) != 11:
            raise ValueError("mobile number must be equal to 11 digits")
        self.__phone_number = value

    def __str__(self):
        return "{} \n{}".format(self.name, self.phone_number)

    def to_dictionary(self):
        """returns dictionary attributes of each objects"""
        return {"name": self.name, "phone_number": self.phone_number}

    def save_to_file(self):
        """a method that writes into a csv file"""

        with open(FILE_NAME, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            if not os.stat(self.FILE_NAME).st_size:
                writer.writerow(["Name", "Phone_number"])
            writer.writerow([self.name, self.phone_number])

    @classmethod
    def load_from_file(cls):
        if not os.path.exists(cls.FILE_NAME):
            return []
        if not os.stat(cls.FILE_NAME).st_size:
            return []
        rows = []
        with open(cls.FILE_NAME, newline="") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                rows.append(cls(row[0], row[1]))
        return rows

    @classmethod
    def search_contact(cls, contact_name):
        file_content = cls.load_from_file()
        if file_content == []:
            return "contact list is empty"
        for obj in file_content:
            if obj.name == contact_name:
                return obj
        return "contact not found"
