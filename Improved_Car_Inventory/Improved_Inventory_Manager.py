#Menu Layouts
MINI_MENU = """
Car Inventory Menu
==================

1- Add a Car
Q- Quit
    """
FULL_MENU = """
Car Inventory Menu
==================

1- Add a Car
2- Remove a Car
3- Find a Car
4- Show Complete Inventory
5- Output Inventory to File
Q- Quit
    """


#Car Entry Index Variables
MODEL_NUMBER_INDEX = 0
YEAR_INDEX = 1
COLOR_INDEX = 2
MAKE_INDEX = 3
MODEL_INDEX = 4
BODY_INDEX = 5
QUANTITY_INDEX = 6

#File Variables
INPUT_FILE = "test.csv"
OUTPUT_FILE = "output.txt"


def load_data(file, inventory, records):
    """(file open for reading, dict of {str: list of str}, list) -> None
    This function takes 3 arguements: a file (that acts as the input file
    that holds the car data), inventory (which is a dictionary of key/value
    pairs of the car accessories and model numbers), and records (a list of
    lists, representing the car records). The function loads all of the data
    from the input file into the dicitionary (inventory) and the records list
    (records).

    An empty inventory and records is given at the start, and an example of the
    inventory and records is provided after the case.
    >>>INV = {}
    >>>REC = []
    >>>load_data(INPUT_FILE, INV, REC)

    >>>print(INV)
    {'Heated Seats': 'ZN3EU', 'Bluetooth': 'GB5TS'}
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1]]
    """
    with open(file, "r") as source:

        data = []

        for line in source:
            
            #Skip Commentary in Data Source; Only Add Car Entries
            if not line.startswith('#'):
                
                data.append(line.strip().split(','))

        for i in range(len(data)):

            #Add New Accessories to Inventory
            if data[i][0] not in inventory:
                inventory[data[i][0]] = []

            #Add Car Model Number to Existing Accessory Inventory Entries
            inventory[data[i][0]].append(data[i][1])

            #Add Car Entries to Records
            records.append(data[i][1:])

def menu(inventory_size):
    """(int) -> str
    This function takes one arguement, the size of the inventory as an int, and
    decides the type of menu that is returned as a result. If the inventory size
    is 0, then a smaller version of the menu is returned with two options, otherwise
    the full menu is displayed. The function reads the menu selection from the
    user and returns it as a str.

    >>>menu(0)
    Car Inventory Menu
    ==================

    1- Add a Car
    Q- Quit

    Enter your selection: 1
    1

    >>>menu(1)
    Car Inventory Menu
    ==================

    1- Add a Car
    2- Remove a Car
    3- Find a Car
    4- Show Complete Inventory
    5- Output Inventory to File
    Q- Quit

    Enter your selection: 4
    4
    """
    
    if inventory_size == 0:
        menu = MINI_MENU

    
    else:
        menu = FULL_MENU

    print(menu)

    selection = input("Enter your selection: ")
    return selection


def find_index(records, model_number):
    """(list, str) -> int
    This function takes two arguemtns, records (a list of lists representing the
    car records) and model_number (a str representing a car model number). The
    function iterates through records and returns the index of the car with
    a matching model number, as an int. If no model number is found, the function
    returns -1.

    An example for inventory is given at the start.
    >>>REC = [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1]]

    >>>find_index(REC, GB5TS)
    1
    >>>find_index(REC, FJ9RD)
    -1
    """

    for car_index in range(len(records)):
            if records[car_index][MODEL_NUMBER_INDEX] == model_number:
                return car_index

    return -1

