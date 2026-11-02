from random import choice

print("====PHYSICS CALCULATOR ====")

print("1. Speed")
print("2. Acceleration")
print("3. Force")
print("4. Work Done")
print("5. Density")
print("6. Weight")

choice = input("Choose a formula (1-6): ")

if choice == "1":
      distance = float(input("Enter distance (m): "))
      time = float(input("Enter time (seconds): "))
      if time > 0:
            print("speed =", distance / time, "m/s")
      else:
            print("Time must be greater than 0")

elif choice == "2":
      u = float(input("Enter initial Velocity:"))
      v = float(input("Enter final velocity: "))
      t = float(input("Enter time: "))
      if t > 0:
            print("Acceleration =", (v-u)/t, "m/s^2")
      else:
            print("Time must be greater than 0")

elif choice == "3":
      mass = float(input("Enter mass (kg): "))
      acceleration = float(input("Enter acceleration: "))
      print("Force =", mass * acceleration, "N")

elif choice == "4":
      force = float(input("Enter force (N): "))
      distance = float(input("Enter distance (m): "))
      print("Work done =", force * distance, "J")

elif choice == "5":
      mass = float(input("Enter mass (kg):"))
      volume = float(input(" Enter volume (m^3); "))
      if volume > 0:
            print("Density =", mass / volume, "kg/m^3")
      else:
            print("Volume must be greater than zero")

elif choice == "6":
      mass = float(input("Enter mass (kg): "))
      gravity = float(input("Enter  gravity (m/s^2):"))
      print("Weight =", mass * gravity, "N")

else:
      print("Invalid selection")