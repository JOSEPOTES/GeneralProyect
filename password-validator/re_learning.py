import re
import string
import random


password = "hO9*"
# defino patrones: scape -> util para encontrar los signos de puntuación sin usar un for(revisa documentación en escape)
spectial_caracteres = re.search(f"[{re.escape(string.punctuation)}]", password)
lower_upper = re.search(r"[A-Za-z0-9]", password)
has_numbers = re.search(r"[0-9]", password)
word_len = True if len(password) >= 8 else False
if all([spectial_caracteres, lower_upper, word_len]):
    print("Contraseña completa")
else:
    print("Contraseña incompleta.")