#Add Car to Inventory
def add_car(inventory, records):
    """(dict of {str: list of str}, list) -> None
    This function takes two arguements, inventory (which is a dictionary of
    key/value pairs of the car accessories and model numbers), and records (a
    list of lists, representing the car records). The functions asks the user to
    input the model number. It first uses the find_index function to see if the
    car already exists in the inventory. If it does not already exist, the
    function adds the key/value pair to the inventory and the car to the list of
    records. If the car already exists in the inventory, the function asks the user
    the quantity to be added and adjusts the records accordingly.


    An example for inventory and records is given at the start, and an example
    of the inventory and records printed is provided after each case.
    >>>REC = [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1]]
    >>>INV = {'Heated Seats': 'ZN3EU', 'Bluetooth': 'GB5TS'}

    #adding a car to the records and adding a new accessory to the inventory
    >>>add_car(INV, REC)
    Enter the model number: AZ2MG
    Enter the car accessory: GPS
    Enter the year: 2015
    Enter the colour: Brown
    Enter the make: Nissan
    Enter the model: Murano
    Enter the body type: SUV
    Enter the quantity: 1

    New car successfully added
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': 'ZN3EU', 'Bluetooth': 'GB5TS', 'GPS': 'AZ2MG'}

    #adding a car, but just adding the model to an existing accessory key
    >>>add_car(INV,REC)
    Enter the model number: TF7FW
    Enter the car accessory: Heated Seats
    Enter the year: 1992
    Enter the colour: Blue
    Enter the make: Ford
    Enter the model: Bronco
    Enter the body type: SUV
    Enter the quantity: 1

    New car successfully added
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': ['ZN3EU', 'TF7FW'], 'Bluetooth': ['GB5TS'], 'GPS': ['AZ2MG']}

    #increasing quantity to a car already in the inventory
    >>>add_car(INV,REC)
    Enter the model number: ZN3EU

    Car already exists in inventory.

    Enter the quantity to be added: 1
    Increased quantity by 1. New quantity is: 3
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 3],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': ['ZN3EU', 'TF7FW'], 'Bluetooth': ['GB5TS'], 'GPS': ['AZ2MG']}
    """

    #Identify if Car Already Exist in Inventory Based on Model Number
    user_model_number = input("Enter the model number: ")
    car_index = find_index(records, user_model_number)

    #If No Match, Capture Additional Car Information
    if car_index == -1:
        user_accessory = input("Enter the car accessory: ")
        user_year = int(input("Enter the year: "))
        user_colour = input("Enter the colour: ")
        user_make = input("Enter the make: ")
        user_model = input("Enter the model: ")
        user_body_type = input("Enter the body type: ")
        user_quantity = int(input("Enter the quantity: "))

        if user_accessory not in inventory:
            inventory[user_accessory] = [user_model_number]

        else:
            inventory[user_accessory].append(user_model_number)

        records.append([user_model_number, user_year, user_colour, user_make, user_model, user_body_type, user_quantity])
        print("\nNew car successfully added\n")

    #Add Extra Units if Car Already Exists in Inventory
    else:
        print("\nCar already exist in inventory.")
        user_quantity = int(input("Enter the quantity to be added: "))

        records[car_index][QUANTITY_INDEX] = int(records[car_index][QUANTITY_INDEX]) + user_quantity
        print("Increased quantity by " + str(user_quantity) + ". New quantity is: " + str(records[car_index][QUANTITY_INDEX]) + "\n")


def remove_car(inventory, records):
    """(dict of {str: list of str}, list) -> None
    This function takes two arguements, inventory (which is a dictionary of
    key/value pairs of the car accessories and model numbers), and records (a
    list of lists, representing the car records). The functions asks the user to
    input a car accessory. If the accessory is not in the inventory, then no cars
    are removed. Otherwise, it propts the user for the model number. Using the
    find_index function, the function searches for if the car exists in the records.
    If it does not exist then no car is removed. If the car is found and it's
    quantity is greater than 1, then quantity is decreased by 1. Otherwise, the
    car is removed from the records. If the value for a key in the inventory
    is empty then the key is removed.

    An example for inventory and records is given at the start, and an example
    of the inventory and records printed is provided after each case.
    >>>REC = [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 3],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>INV = {'Heated Seats': ['ZN3EU', 'TF7FW'], 'Bluetooth': ['GB5TS'], 'GPS': ['AZ2MG']}

    #the car and the accessory key are removed
    >>>remove_car(INV, REC)
    Enter the accessory: Bluetooth
    Enter the model number: GB5TS

    Car removed from inventory.
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 3],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': ['ZN3EU', 'TF7FW'], 'GPS': ['AZ2MG']}

    #the quantity of the car is decreased
    >>>remove_car(INV, REC)
    Enter the accessory: Heated Seats
    Enter the model number: ZN3EU
    Decreased quantity by 1. New quantity is: 1
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': ['ZN3EU', 'TF7FW'], 'GPS': ['AZ2MG']}

    #the car is removed from the records, no key is removed from inventory
    >>>remove_car(INV, REC)
    Enter the accessory: Heated Seats
    Enter the model number: TF7FW

    Car removed from inventory.
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': ['ZN3EU'], 'GPS': ['AZ2MG']}

    #The accessory key is not found in the inventory
    >>>remove_car(INV, REC)
    Enter the accessory: Cruise Control
    No cars for accessory Cruise Control. Cannot remove car!
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': ['ZN3EU'], 'GPS': ['AZ2MG']}

    #the model number is not found in records
    >>>remove_car(INV, REC)
    Enter the accessory: Heated Seats
    Enter the model number: BY4NG
    No cars with model number BY4NG for accessory Heated Seats. Cannot remove car!
    >>>print(REC)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1]]
    >>>print(INV)
    {'Heated Seats': ['ZN3EU'], 'GPS': ['AZ2MG']}
    """
    
    user_accessory = input("Enter the accessory: ")

    #User's Accessory is Not Part of Inventory
    if user_accessory not in inventory:
        print("No cars for accessory " + user_accessory + ". Cannot remove car!\n")

    else:
        #User Accessory is in Inventory, Request Model Number
        user_model_number = input("Enter the model number: ")

        #Find Car Index in Records from Model Number in Inventory
        if user_model_number in inventory[user_accessory]:
            car_index = find_index(records, user_model_number)
            car_quantity = int(records[car_index][QUANTITY_INDEX])

            if int(records[car_index][QUANTITY_INDEX]) > 1:
                records[car_index][QUANTITY_INDEX] = car_quantity - 1
                print("\nDecreased quantity by 1. New quantity is: " + str(records[car_index][QUANTITY_INDEX]) + "\n")

            else:
                inventory[user_accessory].remove(records[car_index][MODEL_NUMBER_INDEX])
                records.remove(records[car_index])
                print("\nCar removed from inventory.\n")

        #No Matches for User Model Number in Specified Accessory
        else:
            print("No cars with model number " + user_model_number + " for accessory " + user_accessory + ". Cannot remove car!\n")

    #Remove Accessory Entry from Inventory if Car Removal Emptied It
    if user_accessory in inventory and len(inventory[user_accessory]) == 0:
        del inventory[user_accessory]


