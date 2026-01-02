# ambas son listas
stop = ["un", "los", "las", "de"]
expresion = "Mi corazon vive de los recuerdos".split()
for w in stop:
    if w in expresion:
        indices = expresion.index(w)
        del expresion[indices]
    else:
        print("NO SE ENCUENTRA")
