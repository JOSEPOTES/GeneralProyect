def start_program():
    while True:
        try:
            opcion = int(
                input(
                    """
            1: Crear tarea.
            2: Listar tareas.
            3: Actualizar tareas.
            4: Eliminar tareas.
            5: Salir.
            Digita: """
                )
            )
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("[!] Por favor, elige un numero del 1 al 5")
        except ValueError:
            print("Debes ingresar un numero entero")
        except KeyboardInterrupt:
            return False


def question_result() -> str | None:
    question_open = input("Agregar mas?: (S/N): ").lower()
    while (not (question_open) in ("s", "n")) or len(question_open) <= 0:
        print("Opcion no valida")
        question_open = input("Agregar mas?: (S/N): ").lower()
    if question_open == "s":
        return "s"
    elif question_open == "n":
        return "n"


def create_task():
    task_list = []
    try:
        MAX_TASK = 10
        contador = 1
        while contador < MAX_TASK:
            print(f"Tarea: {contador} ")
            title = input("Titulo: ").capitalize()
            description = input("Description: ").capitalize()
            due_date = input("Fecha caducidad: ")
            state = input(
                "Escriba el estado(pendiente,terminada,cancelada): "
            ).capitalize()
            task_list.append(
                {
                    "title": title,
                    "Description": description,
                    "contador": contador,
                    "Expires at": due_date,
                    "state": ("undefined" if len(state) <= 0 else state),
                }
            )
            contador += 1
            if contador == 6:
                add_more = question_result()
                if add_more == "s":
                    continue
                elif add_more == "n":
                    return task_list
                else:
                    return False
        return task_list
    except KeyboardInterrupt:
        return task_list


def read_task():
    print("Leyendo tarea")


def update_task():
    print("Actualizar")


def delete_task():
    print("Eliminar")


def run():
    try:
        start = start_program()
        if start == 1:
            print(create_task())
        elif start == 2:
            read_task()
        elif start == 3:
            update_task()
        elif start == 4:
            delete_task()
        elif start == 5:
            print("Saliendo...")
        else:
            raise ValueError("Terminando programa")
    except KeyboardInterrupt:
        print("Terminando programa")
    except ValueError as exit:
        print(exit)


if __name__ == "__main__":
    run()
