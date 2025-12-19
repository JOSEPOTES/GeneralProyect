import json

data_json = open("./programacionfuncional.json", "r")
data_use = json.load(data_json)


def bring_obj(title, data=data_use):
    for line in data:
        while not (line["title"]):
            print("No existe tal resultado")
            title = input("Titulo: ")
        if line["title"] == title:
            return line
    return None


op = bring_obj("tst")
print(op)
