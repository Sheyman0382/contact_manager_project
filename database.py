#!/usr/bin/python3
from contact import Contact
import os
import csv


class ContactDatabase:
    """this class manages every methods involved with database"""
    FILE_NAME = "contacts.csv"

    @classmethod
    def load_contacts(cls):
        """returns a list of references to object(s) as the case may be"""
        if not os.path.exists(cls.FILE_NAME):
            return []
        if not os.stat(cls.FILE_NAME).st_size:
            return []
        rows = []
        with open(cls.FILE_NAME, newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                rows.append(Contact.from_dictionary(row))
        return rows

    @classmethod
    def save_contacts(cls, contacts):
        """a method that writes into a csv file"""

        content = []
        for obj in contacts:
            content.append(obj.to_dictionary())
        content.sort(key=lambda contact: contact["name"].lower)
        with open(cls.FILE_NAME, "w", newline="") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["id", "name", "phone_number"]
            )
            writer.writeheader()
            writer.writerows(content)

    @classmethod
    def add_contact(cls, contact):
        """add/maybe append a contact into the list"""
        if not isinstance(contact, Contact):
            raise TypeError("only contact objects are alowed")
        contacts = cls.load_contacts()
        for obj in contacts:
            if (
                obj.name.lower() == contact.name.lower()
                or obj.phone_number == contact.phone_number
            ):
                return False
        contacts.append(contact)
        cls.save_contacts(contacts)
        return True

    @classmethod
    def delete_contact(cls, contact_id):
        """to delete unwanted contact"""

        file_content = cls.load_contacts()
        new_file_content = []
        deleted = False
        for obj in file_content:
            if obj.id == contact_id:
                deleted = True
            else:
                new_file_content.append(obj)
        if not deleted:
            return False
        cls.save_contacts(new_file_content)
        return True

    @classmethod
    def search_contact(cls, contact_id):
        """searches if a contact exists of not"""
        file_content = cls.load_contacts()
        if not file_content:
            return None
        for obj in file_content:
            if obj.id == contact_id:
                return obj
        return None

    @classmethod
    def update_contact(cls, contact_id, new_contact):
        """ """
        file_content = cls.load_contacts()
        new_file_content = []
        updated = False
        for obj in file_content:
            if obj.id == contact_id:
                new_file_content.append(new_contact)
                updated = True
            else:
                new_file_content.append(obj)
        if not updated:
            return False
        cls.save_contacts(new_file_content)
        return True

    @classmethod
    def view_contacts(cls):
        """returns every contact list that has been saved"""

        return cls.load_contacts()
