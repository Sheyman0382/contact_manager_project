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

        new_file_content = []
        if os.stat(self.FILE_NAME).st_size:
            file_content = self.load_from_file()
            for obj in file_content:
                new_file_content.append(obj.to_dictionary())
        new_file_content.append(self.to_dictionary())
        with open(self.FILE_NAME, "w", newline="") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["name", "phone_number"]
            )
            writer.writeheader()
            for obj in new_file_content:
                writer.writerow(obj)
            print("contact saved successfully")

    @classmethod
    def load_from_file(cls):
        """returns a list of references to object(s) as the case may be"""
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
        """searches if a contact exists of not"""
        file_content = cls.load_from_file()
        if file_content == []:
            return "contact list is empty"
        for obj in file_content:
            if obj.name == contact_name:
                return obj
        return "contact not found"

    @classmethod
    def delete_contact(cls, contact_name):
        """to delete unwanted contact"""

        file_content = cls.load_from_file()
        new_file_content = []
        deleted = False
        for obj in file_content:
            if obj.name == contact_name:
                deleted = True
            else:
                new_file_content.append([obj.name, obj.phone_number])
        if not deleted:
            print("contact not found")
            return
        with open(cls.FILE_NAME, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "Phone_number"])
            writer.writerows(new_file_content)
