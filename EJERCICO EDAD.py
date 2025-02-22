def obtener_nombre():
    return input("Ingrese su nombre: ")

def obtener_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad (1-130): "))
            if 1 <= edad <= 130:
                return edad
            else:
                print("⚠️ Error: La edad debe estar entre 1 y 130.")
        except ValueError:
            print("⚠️ Error: Ingrese un valor numérico válido para la edad.")

def main():
    nombre = obtener_nombre()
    edad = obtener_edad()
    
    if edad < 18:
        print(f"{nombre}, eres Menor de edad.")
    else:
        print(f"{nombre}, eres Mayor de edad.")

if __name__ == "__main__":
    main()