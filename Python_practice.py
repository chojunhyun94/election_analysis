import datetime as dt
counties = ["Arapahoe", "Denvor", "Jefferson"]

if counties[1] == "Denvor":
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson","registered_voters": 432438}]

for dict in voting_data:
    print(f"{dict['county']} county has {dict['registered_voters']} registered voters")

now = dt.datetime.now()

print("The time right now is ", now)