def find_car(inventory, records):
    """(dict of {str: list of str}, list) -> None
    This function takes two arguements, inventory (which is a dictionary of
    key/value pairs of the car accessories and model numbers), and records (a
    list of lists, representing the car records). The functions asks the user to
    input a car accessory. If the accessory is not in the inventory, it notifies
    the user that the accessory is not in the inventory. If the car cannot be found
    in records, the function notifies the user that the car is not in records.
    Otherwise, the function prints the car data, tab-delimited on one line and the
    car accessory on the next line.

    An example for inventory and records is given at the start.
    >>>REC = [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 3],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1],
    [AZ2MG, 2015, Brown, Nissan, Murano, SUV, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>INV = {'Heated Seats': ['ZN3EU', 'TF7FW'], 'Bluetooth': ['GB5TS'], 'GPS': ['AZ2MG']}

    #car is found
    >>>find_car(INV, REC)
    Enter the accessory: Heated Seats
    Enter the model number: TF7FW

    TF7FW	1992	Blue	Ford	Bronco	SUV	1
    Accessory: Heated Seats

    #accessory is not found
    >>>find_car(INV, REC)
    Enter the accessory: Panoramic Roof
    No cars for accessory Panoramic Roof.

    #car is not found
    >>>find_car(INV, REC)
    Enter the accessory: Heated Seats
    Enter the model number: NH8J9
    No cars with model number NH8J9 for accessory Heated Seats.
    """


    user_accessory = (input("Enter the accessory: "))

    #User's Accessory is Not Part of Inventory
    if user_accessory not in inventory:
        print("No cars for accessory " + user_accessory + ".\n")

    else:
        #User Accessory is in Inventory, Request Model Number
        user_model_number = input("Enter the model number: ")

        #Model Number Is Not in the Accessory's Inventory
        if user_model_number not in inventory[user_accessory]:
            print("No cars with model number " + user_model_number + " for accessory " + user_accessory + ".")


        elif user_model_number in inventory[user_accessory]:
            model_index = find_index(records, user_model_number)

            #Search through Model Number Amongst in the Accessory's Inventory Entry
            for i in range(len(inventory[user_accessory])):
                car_model_number = inventory[user_accessory][i]

                #User Model Number Matches a Model Number Inside the Accessory's Inventory Entry
                if user_model_number == car_model_number:  
                    car = records[model_index]
                    
                    for attribute in car:
                        
                        if attribute == car[MODEL_NUMBER_INDEX]:
                            print("\n" + "\n" + car[MODEL_NUMBER_INDEX], end="\t")
                            
                        elif attribute == car[QUANTITY_INDEX]:
                            print(attribute)
                            print("Accessory : " + user_accessory)
                            
                        else:
                            print(attribute, end="\t")

