def validar_nombre(nombre):
    return bool(nombre.strip())  # Verifica si el nombre no está vacío

def validar_matricula(matricula):
    return matricula.isdigit() and len(matricula) == 8  # Suponemos que la matrícula tiene 8 dígitos

def validar_nota(nota):
    try:
        nota = float(nota)
        return 0 <= nota <= 10  # Las notas deben estar entre 0 y 10
    except ValueError:
        return False
