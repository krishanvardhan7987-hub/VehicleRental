Here’s a `statement.md` for your **Vehicle Rental System** project, written in the same style and level of detail as the Password Analyzer example you provided:



# VEHICLE RENTAL SYSTEM

This repository hosts a **Vehicle Rental System**, a Python-based command-line tool designed to help users manage vehicles, track rentals, and monitor returns efficiently. It allows users to add vehicles, rent them out to customers, view vehicle status, and return vehicles while keeping a record of all rental activities. This system provides an intuitive interface for both personal and small-scale business use, ensuring that vehicle management is simple, organized, and error-free.


## PROJECT OVERVIEW

Managing vehicle rentals manually can be tedious, prone to errors, and difficult to track, especially when multiple vehicles and customers are involved. Traditional methods might rely on handwritten logs or spreadsheets that can easily become inconsistent.

This **Vehicle Rental System** solves these problems by offering a Python-based command-line solution where users can:

* Add new vehicles to the system with relevant details.
* Check which vehicles are available or currently rented.
* Rent vehicles to customers while calculating total cost automatically.
* Return vehicles and update availability in real time.

By using this tool, even small businesses or individuals can maintain an organized rental log, avoid double-booking, and keep track of revenue, all without needing complex databases or web interfaces.



## FEATURES AND LOGICS

The Vehicle Rental System includes the following core functionalities:

* **Add Vehicle**
  Users can add a vehicle to the system by entering its ID, make, model, and rental rate per day. The system ensures unique vehicle IDs to avoid conflicts.

* **View Vehicles**
  Displays all vehicles along with their status (Available or Rented) and rental rate. This helps users quickly know which vehicles are ready to rent.

* **Rent Vehicle**
  Allows a customer to rent a vehicle by providing their name and the number of rental days. The system calculates the total rental cost and updates the vehicle's status automatically.

* **Return Vehicle**
  Handles vehicle returns by updating the vehicle’s availability and removing it from the active rentals list.

* **Error Handling**
  Validates user inputs for vehicle IDs, rental days, and rates to prevent invalid or inconsistent data.

* **User-Friendly CLI**
  Provides a simple, text-based interface with clear instructions and prompts to guide users through all operations.



## TECHNOLOGIES / TOOLS USED

* **Core Language:** Python 3.x
* **Standard Library:** None external, uses only built-in Python data structures (lists, dictionaries) and input/output functions.
* **Interface:** Command-line interface (CLI) for interactive user input and output.



## STEPS TO RUN THE CODE

Since this project relies solely on standard Python libraries, no extra installations are required.

1. **Save the Code**
   Copy the Python code into a file named `vehicle_rental_system.py`.

2. **Run the Script**
   Open your terminal or command prompt, navigate to the folder containing the file, and execute:

bash
   python vehicle_rental_system.py
   

3. **Follow Prompts**
   The program will display a menu:
   
   --- VEHICLE RENTAL SYSTEM ---
   1. Add Vehicle
   2. View Vehicles
   3. Rent Vehicle
   4. Return Vehicle
   5. Exit
   

   Enter your choice to perform the desired operation.



## EXAMPLE OUTPUT


 VEHICLE RENTAL SYSTEM 
1. Add Vehicle
2. View Vehicles
3. Rent Vehicle
4. Return Vehicle
5. Exit

Choice: 1
Vehicle ID: V001
Make: Toyota
Model: Corolla
Rate per day: 1500
Vehicle added.

Choice: 2
Vehicle List:
V001 - Toyota Corolla (₹1500/day) :: Available

Choice: 3
Enter Vehicle ID to rent: V001
Customer Name: Alice
Days: 3
Rented Successfully! Bill = ₹4500

Choice: 4
Enter Vehicle ID to return: V001
Vehicle returned.


## PROJECT STRUCTURE

* **add_vehicle()**: Prompts the user to input vehicle details, validates them, and adds the vehicle to the system.
* **view_vehicles()**: Displays all vehicles in the system along with availability and rates.
* **rent_vehicle()**: Handles renting a vehicle to a customer, calculates rental cost, and updates availability.
* **return_vehicle()**: Processes the return of a rented vehicle and updates the system.
* **main()**: Displays the main menu, accepts user choices, and routes them to the appropriate functions.