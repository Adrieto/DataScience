"""You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {
    "North America": {"USA": ["Atlanta", "Mountain View"]},
    "Asia": {"India": "Bangalore", "China": "Shangai"},
    "Africa": {"Egypt": "Cairo"},
}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

lista = locations["Asia"].items()
print(1)
print(locations["North America"]["USA"][0])
print(locations["North America"]["USA"][1])
print(2)
# print (lista[0][1], " - ", locations["Asia"].keys())
# print (locations["Asia"]["China"])

for (k, v) in locations["Asia"].items():
    print(v, " - ", k)
