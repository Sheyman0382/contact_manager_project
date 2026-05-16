#!/usr/bin/python3
from contact import Contact


if __name__ == "__main__":
    #contact_name = input("Contact name:")
    #number = input("Mobile:")
    c1 = Contact("sheyman", "08138482343")
    c1.save_to_file()
    print("{} {}".format(id(c1), c1))
    
    c2 = Contact("shola", "08035848354")
    c2.save_to_file()
    print("{} {}".format(id(c2), c2))
    c3 = Contact("Tope", "09092764905")
    c3.save_to_file()
    print("{} {}".format(id(c3), c3))
    print("=============")
    print("=============")
    obj_list = Contact.load_from_file()
    for i in obj_list:
        print("{} {}".format(id(i), i))


if __name__ == "__main__":
  6     print(Contact.search_contact("Top"))


  if __name__ == "__main__":
  6     Contact.delete_contact("shola")
