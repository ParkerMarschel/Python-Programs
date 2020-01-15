# Lab 5
# Jared Cox, Parker Marschel
# cjw446 pgm33
# CS126 - Section 4
# 10/16/17
# we set contact info equal to a list to store some data
# and input that data into the dictionary withthe name as the key


def create_contact(contacts, first, last, email, age, phone):
    name = (first.lower(), last.lower())
    contact_info = [email, age, phone]
    contacts[name] = contact_info
# The below functions can be called to easily update
# contact information of a particular person


def update_contact_number(contacts, first, last, phone):
    name = (first.lower(), last.lower())
    contacts[name][2] = phone


def update_contact_email(contacts, first, last, email):
    name = (first.lower(), last.lower())
    contacts[name][0] = email


def update_contact_age(contacts, first, last, age):
    name = (first.lower(), last.lower())
    contacts[name][1] = age
# The below functions allow the retrieval of a certain piece of info
# relating to a specific contact


def get_contact_number(contacts, first, last):
    name = (first.lower(), last.lower())
    return contacts[name][2]


def get_contact_email(contacts, first, last):
    name = (first.lower(), last.lower())
    return contacts[name][0]


def get_contact_age(contacts, first, last):
    name = (first.lower(), last.lower())
    return contacts[name][1]
# contains_contact will return true if the name
# is in the dictionary and false otherwise


def contains_contact(contacts, first, last):
    name = (first.lower(), last.lower())
    if name in contacts:
        return True
    else:
        return False
# will display the information neatly when called


def display(contacts, first, last):
    name = (first.lower(), last.lower())
    print("%s %s" % (first, last))
    print("Email: %s" % (contacts[name][0]))
    print("Phone: %s" % (contacts[name][2]))
    print("Age: %s" % (contacts[name][1]))
# the function main when run will retrieve the needed information
# from the other functions


def main():
    contacts = {}
    create_contact(contacts, "Katie", "Katz", "katie.katz@nau.edu",
                   25, "857-294-2758")
    print("Creation of Katie Katz: {}".format("Passed" if
                                              contains_contact(contacts,
                                                               "Katie", "kaTz")
                                              else "Failed"))
    update_contact_number(contacts, "Katie", "Katz", "907-536-2946")
    print("Updating Katie Katz's number: {}".format("Passed" if
                                                    get_contact_number
                                                    (contacts, "Katie",
                                                     "Katz") ==
                                                    "907-536-2946" else
                                                    "Failed"))
    display(contacts, "Katie", "Katz")


main()