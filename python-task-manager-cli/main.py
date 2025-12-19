import json
from typing import Any
import os
from pathlib import Path


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
    file_name: str = input("Nombre del archivo: ").lower().strip().replace(" ", "_")
    task_list = []
    try:
        MAX_TASK = 10
        contador = 1
        while contador < MAX_TASK:
            print(f"Tarea: {contador} ")
            title = input("Titulo: ").lower()
            description = input("Description: ").lower()
            due_date = input("Fecha caducidad: ")
            state = input("Escriba el estado(pendiente,terminada,cancelada): ").lower()
            task_list.append(
                {
                    "title": title,
                    "Description": description,
                    "contador": contador,
                    "Expires at": due_date,
                    "state": ("undefined" if len(state) <= 0 else state),
                }
            )
            with open(f"{file_name}.json", "w", encoding="UTF-8") as file:
                json.dump(task_list, file, indent=4)
            contador += 1
            if contador == 6:
                add_more = question_result()
                if add_more == "s":
                    os.system("cls")
                    continue
                elif add_more == "n":
                    os.system("cls")
                    return task_list
                else:
                    return False
        return task_list
    except KeyboardInterrupt:
        print("saliendo....")
        return run()


# FIXME
def read_task():
    file_name = input("Nombre del archivo: ").lower()
    # almacena el resultado de la busqueda del archivo
    try:
        # verifica si el archivo escrito en 85line existe.
        if not (os.path.exists(f"{file_name}.json")):
            question_create_file = input(
                "El archivo no existe, 1) Crear nuevo, 2) Salir: "
            )
            if question_create_file == "1":
                create_task()
            elif question_create_file == "2":
                print("saliendo")
                run()
        task_title = input("Nombre de la tarea: ").lower()
        with open(f"{file_name}.json", "r", encoding="utf-8") as file_read:
            data_json = json.load(file_read)
            task_dict = {task[task_title] for task in data_json}
            print(task_dict)
    except:
        print("Leyendo")


def update_task():
    print("Actualizar")
    run()


def delete_task():
    print("Eliminar")
    run()


def run():
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
        while not (1 <= opcion <= 5):
            print("Optición no valida")
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
        match opcion:
            case 1:
                create_task()
            case 2:
                read_task()
            case 3:
                update_task()
            case 4:
                delete_task()
            case 5:
                print("Terminando el programa")
    except KeyboardInterrupt:
        print("-> Programa terminado por el usuario.")


if __name__ == "__main__":
    run()
