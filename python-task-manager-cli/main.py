def start_program():
    try:
        open_question = input(
            """
            1: Crear tarea.
            2: Listar tareas.
            3: Actualizar tareas.
            4: Eliminar tareas.
            5: Salir.
            Digita: """
        )
        open_question = int(open_question)
        while not (open_question) in range(1, 6):
            print(f"{open_question} no es valida")
            open_question = input(
                """
            1: Crear tarea.
            2: Listar tareas.
            3: Actualizar tareas.
            4: Eliminar tareas.
            5: Salir.
            Digita: """
            )
            open_question = int(open_question)
        return open_question
    except KeyboardInterrupt:
        return False


def create_task():
    print("Creando tarea")


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
            create_task()
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
