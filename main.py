print("Welcome Pilot, This is Navigation System.")
print("NOTE: For Safe landing in the Runway, the aircraft must be under the altitude of 3000 ft")
altitude = int(input("Please provide your altitude: "))
flag = 0
while flag != 1:
    if altitude >= 6000:
        print("WARNING: The altitude is TOO HIGH")
    elif altitude >= 3000:
        print("You can land.\nNOTE: It is recommended to be below 3000 ft")
        flag = 1
    else:
        print("You can safely land the aircraft.")
        flag = 1
    if flag != 1:
        altitude = int(input("Enter your current altitude(After turning around), Pilot: "))

print("SUCCESS!! You landed the Aircraft safely. Have a Nice Day, Pilot.")
