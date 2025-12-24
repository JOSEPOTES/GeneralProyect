import re


def warning(function):
    def wrapper(*args):
        print(
            f"""La contraseña debe tener: Minimo 8 caracteres, al menos 1 mayuscula, 1 numero, 1 caracter especial."""
        )
        function(*args)

    return wrapper


@warning
def checker_password(password):
    pass


@warning
def password():
    user_password = input("Escriba una contraseña: ")
    validator = checker_password(user_password)
    if validator:
        print("Contraseña aceptada")
    else:
        print("Contraseña erronea")


password()
