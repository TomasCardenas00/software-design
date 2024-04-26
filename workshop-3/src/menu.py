from platform import processor
from catalog import AdminCatalog, Catalog
from engines import Engine
from factories import HighEngineFactory, PoorEngineFactory
from loger import Loger
from processor import Processor
from vehicles import Bike, Car, Helicopter, Scooter, Truck, Vehicle, Yacht


new_loger = Loger()
new_poor_engine = PoorEngineFactory()
new_expns_engine = HighEngineFactory()
new_catalog = Catalog()
new_admin_catalog = AdminCatalog()

INF1 = """
    (1) High tier engine
    (2) Low tier engine
"""

INF2 = """
    (1) Electric engine
    (2) Gas engine
"""


def choose_engine():
    print(INF1)
    engine_type = int(input("What tier of engine do you want in your vehicle: "))
    print(INF2)
    engine_fuel = int(input("What tier of fuel do you want in your vehicle: "))
    if engine_type == 1:
        if engine_fuel == 1:
            engine = new_expns_engine.create_electric_engine()
        elif engine_fuel == 2:
            engine = new_expns_engine.create_gas_engine()
    elif engine_type == 2:
        if engine_fuel == 1:
            engine = new_poor_engine.create_electric_engine()
        elif engine_fuel == 2:
            engine = new_poor_engine.create_gas_engine()
    return engine

def create_vehicle():
    engine = choose_engine()
    chassis = input("Write the chassis of the vehicle (A or B):")
    if chassis not in ["A", "B"]:
        raise ValueError("Error: Chassis wrote is wrong. Must be A or B.")
    price = int(input("What is the price of this vehicle: "))
    model = int(input("What is the price of this vehicle: "))
    year = int(input("What is the year of this vehicle: "))
    consumption = float(input("What is the consumption of the vehicle: "))
    vehicle_type = input("What vehicle is this: ").capitalize()

    try:
        if vehicle_type == "CAR":
            transmission = input("What transmision does the vehicle have: ")
            trade = input("What is the trade of the car: ")
            combustible_type = input("What type of combustible does the vehicle have: ")
            new_vehicle = Car(engine,chassis,price,model,year,consumption,transmission,trade,combustible_type)
        
        elif vehicle_type == "TRUCK":
            new_vehicle = Truck(engine,chassis,price,model,year,consumption)

        elif vehicle_type == "YACHT":
            length = float(input("What is the length of the vehicle: "))
            weight = float(input("What is the weight of the vehicle"))
            trade = input("What is the trade of the car: ")
            new_vehicle = Yacht(engine,chassis,price,model,year,consumption,length,weight,trade)
        elif vehicle_type == "HELICOPTER":
            Helicopter(engine,chassis,price,model,year,consumption)
        elif vehicle_type == "SCOOTER":
            Scooter(engine,chassis,price,model,year,consumption)
        elif vehicle_type == "BIKE":
            Bike(engine,chassis,price,model,year,consumption)
    except Exception as e:
        print(f"Error: {e}.")

        new_admin_catalog.add_vehicle(new_vehicle)

def modify_vehicle():
    print([vehicle for vehicle in new_catalog.__vehicles])
    mod_vehicle = input("What vehicle are you trying to modify?: ")

def delete_vehicle():
    print([vehicle for vehicle in new_catalog.__vehicles])
    del_vehicle = input("What vehicle are you trying to delete?: ")
    new_catalog.__vehicles.remove(del_vehicle)
    
    


# ====================================MENU=========================================


MESSAGE_1 = """
    Welcome to the vehicle dealership company
    (1) Register user
    (2) Login user
    (3) Exit
"""

MESSAGE_2 = """
    (1) Administrator
    (2) User
"""

MESSAGE_3 = """
    (1) Create a vehicle
    (2) Update a vehicle
    (3) Delete a vehicle
    (4) Exit
"""

MESSAGE_4 = """
    (1) See vehicle catalog
    (2) Search a vehicle
    (3) Exit
"""

print(MESSAGE_1)
opcion1 = int(input("Please, select an option from the above: "))

while opcion1 != 3:
    if opcion1 == 1:
        username = input("Please, insert your username: ")
        password = input("Please, insert your password: ")
        new_processor = Processor(username)
        print(MESSAGE_2)
        utype = int(input("Please select your role: "))
        new_loger.register(username, password, utype)
        new_processor.add_to_log(new_processor.register())
        opcion1 = 0

    elif opcion1 == 2:
        username = input("Please, insert your username: ")
        password = input("Please, insert your password: ")
        new_processor = Processor(username)
        new_loger.login(username, password)
        new_processor.add_to_log(new_processor.login())

        print(f"Welcome {username}!")
        if new_loger.users[username]["type"] == 1:  # ADMIN
            print(MESSAGE_3)
            opcion2 = int(input("Please, select an option from the above: "))
            if opcion2 == 1:
                create_vehicle()
                new_processor.add_to_log(new_processor.vehicle_addition())

            elif opcion2 == 2:
                modify_vehicle()
                new_processor.add_to_log(new_processor.vehicle_modification())

            elif opcion2 == 3:
                delete_vehicle()
                new_processor.add_to_log(new_processor.vehicle_elimination())

            elif opcion2 == 4:
                new_processor.add_to_log(new_processor.exit())
                opcion1 = 0

        elif new_loger.users[username]["type"] == 2:  # USER
            opcion3 = int(input("Please, select an option from the above: "))
            if opcion3 == 1:
                new_catalog.get_price_by_range
                new_processor.add_to_log(new_processor.vehicle_classification())
            elif opcion3 == 2:
                new_catalog.get_all_vehicles()
                new_processor.add_to_log(new_processor.vehicle_search())
            elif opcion3 == 3:
                new_processor.add_to_log(new_processor.exit())
                opcion1 = 0
    else:
        print("Invalid option.")
        print("\n\n" + MESSAGE_1)
        option = int(input("Please, choise an option: "))        
