import re
import string
import pygame


def checker_password(password: str) -> bool:
    """checks if password contains minimun 1 upper, 1 lower case and 1 puntuaction string.

    Args:
        password (str): eg: "NewPassword

    Returns:
        bool: True or False
    """
    return all(
        [
            re.search(f"[{re.escape(string.punctuation)}]", password),
            re.search(r"[a-z]", password),
            re.search(r"[A-Z]", password),
            re.search(r"[0-9]", password),
            len(password) >= 8,
        ]
    )


def run():
    try:
        pygame.mixer.init()
        print(
            """Mínimo 8 caracteres

    Al menos 1 mayúscula

    1 número

    1 carácter especial"""
        )
        user_password = input("Escribe una contraseña: ").strip()
        check_result = checker_password(password=user_password)
        while not check_result:
            print(
                """Mínimo 8 caracteres Al menos 1 mayúscula 1 número 1 carácter especial"""
            )
            # load the music file:
            pygame.mixer.music.load("./game-over-417465.mp3")
            # set volume
            pygame.mixer.music.set_volume(1)
            # start music.
            pygame.mixer.music.play(1)
            user_password = input("Escribe una contraseña: ").strip()
            check_result = checker_password(password=user_password)
            # stop
            pygame.mixer.music.stop()
        else:
            # load the music file:
            pygame.mixer.music.load("./sweet-game-over-sound-effect-230470.mp3")
            # set volume
            pygame.mixer.music.set_volume(1)
            # start music.
            pygame.mixer.music.play(1)
            print("Contraseña valida")
    except KeyboardInterrupt:
        print("Programa terminado por el usuario")


if __name__ == "__main__":
    run()
