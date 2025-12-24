import re
import string
import random


password = "TeamoJesus1*"
# defino patrones: scape -> util para encontrar los signos de puntuación sin usar un for(revisa documentación en escape)
spectial_caracteres = re.search(f"[{re.escape(string.punctuation)}]", password)
has_upper_case = re.search(r"[A-Z]", password)
has_lower_case = re.search(r"[a-z]", password)

if all([spectial_caracteres, has_upper_case, has_lower_case]):
    print("Contraseña valida")
else:
    print("Contraseña invalida")
