
vehicles = []

rentals = []


def main():

    while True:

        print("\n--- VEHICLE RENTAL SYSTEM ---")
        print("1. Add Vehicle")
        print("2. View Vehicles")

        print("3. Rent Vehicle")
        print("4. Return Vehicle")
        print("5. Exit")

        i = input("Choice: ")

        if i == "1":

            add_vehicle()

        elif i == "2":
            view_vehicles()

        elif i == "3":
            rent_vehicle()
        elif i == "4":

            return_vehicle()
        elif i == "5":

            print("Bye!")
            break


        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

# addind vehicles
def add_vehicle():
    a = "Add New Vehicle"

    z = input("Vehicle ID: ")

    x = input("Make: ")
    y = input("Model: ")

    try:
        f = float(input("Rate per day: "))
    except:
        print("Invalid rate, using 0")
        rate = 0



    vehicle = {
        "id": z,
        "make": x,
        "model": y,

        "rate": f ,
        "available": True
    }
    vehicles.append(vehicle)
    print("Vehicle added.")


def view_vehicles():
    print("\nVehicle List:\n")
    for v in vehicles:
        st = "Available" if v["available"] else "Rented"
        
    
        print(f"{v['id']} - {v['make']} {v['model']} (₹{v['rate']}/day) :: {st}")

    print()


def rent_vehicle():
    vid = input("Enter Vehicle ID to rent: ")
    found = False

#temp_counter = 0   # for later use (not used anywhere)


    for v in vehicles:
        if v["id"] == vid:
            found = True

            if not v["available"]:
                print("Already rented!")
                return

            cust = input("Customer Name: ")

            try:

                days = int(input("Days: "))
            except:

                print("Invalid number, setting 1 day")
                days = 1

            total = v["rate"] * days
            v["available"] = False

            rentals.append({
                "vehicle_id": vid,
                "customer": cust,

                "days": days,
                "total": total
            })

            print("Rented Successfully! Bill = ₹", total)
            break

    if not found:
        print("Vehicle ID not found.")

# return
def return_vehicle():

    vid = input("Vehicle ID to return: ")
    ok = False

    for v in vehicles:
        
        if v["id"] == vid:
            ok = True
            if v["available"]:

                print("Vehicle is not rented.")
                return       
            # def delete_vehicle():#     print("will do later")#     pass

            v["available"] = True
            # remove rental record
            for r in rentals:
                if r["vehicle_id"] == vid:
                    rentals.remove(r)
                    break



            print("Vehicle returned.")
            break


    if not ok:
        print("Vehicle ID not found.")
