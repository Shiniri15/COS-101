
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (seconds): "))

    if time > 0:
        print("speed =", distance / time, "m/s")
    else:
        print("Time must be greater than 0")

def acceleration():
    u = float(input("Enter initial Velocity: "))
    v = float(input("Enter final velocity: "))
    t = float(input("Enter time: "))

    if t > 0:
        print("Acceleration =", (v - u) / t, "m/s^2")
    else:
        print("Time must be greater than 0")

def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration: "))

    result = mass * acceleration
    print("Force =", result, "N")

def work_done():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))

    result = distance * force_value
    print("Work done =", force_value * distance, "J")

def density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input(" Enter volume (m^3); "))

    if volume > 0:
        result = mass / volume
        print("Density =", result, "kg/m^3")
    else:
        print("Volume must be greater than zero")

def weight():
    mass = float(input("Enter mass (kg): "))
    gravity = float(input("Enter  gravity (m/s^2): "))

    result = mass * gravity
    print("Weight =", result, "N")

while True:
    print("====PHYSICS CALCULATOR ====")

    print("1. Speed")
    print("2. Acceleration")
    print("3. Force")
    print("4. Work Done")
    print("5. Density")
    print("6. Weight")

    choice = input("Choose a formula (1-6): ")
    if choice == "1":
        speed()

    elif choice == "2":
        acceleration()

    elif choice == "3":
        force()

    elif choice == "4":
        work_done()

    elif choice == "5":
        density()

    elif choice == "6":
        weight()

    else:
        print("Invalid selection!")

    again = input("Do you want to continue? (y/n): ")

    if again.lower() == "n":
        print("Thank you for using Physics Calculator!")
        break 