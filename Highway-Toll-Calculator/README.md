# Calculator - Basics and Components: 

Script requests car and travel information from the user to calculate the total fee for their trip. 

The factors below are taken into account to calculate toll charges for each ride:
  * Standard Highway Entrance Fee: **$1.25**
  * Highway Travel Zones:
    * Zone 1: Kilometer Markers **0 to 30** 
    * Zone 2: Kilometer Markers **31 to 60** 
    * Zone 3: Kilometer Markers **61 to 90**
  * Vehicle Charges per Weight:
    * Light Vehicles: **40.85 cents/km**
    * Heavy Vehicles: **81.75 cents/km**
  * Zone 2 Surcharge: **27%** 
  * Vehicles without a rental transponder unit are charged an additional camera recording
  fee of **$4.15**.
  * Provincial Tax: **13% of total fee**



## Calculator - Specifications
* Exactly 12 constant variables must be used for the purpose of this assignment. 
* The final product must only use the specified 4 functions - display_instructions(), calculate_toll_charge(), determine_zone(), calculate_total_bill()
