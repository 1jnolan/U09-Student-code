#Using OR to simplify code
#Student name:
#*****************************************
carAge=int(input("Enter age of car: "))
carFuel=input("Enter car's fiel type (petrol/diesel): ")
if carAge >10 or carFuel == "diesel":
    print("Pollution level: high")
else:
    print("Pollution level: low")
