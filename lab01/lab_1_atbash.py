print("-------------")
print(" Шифр Атбаш")
print("-------------")

alphabet = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
alphabet = alphabet.split()
alphabet.append(' ')
cypher = alphabet.copy()
cypher.reverse()


print("Таблица шифрования")
print(alphabet)
print(cypher)

while True:
    mess = str(input("Введите предложение, которое нужно зашифровать (0 - для завершения шифрования): "))
    if mess == '0':
        print("Выход из шифрования...")
        break

    cypher_mess = str()
    for symbol in mess:
        cypher_mess += cypher[alphabet.index(symbol)]

    print("      Введенное предложение: ", mess)
    print("   Зашированное предложение: ", cypher_mess)