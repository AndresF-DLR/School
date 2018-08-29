# Improved Inventory Manager - Basics:

When executed, the program first extracts available car models from a pre-existent inventory file - in this case "test.csv". 
The script then loads the data into two repositories:
  1. The **Accessory Inventory** is a dictionary where the dealership's accessories are matched with elegible car models.
  2. The **Car Record** is a list of the dealership's available car models. 

Users are then able to view, add, and remove available cars as well as accessories. Finally, users can "print" the car inventory as a text file - for example, see "output.txt".

## Components
Each key/value pair in the Accesory Inventory is made of the following components:
* Key: **Accessory Name** - str
* Value: Available **Car Model Numbers** - list of str

In the Car Record, each entry is made up of the following elements in the specified order and data type:
* **Model Number** - str
* **Model Year** - int
* **Colour** - str
* **Make** - str
* **Model Name** - str
* **Body Type** - str
* **Quantity** - int

## Specifications
* Due to the nature of the assignment, the script must use the specified data structures (a dictionary and a list) as well as key/value and car entry schema. 

* The final product must only use the 8 specified functions - load_data(), menu(), find_index(), add_car(), remove_car(), find_car(), show_inventory(), output_inventory()
