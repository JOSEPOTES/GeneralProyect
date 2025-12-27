from main import checker_password


# unidad de validación.
def testCheckPassword():
    assert checker_password("mundocontroladoTest1*")
