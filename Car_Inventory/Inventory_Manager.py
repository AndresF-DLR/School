#Main Variables
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
Q- Quit

    """
    
SEARCH_MENU = """
Search Menu
==================

1- Search by Model Number
2- Search by Make
3- Search by Model
4- Search by Body Type

    """

#Index Variables Per Car in Inventory
MODEL_NUMBER_INDEX = 0
YEAR_INDEX = 1
COLOR_INDEX = 2
MAKE_INDEX = 3
MODEL_INDEX = 4
BODY_INDEX = 5
QUANTITY_INDEX = 6

#Display Menu
def menu(inventory_size):
    """(int) -> str 
    This function takes one variable, the size of the inventory, and decides 
    the type of menu that is returned as a result. If the inventory size is 0, 
    then a smaller version of the menu is returned with two options, otherwise
    the full menu is displayed.
    
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
    Q- Quit    
    
    Enter your selection: 4
    4
    """
    #Minimize Menu Options if Inventory Contains No Cars.
    if inventory_size == 0:
        menu = MINI_MENU
        
    #Otherwise Include Full Menu Options
    else:
        menu = FULL_MENU

    print(menu)
    
    #User Input Based on Menu Options
    selection = input("Enter your selection: ")
    return selection

#Find Card Index
def find_index(inventory, model_number, year, colour):
    """(list, str, int, str) -> int
    This function takes four variables, the inventory (a list of lists), the 
    car model number, the year, and the color. The function works by iterating
    through the sublists within inventory and seeing if model_number, year, and
    color exist in a sublist of the inventory, in their expected index positions.
    It returns the index of that sublist within inventory. If there is no match, 
    the function returns -1.
    
    An example for inventory is given at the start.
    >>>INV=[[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 1]]
    
    >>>find_index(INV, ZN3EU, 2017, Red)
    0
    >>>find_index(INV, ZN3EU, 2017, Blue)
    -1
    """
    
    #Go Through Cars in Inventory and Try to Match User Input with Respective Car Variable
    for car_index in range(len(inventory)):
            if inventory[car_index][MODEL_NUMBER_INDEX] == model_number and inventory[car_index][YEAR_INDEX] == year and inventory[car_index][COLOR_INDEX] == colour:
                return car_index
    #Result When No Car Variables Matched User Inputs
    return -1

#Add Car to Inventory
def add_car(inventory):
    """(list) -> None
    This function takes one variable, the inventory, which is a list of lists.
    The function asks for the user to input model number, year, and color. It first
    uses the find_index function to see if the car already exists in the inventory.
    If it does not already exist, the function asks for the user to input the 
    make, model, body type and quantity and then appends these answers as a list
    within inventory. Otherwise, the function increases the quantity of the matching 
    car within it's existing sublist.
    
    An example for inventory is given at the start, and an example of the inventory
    printed is provided after each case.
    >>>INV=[[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 1]]
    
    >>>add_car(INV)
    Enter the model number: ZN3EU
    Enter the year: 2017
    Enter the colour: Blue
    Enter the make: Toyota
    Enter the model: Prius V
    Enter the body type: Hatchback
    Enter the quantity: 1
    >>>print(INV)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 1],
    [ZN3EU, 2017, Blue, Toyota, Prius V, Hatchback, 1]]
    
    >>>add_car(INV)
    Enter the model number: ZN3EU
    Enter the year: 2017
    Enter the colour: Red
    >>>print(INV)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2]]
    """
    
    #Identify if Car Already Exist Based on First Three Car Variables
    user_model_number = input("Enter the model number: ")
    user_year = int(input("Enter the year: "))
    user_colour = input("Enter the colour: ")
    car_index = find_index(inventory, user_model_number, user_year, user_colour)
    
    #If No Matches Result from First Three Variables Add New Car With the Rest of Variables
    if car_index == -1:
        user_make = input("Enter the make: ")
        user_model = input("Enter the model: ")
        user_body_type = input("Enter the body type: ")
        user_quantity = int(input("Enter the quantity: "))
        inventory.append([user_model_number, user_year, user_colour, user_make, user_model, user_body_type, user_quantity])
        print("\nNew car successfully added")

    #If First Three Variables Match a Existing Car in Inventory, Only Ask for Additional Quantities
    else:
        print("\nCar already exist in inventory.")
        user_quantity = int(input("Enter the quantity to be added: "))
        inventory[car_index][QUANTITY_INDEX] += user_quantity
        print("\nIncreased quantity by " + str(user_quantity) + ". New quantity is: " + str(inventory[car_index][QUANTITY_INDEX]))

#Remove Car from Inventory
def remove_car(inventory):
    """(list) -> None
    This function takes one variable, the inventory, whch is a list of lists.
    The function asks for the user to input model number, year, and color. It first
    uses the find_index function to see if the car already exists in the inventory.
    If it does not exist then no entry is removed. If the car is found and it's 
    quantity is greater than 1, then quantity is decreased by 1. Otherwise, the 
    index for the car is removed from the inventory.
    
    An example for inventory is given at the start, and an example of the inventory
    printed is provided after each case.
    >>>INV=[[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [ZN3EU, 2017, Blue, Toyota, Prius V, Hatchback, 1]]
    
    >>>remove_car(INV)
    Enter the model number: ZN3EU
    Enter the year: 2017
    Enter the colour: Gold
    Car not found! Cannot remove car!
    >>>print(INV)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [ZN3EU, 2017, Blue, Toyota, Prius V, Hatchback, 1]]
    
    >>>remove_car(INV)
    Enter the model number: ZN3EU
    Enter the year: 2017
    Enter the colour: Red
    Decreased quantity by 1. New quantity is: 1
    >>>print(INV)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 1],
    [ZN3EU, 2017, Blue, Toyota, Prius V, Hatchback, 1]]
    
    >>>remove_car(INV)
    Enter the model number: ZN3EU
    Enter the year: 2017
    Enter the colour: Blue
    Car removed from inventory
    >>>print(INV)
    [[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2]]
    """
    
    #Identify if Car Already Exist Based on First Three Car Variables
    user_model_number = input("Enter the model number: ")
    user_year = int(input("Enter the year: "))
    user_colour = input("Enter the colour: ")
    car_index = find_index(inventory, user_model_number, user_year, user_colour)
    
    #Prompt if No Matches from First Three Variables
    if car_index == -1:
        print("\nCar not found! Cannot remove car!")
    
    #If Matching Car has More than One Unit in Inventory, Remove One Unit from Inventory
    elif inventory[car_index][QUANTITY_INDEX] > 1:
        inventory[car_index][QUANTITY_INDEX] -= 1
        print("\nDecreased quantity by 1. New quantity is: " + str(inventory[car_index][QUANTITY_INDEX]))
    #If Matching Car Had Only One Unit in Inventory, Remove Car Entry from Inventory
    else:
        inventory.remove(inventory[car_index])
        print("\nCar removed from inventory.")

#Find Car in Inventory
def find_car(inventory):
    """(list) -> None
    This function takes one variable, inventory, which is a list of lists. It first 
    provides the user with a list of options to search for a car by, model number,
    make, model or body type. It asks the user to choose from these options, and
    then prompts the user to provide the relevent feature of the car based on their 
    chosen search feature. The function then interates through the inventory, appending
    all sublists with this matching feature, into a new list, matching_cars. If
    matching_cars has more than 0 items, then the function prints the entries in 
    matching_cars. Otherwise, the function says no cars have been found.
    
    An example for inventory is given at the start, and an example of the inventory
    printed is provided after each case.
    >>>INV=[[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 2],
    [ZN3EU, 2017, Blue, Toyota, Prius V, Hatchback, 1]]
    
    >>>find_car(INV)
    Enter your selection: 1
    Enter the model number: ZN3EU
    ZN3EU    2017    Red    Toyota    Prius V    Hatchback    2
    ZN3EU    2017    Blue    Toyota    Prius V    Hatchback    1
    
    >>>find_car(INV)
    Enter your selection: 4
    Enter the body type: Sport
    No cars found!
    """
    
    #List of Cars With Matching Parameters Per New Search
    matching_cars = []
    
    #Display Search Parameter Options
    print(SEARCH_MENU)
    
    #Capture User Choice of Search Parameter
    user_search = int(input("Enter your selection: "))
    
    #Prompt for User Input Outside of Available Options and Call for New Input
    while user_search > 4:
        print("\nWrong selection, try again!")
        user_search = int(input("Enter your selection: "))
    
    #Assign Car Variable Index Depending on User's Choice of Parameter
    if user_search == 1:
        search_parameter = input("Enter the model number: ")
        search_index = MODEL_NUMBER_INDEX
    elif user_search == 2:
        search_parameter = input("Enter the make: ")
        search_index = MAKE_INDEX
    elif user_search == 3:
        search_parameter = input("Enter the model: ")
        search_index = MODEL_INDEX
    elif user_search == 4:
        search_parameter = input("Enter the body type: ")
        search_index = BODY_INDEX
 
    #Group Search Parameter-Variable Matches in List
    for car in inventory:
        if search_parameter == car[search_index]:
            matching_cars.append(car)

    #Display Cars with Matching Parameters
    if len(matching_cars) >= 1:
        for car in matching_cars:
            print("\n", car[MODEL_NUMBER_INDEX], "\t", str(car[YEAR_INDEX]), "\t", car[COLOR_INDEX], "\t", car[MAKE_INDEX], "\t", car[MODEL_INDEX],"\t", car[BODY_INDEX],"\t", str(car[QUANTITY_INDEX]))
    
    #Prompt for No Matches/Empty List
    else:
        print("\nNo cars found!")

#Show Full Car Inventory
def show_inventory(inventory):
    """(list) -> None
    This function takes one variable, the inventory, which is a list of lists.
    The function first prints "Complete Inventory" and starts a new line before 
    returning each sub list as a new line, with the items in that sublist 
    seperated with tabs.
    
    An example for inventory is given at the start.
    >>>INV=[[ZN3EU, 2017, Red, Toyota, Prius V, Hatchback, 1]]
    
    >>>show_inventory(INV)
    Complete Inventory:
    ==================
        
    ZN3EU    2017    Red    Toyota    Prius V    Hatchback    1
    """
    print("\nComplete Inventory:", "\n==================", "\n")
    
    #Loop Through and Print Individual Car Entries
    for car in inventory:
         print(car[MODEL_NUMBER_INDEX], "\t", str(car[YEAR_INDEX]), "\t", car[COLOR_INDEX], "\t", car[MAKE_INDEX], "\t", car[MODEL_INDEX],"\t", car[BODY_INDEX],"\t", str(car[QUANTITY_INDEX]))


if __name__ == '__main__':
   
    #Initialize a Blank Inventory
   INV = [] 
   
   #Initialize Menu with Blank Inventory
   menu_selection = menu(len(INV))
   
   #Check for Quit Prompt
   while menu_selection.lower() != "q":
        
        #Check for Empty Menu Options if 0 Cars in Inventory
        if (len(INV) ==0 and menu_selection != "1") or (len(INV) > 0 and int(menu_selection) > 4):
            print("Wrong selection, try again!")
            menu_selection = menu(len(INV))
            
        #Initialize Function Matching Numerical Prompt in Full Menu and Display Menu Again After Termination
        elif menu_selection == "1":
            add_car(INV)
            menu_selection = menu(len(INV))
        elif menu_selection == "2":
            remove_car(INV)
            menu_selection = menu(len(INV))
        elif menu_selection == "3":
            find_car(INV)
            menu_selection = menu(len(INV))
        elif menu_selection == "4":
            show_inventory(INV)
            menu_selection = menu(len(INV)) 
            
   #Quit Prompt Called By User; End of Program
   print("\nGoodbye!")
