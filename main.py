from pyscript import document,display

#All Nonmetals Variable
Nonmetals = {
    "H": ("Hydrogen", 1, 1.0078),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.065),
    "Cl": ("Chlorine", 17, 35.453),
    "Ar": ("Argon", 18, 39.948),
    "As": ("Arsenic", 33, 74.922),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "K": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.290),
    "Rn": ("Radon", 86, 222.000),
    "Og": ("Oganesson", 118, 294.000)
}

Element1 = document.getElementById("Elemsymbol");

result = Nonmetals.get(Element1, ("Element not found", "-", "-"))

display(result, target="output1")