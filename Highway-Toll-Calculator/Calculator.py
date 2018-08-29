#Initialize Zone Kilometer Markers

zone_1_beginning = 0
zone_1_end = 30
zone_2_beginning = zone_1_end + 1
zone_2_end = 60
zone_3_beginning = zone_2_end + 1
zone_3_end = 90

#Initialize Conditional Charges
camera_charge = 4.15
basic_charge = 1.25
Light_Vehicle_Charge = 0.4085
Heavy_Vehicle_Charge = 0.8175
Zone_2_Surcharge = 1.27

def display_instructions():
    """ () -> None
    Print instructions describing the fare's amount based on the vehicle's weight,
    zones and kilometers traveled, use of a transponder, fees, and taxes.
    """
    print("""This program calculates the toll charges for a paid highway.
            Light vehicles will be charged at a rate of 40.85 cents per km. Heavy
            vehicles will be charged at a rate of 81.75 cents per km.
            There are three travelling zones as follow:

                -Zone 1: from km marker 0 to marker 30.
                -Zone 2: from km marker 31 to marker 60.
                -Zone 3: from km marker 61 to marker 90.

            There will be a surcharge of 27% to travel in Zone 2.
            Each trip will be charged a highway entrance fee of $1.25.
            Vehicles without a rental transponder will be charged an additional
            camera recording fee of $4.15.
            All applicable Ontario taxes (13%) will be added to the total.""")

def calculate_toll_charge(entry_m, exit_m, vehicle):
    """ (int, int, str) -> float
    Return amount of toll charge derived from the vehicle's weight as well as
    kilometers and zones traveled, given that entry and exit are the kilometer markers
    through which the driver arrived at the highway in the range of 1-90, and vehicle
    is the weight category of the car driven (either "l" for light or "h" for heavy).

    "heavy" vehicles will be charged an increased rate of dollars/kilometers than
    "light" vehicles.

    Kilometers driven inside Zone 2 (ranging from kilometer marker 31 to 60) will
    have an added charge of 27% added to their base rate.

    Function assumes user provided his/her information correctly and within the ranges
    described above.

    >>> calculate_toll_charge(8, 35, "l")
    11.580975000000004
    >>>calculate_toll_charge(71, 42, "h")
    27.901274999999995
    >>>calculate_toll_charge(21, 55, "h")
    33.31312500000001
    """
    total = 0

    def determine_zone(marker):
        """(int) -> int
        Return zone (ranging 1 to 3) through which a driver entered or exited
        the highway, given that marker is the kilometer marker in the range 1-90
        through which they arrived/left the highway.

        >>> determine_zone(15)
        1
        >>> determine_zone(67)
        3
        >>> determine_zone(35)
        2
        """
        if (zone_1_beginning < marker < zone_2_beginning):
            zone = 1
        elif (zone_1_end < marker < zone_3_beginning):
            zone = 2
        elif (zone_2_end < marker < (zone_3_end+1)):
            zone = 3
        return zone

    if entry_m > exit_m:
        drive = range(exit_m+1, entry_m+1)
    else:
        drive = range(entry_m+1, exit_m+1)
    #Don't repeat yourself: save yourself these duplicates by assiging one "Rate" variable that can take the value of either Heavy or Ligth
    if (vehicle.lower() == "l"):
        for i in drive:
            if determine_zone(i) == 2:
                total +=((Light_Vehicle_Charge)*Zone_2_Surcharge)
            else:
                total += Light_Vehicle_Charge
    elif (vehicle.lower() == "h"):
        for i in drive:
            if determine_zone(i) == 2:
                total +=((Heavy_Vehicle_Charge)*Zone_2_Surcharge)
            else:
                total += Heavy_Vehicle_Charge
    return total

def calculate_total_bill(trip, transponder):
    """
    (float, bool) -> float
    Return the total amount the driver owes for the trip,
    considering trip is the amount owed due to the vehicle's weight and the
    kilometers/zones driven, and transponder is a True or False element in response
    to the driver's car having or lacking a transponder, respectively.

    Also adds $1.25 of standard fee for highways as basic_charge, 13% from Ontario taxes
    as taxes, and $4.25 should the car lack a transponder and transponder is False
    as camera_charge

    >>> calculate_total_bill(14.57, False)
    22.566099999999995
    >>> calculate_total_bill(33.18, True)
    38.905899999999995
    >>> calculate_total_bill(21.90, False)
    30.848999999999993
    """
    taxes = 1.13
    if transponder:
        return (trip + basic_charge)*taxes
    else:
        return (trip + basic_charge + camera_charge)*taxes


if __name__ == '__main__':
    
    display_instructions()
    
    entry_m = int(input("Enter entry marker:" ))
    
    exit_m = int(input("Enter exit marker:"))
    
    vehicle = input("Enter your vehicle type (L)ight or (H)eavy:")
    
    transponder_question = input("Do you have a transponder (Y)es or (N)o:")
    
    transponder = "Y" in transponder_question
    
    #Calculate trip charges before basic fee, transponder charge, and taxes.
    trip_charges = calculate_toll_charge(entry_m, exit_m, vehicle) 
    
    #Rounds total (including transpoder charge and taxes) bill to the second decimal
    total_bill = round(calculate_total_bill(trip_charges, transponder), 2) 
    
    print("Total due is: $" + str(total_bill))
