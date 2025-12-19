    file_name = input("Nombre del archivo: ").lower()
    # almacena el resultado de la busqueda del archivo
    try:
        # verifica si el archivo escrito en 85line existe.
        if not (os.path.exists(f"{file_name}.json")):
            question_create_file = input(
                "El archivo no existe, 1) Crear nuevo, 2) Salir: "
            )
            try:
                while not question_create_file in ["1", "2"]:
                    raise ValueError("La opción no es valida")
            except ValueError as no_valid:
                print(no_valid)
            if question_create_file == "1":
                create_task()
            elif question_create_file == "2":
                return False
        task_title = input("Nombre de la tarea: ").lower()
        with open(f"{file_name}.json", "r", encoding="utf-8") as file_read:
            data_json = json.load(file_read)
            task_dict = {task[task_title] for task in data_json}
            print(task_dict)
    except:
        print("Leyendo")
        
        
def start_program():
    while True:
        try:

            if 1 <= opcion <= 5:
                return opcion
            else:
                print("[!] Por favor, elige un numero del 1 al 5")
        except ValueError:
            print("Debes ingresar un numero entero")
        except KeyboardInterrupt:
            return False