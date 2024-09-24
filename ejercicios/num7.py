#contar los digitos de un numero
num = input(print("Ingrese un Numero"))

if num != int:
    print(f"ATENCION! {num} no es un dato valido, /n Por favor ingrese un valor numerico")
else:
    print(f"El numero {num} contiene {len(str(num))} digitos")
    