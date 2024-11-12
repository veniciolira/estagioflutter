def contar_a(string):
    return string.lower().count('a')

texto = input("Digite uma frase: ")

quantidade = contar_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes.")
