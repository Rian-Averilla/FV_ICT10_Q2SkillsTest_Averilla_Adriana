from pyscript import document,display

def checkdeets():

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
        "Kr": ("Krypton", 36, 83.798),
        "I": ("Iodine", 53, 126.90),
        "Xe": ("Xenon", 54, 131.290),
        "Rn": ("Radon", 86, 222.000),
        "Og": ("Oganesson", 118, 294.000)
        }

    Element1 = document.getElementById("Elemsymbol")
    symbol = Element1.value.strip().capitalize()
    element_display = Nonmetals.get(symbol, ("Element not found", "-", "-"))
    display(element_display, target="output1")

#DISPLAY FORMAT
    document.getElementById("result").innerHTML = f"""
    <b> Symbol: <b> {symbol} <br>
    <b> Element: <b> {element_display[0]} <br>
    <b> Atomic Number: <b> {element_display[1]} <br>
    <b> Atomic Mass: <b> {element_display[2]} <br>
    """
