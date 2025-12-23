import json
from typing import Any
import os
from datetime import datetime


def question_result() -> str | None:
    question_open = input("Agregar mas?: (S/N): ").lower()
    while (not (question_open) in ("s", "n")) or len(question_open) <= 0:
        print("Opcion no valida")
        question_open = input("Agregar mas?: (S/N): ").lower()
    if question_open == "s":
        return "s"
    elif question_open == "n":
        return "n"


def search(title: str, data: dict[str, Any]):
    for line in data:
        if line.get("title") == title:  # type: ignore
            return line
        elif title == "all":
            return data
    return None


def create_task():
    print("Creando la tareas.")
    file_name: str = input("Nombre del archivo: ").lower().strip().replace(" ", "_")
    task_list = []
    try:
        print(f"el archivo: {file_name} creado.")
        MAX_TASK = 10
        contador = 1
        now = datetime.now()
        while contador < MAX_TASK:
            print(f"Tarea: {contador} ")
            title = input("Titulo: ").lower()
            description = input("Description: ").lower()
            due_date = input("Fecha caducidad: ")
            state = input("Escriba el estado(pendiente,terminada,cancelada): ").lower()
            task_list.append(
                {
                    "id_task": contador,
                    "title": title,
                    "description": description,
                    "created_at": now.isoformat(),  # converts datetime to string.
                    "expires_at": due_date,
                    "state": "undefined" if len(state) <= 0 else state,
                }
            )
            with open(f"{file_name}.json", "w", encoding="UTF-8") as file:
                json.dump(task_list, file, indent=4, ensure_ascii=False)
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


def read_task():
    print("Leyendo tareas.")
    file_name = input("Nombre del archivo: ").lower()
    # almacena el resultado de la busqueda del archivo
    try:
        # verifica si el archivo escrito en 85line existe.
        if not (os.path.exists(f"{file_name}.json")):
            question_create_file = input(
                f"El archivo: {file_name} no existe, 1) Crear nuevo, 2) Salir: "
            )
            if question_create_file == "1":
                create_task()
            elif question_create_file == "2":
                print("saliendo")
                run()
            else:
                print("Opcion no valida")
                run()
        with open(f"{file_name}.json", "r", encoding="utf-8") as file_read:
            data_json = json.load(file_read)
            title = input("Titulo: ").strip()
            while len(title) <= 0:
                title = input("Titulo: ").strip()
            bring_data = search(title, data=data_json)
            while bring_data is None:
                print(f"Ups!, no he encontrado la tarea {title}")
                title = input("Titulo: ")
                bring_data = search(title=title, data=data_json)
            print(bring_data)
    except KeyboardInterrupt:
        print("Saliendo...")
        run()
    finally:
        run()


def update_task():
    print("--- Actualizar Tarea ---")
    file_name = input("Escribe el nombre del archivo (sin .json): ")

    try:
        # 1. Leer el archivo
        with open(f"{file_name}.json", "r", encoding="UTF-8") as file:
            file_json = json.load(file)

        # 2. Indexar por 'task_counter' para acceso rápido O(1)
        # Usamos task_counter como clave para no depender de la posición en la lista
        tasks_dict = {task["id_task"]: task for task in file_json}

        # 3. Pedir el ID de la tarea a actualizar
        task_id = int(input("Introduce el id_task de la tarea: "))

        if task_id in tasks_dict:
            campo = input("¿Qué campo quieres cambiar? (title, description, state): ")
            nuevo_valor = input(f"Nuevo valor para {campo}: ")

            # Actualizar el valor en el diccionario
            tasks_dict[task_id][campo] = nuevo_valor

            # 4. Guardar de nuevo como LISTA (formato JSON original)
            # Convertimos los valores del diccionario de vuelta a una lista
            with open(f"{file_name}.json", "w", encoding="UTF-8") as file_write:
                json.dump(
                    list(tasks_dict.values()), file_write, indent=4, ensure_ascii=False
                )
            print(f"Cambios guardados en {file_name}")
        else:
            print("Error: El ID de tarea no existe.")

    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def delete_task():
    print("Eliminar")
    file_name = input("Escribe el nombre del archivo (sin .json): ")
    with open(f"{file_name}.json", "r", encoding="UTF-8") as file_read:
        file_json = json.load(file_read)
        task_dict = {task["id_task"]: task for task in file_json}
        print(task_dict)
        id_task = int(input("introduce el id de la tarea: "))
        if id_task in task_dict:
            del task_dict[id_task]
        with open(f"{file_name}.json", "w", encoding="utf-8") as file_save:
            json.dump(list(task_dict.values()), file_save, ensure_ascii=False, indent=4)
            print("Cambio realizado en {}".format(file_name))


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
