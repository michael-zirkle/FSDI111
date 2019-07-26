import datetime

def get_date_time():
    current = datetime.datetime.now()
    time = current.strftime("%X")
    return time

def print_menu():
    # print("\n\n\n\n")
    print("*" * 30)
    print("Warehouse control system : "  + get_date_time())
    print("*" * 40)

    print("[1] Register new item")
    print("[2] List all the items")
    print("[3] Update stock of item")
    print("[4] List item with stock value")
    print("[5] Remove Item")
    print("[6] Register an entry")
    print("[7] Register an output")
    print("[8] See log of events")
    print("[9] See Inventory Value")
    print("[x] Exit the system")