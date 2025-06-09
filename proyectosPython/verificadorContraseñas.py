#Verificador de Contraseñas Seguras

import string


contraseña = input("Digita tu contraseña para verificar su seguridad: ")

tiene_longitud = len(contraseña) >= 8
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_minuscula = any(c.islower() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
tiene_simbolo = any(c in string.punctuation for c in contraseña)

if all([tiene_longitud, tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_simbolo]):
    print("✅ Contraseña segura.")
else:
    print("❌ Contraseña insegura. Revisa los siguientes puntos:")
    if not tiene_longitud:
        print("- Debe tener al menos 8 caracteres.")
    if not tiene_mayuscula:
        print("- Debe tener al menos una letra mayúscula.")
    if not tiene_minuscula:
        print("- Debe tener al menos una letra minúscula.")
    if not tiene_numero:
        print("- Debe tener al menos un número.")
    if not tiene_simbolo:
        print("- Debe tener al menos un símbolo.")
