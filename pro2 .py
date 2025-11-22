# DAY 1 PROJECT - VEHICLE RENTAL SYSTEM
# Learning Python, first real project 

# Some parts messy, some parts work, that's okay!

vehicles = []  # stores all vehicles
rentals = []   # currently rented vehicles
temp_var = 0   # not used yet, just testing 

day_counter = 1  # tracking my progress

# ------------------- ADD VEHICLE -------------------
def add_vehicle():
    print("\n--- Day 1: Add Vehicle ---")
    random_var = "I might use this later"  # not really used


    vid = input("Vehicle ID: ")
    # check duplicate
    for v in vehicles:

        if v["id"] == vid:
            print("Vehicle ID already exists ")
            return

    make = input("Make: ")
    model = input("Model: ")


    try:
        rate = float(input("Rate per day (₹): "))

    except:
        print("Invalid input! Setting rate to 0 ")
        rate = 0

    vehicle = {
        "id": vid,
        "make": make,

        "model": model,
        "rate": rate,

        "available": True
    }

    vehicles.append(vehicle)
    print("Vehicle added successfully! ")
    print(f"Debug: {vehicles}")  # just checking what's inside

# ------------------- VIEW VEHICLES -------------------
def view_vehicles():
    print("\n--- Day 2: View Vehicles ---")
    if len(vehicles) == 0:
        print("No vehicles yet  Add some first!")
        return

    for v in vehicles:
        status = "Available" if v["available"] else "Rented"
        print(f"[{v['id']}] {v['make']} {v['model']} - ₹{v['rate']}/day | {status}")

    print("\n")  # extra spacing, why not?

# ------------------- RENT VEHICLE -------------------
def rent_vehicle():
    print("\n--- Day 3: Rent Vehicle ---")

    v_id = input("Enter Vehicle ID to rent: ")
    found = False

    temp_counter = 123  # just testing variable usage 

    for v in vehicles:
        if v["id"] == v_id:
            found = True
            if not v["available"]:
                print("Already rented! Try again later.")

                return

            cust = input("Customer Name: ")

            try:
                days = int(input("Number of days: "))
            except:
                print("Invalid input  Setting days = 1")

                days = 1

            total = v["rate"] * days
            v["available"] = False

            rentals.append({
                "vehicle_id": v_id,
                "customer": cust,
                "days": days,
                "total": total
            })

            print(f"Rented successfully! Total Bill = ₹{total} ")
            break

    if not found:
        print("Vehicle ID not found  Check spelling maybe?")

# ------------------- RETURN VEHICLE -------------------
def return_vehicle():
    print("\n--- Day 4: Return Vehicle ---")
    v_id = input("Enter Vehicle ID to return: ")

    ok = False

    for v in vehicles:
        if v["id"] == v_id:
            ok = True
            if v["available"]:
                print("Vehicle is already available ")
                return

            v["available"] = True

            # remove from rentals
            for r in rentals:
                if r["vehicle_id"] == v_id:
                    rentals.remove(r)
                    break

            print("Vehicle returned successfully! ")
            break

    if not ok:
        print("Vehicle ID not found ")

# ------------------- MAIN MENU -------------------
def main():
    print("Welcome to Vehicle Rental System! ")

    print("Let's start coding... day by day ")


    while True:
        print("\n==============================")

        print(f"       MAIN MENU - Day {day_counter}")
        print("==============================")
        print("1. Add Vehicle")

        print("2. View Vehicles")

        print("3. Rent Vehicle")
        print("4. Return Vehicle")
        print("5. Exit")
        print("------------------------------")

        choice = input("Your choice: ")

        if choice == "1":

            add_vehicle()

        elif choice == "2":
            view_vehicles()
        elif choice == "3":
            rent_vehicle()

        elif choice == "4":
            return_vehicle()
        elif choice == "5":
            print("Exiting... Bye! ")
            break
        else:
            print("Hmm, invalid choice  Try again!")

        # random debug print to look human
        print(f"DEBUG: Vehicles={len(vehicles)}, Rentals={len(rentals)}")

# ------------------- RUN -------------------
if __name__ == "__main__":
    main()

print("Program finished! ")
