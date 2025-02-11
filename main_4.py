# Program Name: main.py
# Program Description:
#   This is the Sixth lab
#
#   In this program I make a program to make a new file and use it as a dictionary
# @Author: Akshay Rajendran
# @Date: 7/14/22

import json
from datetime import datetime


def print_me_first(value):
    current_time = datetime.now()
    current_time_str = str(current_time)

    print(f"Name        : {value}")
    print("program      : DictionaryLab6_working.py")
    print("Current Time :", current_time_str)
    return print()


def create_my_contact():
    my_contact = {
        "01": {
            "firstName": "John",
            "lastName": "Smith",
            "DOB": "1/20/1991",
            "phoneNum": {"number": "510-600-5400",
                         "type": "cell"},
            "address": {
                "street": "100 main street",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94536"}
        },

        "02": {
            "firstName": "Ron",
            "lastName": "Robertson",
            "DOB": " 5/23/1991 ",
            "phoneNum": {"number": "510-600-8800",
                         "type": "cell"},
            "address": {
                "street": "4600 Ohlone Way",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94539"}
        },

        "03": {
            "firstName": "Paul",
            "lastName": "Washington",
            "DOB": " 6/15/1995 ",

            "phoneNum": {"number": "510-688-1241",
                         "type": "cell"},
            "address": {
                "street": "8543 Ohlone Plaza",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94539"}
        }

    }

    return my_contact


def save_json_file(filename, contact_lis):
    json_object = json.dumps(contact_lis, indent=4)

    with open(filename, "w") as outfile:
        outfile.write(json_object)
    outfile.close()

    return json_object


def find_my_contact_key(searchkey, file):
    with open(file, "r") as json_file:
        opened_data = json.load(json_file)

        found = False
        for p_id, p_info in opened_data.items():
            for key in p_info:
                if p_info[key] == searchkey:
                    print("*** Searching for", p_info[key])
                    print("***",  p_info[key], "found", "***")
                    print("{:<10}".format("Name: "), p_info["firstName"], p_info["lastName"])
                    print("{:<10}".format("Birthday: "), p_info["DOB"])
                    print(p_info["phoneNum"]["type"], ": ", p_info["phoneNum"]["number"])
                    print("address: ", p_info["address"])
                    print()
                    found = True
        if not found:
            print("*** Searching for ", searchkey)
            print("***", searchkey, "not found ***")
        return


def open_json_file(filename):
    cheese = open(filename)
    return cheese


if __name__ == '__main__':

    print(print_me_first("Akshay Rajendran - CNET 142 - Lab 6 Dictionary"))

    contact_list = create_my_contact()
    save_json_file("json_data.json", contact_list)

    json_data = open_json_file('json_data.json')
    print("***BEGINNING OF JSON List: \n", contact_list, "\n***END OF JSON LIST\n")

    find_my_contact_key("Ron", "json_data.json")
    find_my_contact_key("Sha", "json_data.json")
