"""
Program : Warehouse control system
"""
import sys
from menu import print_menu
from item import Item
import datetime

import os
clear = lambda: os.system('cls')

import pickle

items = []
event_log = []
id_count = 1
items_file = "items.data"
log_file = "log.data"



#def clear():
 #   print("\033[H\033[J")

def save_log():
    try:
        writer = open(log_file, "wb")
        pickle.dump(event_log, writer)
        writer.close()
        print("Log saved")
    
    except:
        print("Error, log could not be saved")

def save_items():
    try:
        writer = open(items_file, "wb")
        pickle.dump(items, writer)
        writer.close()
        print("Data saved")
    
    except:
        print("Error, data could not be saved")


def read_events():
    global log_file

    try:

        reader = open(log_file, "rb")
        temp_data = pickle.load(reader)

        for event in temp_data:
            event_log.append(event)

    

        print("Events loaded")
    except:
        print("No events to load")

def read_items():
    global id_count
    global items_file

    try:

        reader = open(items_file, "rb")
        temp_data = pickle.load(reader)

        for item in temp_data:
         items.append(item)

        last = items[-1]
        id_count = last.id + 1

        print("Data loaded: " +str(len(items)) + " items")
    except:
        print("Error: Data could not be loaded")

def remove_item():
    item = select_item()
    if(item is not None):
        items.remove(item)
        print("Item removed!")

def print_inventory_value():
    print("*" * 30)
    print(" Inventory Value")

    for item in items:
        sum = 0
        val = item.price * item.stock
        sum += val
        print(item.title + " " + str(val))


    
        

def select_item():
    list_all()
    try:
        selection = int(input("Id of item: "))
        for item in items:
            if(item.id == selection):
                return item
    except:
        print(" Error: ID should be number")
    print("Error: ID not found")
    return None

def format_left(how_many, text):
    if(len(text) == how_many):
        return text

def register_entry(action):
    item = select_item()
    how_many = int(input("How many items: "))
    if(item is not None):
        

        if(action == 1):
            item.stock +=how_many
            event = str(item.id) + " " + str(how_many) + "input"
            event_log.append(event)
        elif(action == 2):
            item.stock -=how_many
            event = str(item.id) + " " + str(how_many) + "input"
            event_log.append(event)

        
        
        
        save_log()


def register_item():
    global id_count
    try:
        print(" Register new Item")
        id = id_count
        title = input("Enter item title: ")
        category = input("Enter item category: ")
        price = float(input("Enter item price: "))
        stock = int(input("Enter item stock: "))

        new_item = Item(id, title, category, price, stock)

        items.append(new_item)
        id_count += 1
        print(new_item.price)

    except:
        print("**Error, verify data and try again***")
        print("**Error: ", sys.exc_info()[0])

def print_log():
    for event in event_log:
            print(event)

def list_with_stock():
   #  print("\n\n\n")
    print(" List item with stock ")
    for item in items:
        if(item.stock > 0):
            print(str(item.id) + " _ " + (item.title) + "$" + str(item.price) + " " + str(item.stock))

        if(len(items) < 1):
            print("-Empty DB")

def update_stock():
    item = select_item()
    if(item):
        try:
            new_stock = int(input("Please provide new Stock value: "))
            item.stock = new_stock
            print("Status : Stock value updated")
        except:
             print("Error: Stock should be an integer")    
        

def list_all():
    print("*" * 30)
    print(" List of all items ")
    print("*" * 30)
    for item in items:
        print(str(item.id) + " " + item.title + "$" + str(item.price) + " " + str(item.stock))

read_items()
read_events()

opc = ''
while( opc !='x'):
    clear()
    print_menu()
    opc = input("Select an options: ")
    clear()

    if (opc == "1"):
        register_item()
        save_items()
    elif(opc == "2"):
        list_all()
    elif(opc == "3"):
        update_stock()
        save_items()
    elif(opc == "4"):
        list_with_stock()
    elif(opc == "5"):
        remove_item()
        save_items()
    elif(opc == "6"):
        register_entry(1)
        save_items()
    elif(opc == "7"):
        register_entry(2)
        save_items()
    elif(opc == "8"):
        print_log()
    elif(opc == "9"):
        print_inventory_value()

    if(opc !='x'):
        input("\n\nPress Enter to continue....")

            
