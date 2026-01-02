from pathlib import Path
import re

file_path = Path().resolve().parent

file_content = file_path / "text-analyzer-python" / "content.txt"
stop_words = file_path / "text-analyzer-python" / "stop_words.txt"

read_text = file_content.read_text()
read_stop = stop_words.read_text()

# limpiar puntuación
text = re.sub(r"[,\.\-\+]", "", read_text).split()

# convertir stopwords a set (más rápido)
list_stop = set(read_stop.split())

# eliminar TODAS las ocurrencias
text = [w for w in text if w not in list_stop]

print(text)