def show_inventory(inventory, records):
    """(dict of {str: list of str}, list) -> None
    This function takes two arguements, inventory (which is a dictionary of
    key/value pairs of the car accessories and model numbers), and records (a
    list of lists, representing the car records). The function first prints
    "Complete Inventory", and then prints on a new line a series of "=" the length of
    "Complete Inventory" to act as a breaker. The function then iterates through
    the inventory, first printing the accessory, using "-" as a breaker and then
    uses the find_index function to find and print any car records that match the
    values, model numbers in this case, paired with that accessory. For every
    accessory key in the dictionary, the function completes this process.

    An example for inventory and records is given at the start.
    >>>REC = [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 3],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>INV = {'Heated Seats': ['ZN3EU', 'TF7FW'], 'Bluetooth': ['GB5TS']}

    >>>show_inventory(INV, REC)

    Complete Inventory:
    ==================

    Heated Seats:
    ------------
    ZN3EU	2017	Red    Toyota	Prius V	Hatchback	3
    TF7FW	1992	Blue	Ford	Bronco 	SUV	1

    Bluetooth:
    ---------
    GB5TS	2003	Blue	Volkswagen	Golf MK5	Compact	1
    """

    print("\nComplete Inventory:", "\n" + ("=" * len("Complete Inventory")), "\n")

    #Print Accessory Header
    for accessory in inventory:
        print(accessory + ":" + "\n" + ("-" * len(str(accessory))))

        #Find and Print Car Information by Matching Model Number in Inventory and Records
        for model_number in inventory[accessory]:
            model_index = find_index(records,model_number)
            car = records[model_index]
            print(car[MODEL_NUMBER_INDEX], "\t", str(car[YEAR_INDEX]), "\t", \
                  car[COLOR_INDEX], "\t", car[MAKE_INDEX], "\t", \
                  car[MODEL_INDEX],"\t", car[BODY_INDEX], "\t", str(car[QUANTITY_INDEX]))
            
        print("")


def output_inventory(file, inventory, records):
    """(file open for writing, dict of {str: list of str}, list) -> None
    This function takes three arguements, a file (that acts as the output file)
    inventory (which is a dictionary of key/value pairs of the car accessories
    and model numbers), and records (a list of lists, representing the car records).
    This function outputs the cars for each accessory to the output file. The
    format is akin to what is printed by the show_inventory function. First producing
    "Complete Inventory", and then prints on a new line a series of "=" the length of
    "Complete Inventory" to act as a breaker. The function then iterates through
    the inventory, first outputting the accessory, using "-" as a breaker and then
    uses the find_index function to find and output any car records that match the
    values, model numbers in this case, paired with that accessory. For every
    accessory key in the dictionary, the function completes this process.

    An example for inventory and records is given at the start.
    >>>REC = [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 3],
    [GB5TS, 2003, Blue, Volkswagen, Golf MK5, Compact, 1],
    [TF7FW, 1992, Blue, Ford, Bronco, SUV, 1]]
    >>>INV = {'Heated Seats': ['ZN3EU', 'TF7FW'], 'Bluetooth': ['GB5TS']}

    >>>output_inventory(OUTPUT_FILE, INV, REC)
    >>>output_file = open(OUTPUT_FILE)
    Complete Inventory:

    ==================


    Heated Seats:

    ------------

    ZN3EU	2017	Red    Toyota	Prius V	Hatchback	3

    TF7FW	1992	Blue	Ford	Bronco 	SUV	1


    Bluetooth:

    ---------

    GB5TS	2003	Blue	Volkswagen	Golf MK5	Compact	1

    """
    #Initialize New Blank File
    output_file = open(file, 'w')

    #Header
    output_file.write("\nComplete Inventory:"+"\n" + ("=" * len("Complete Inventory"))+"\n")

    #Accessory Header
    for accessory in inventory:
        output_file.write("\n" + accessory + ":" + "\n" + ("-" * len(str(accessory)))+"\n")

        #Find Car Information by Matching Model Number in Inventory and Records
        for model_number in inventory[accessory]:
            model_index = find_index(records,model_number)
            car = records[model_index]

            #Write Car Attributes
            for attribute in car:
                output_file.write(str(attribute)+"\t")

            output_file.write("\n")

    return None

if __name__ == '__main__':
    
    #Initialize Records Repository
    REC = []
    
    #Initialize Inventory Repository
    INV = {}

    #Load Car Data into Inventory and Records
    load_data(INPUT_FILE, INV, REC)

    #Present Menu with Current Inventory Until User Quits
    menu_selection = menu(len(INV))

    while menu_selection.lower() != "q":
    
        #Check for Empty Menu Options if 0 Cars in Inventory
        if (len(INV) ==0 and menu_selection != "1") or (len(INV) > 0 and (int(menu_selection) > 5 or int(menu_selection) <= 0)):
            print("Wrong selection, try again!\n")
            menu_selection = menu(len(REC))
    
        #Initialize Function and Menu Display Matching Numerical
        elif menu_selection == "1":
            add_car(INV, REC)
            menu_selection = menu(len(REC))
        elif menu_selection == "2":
            remove_car(INV, REC)
            menu_selection = menu(len(REC))
        elif menu_selection == "3":
            find_car(INV,REC)
            menu_selection = menu(len(REC))
        elif menu_selection == "4":
            show_inventory(INV, REC)
            menu_selection = menu(len(REC))
        elif menu_selection == "5":
            output_inventory(OUTPUT_FILE, INV, REC)
            menu_selection = menu(len(REC))
    
    #Quit Prompt Called By User
    print("Goodbye!")
