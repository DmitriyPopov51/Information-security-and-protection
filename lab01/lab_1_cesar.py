import sys

print("-------------")
print(" Шифр Цезаря")
print("-------------")

alphabet = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
alphabet = alphabet.split()
password = list(input("Введите пароль (неповторяющиеся буквы): ").lower())
k = int(input("Введите сдвиг k: "))
k = k % len(alphabet)

uniq_letters = list()
for letter in alphabet:
    if letter not in password:
        uniq_letters.append(letter)
if k == 0:
    cypher = password + uniq_letters
elif k <= len(alphabet) - len(password):
    cypher = uniq_letters[-k:] + password + uniq_letters[:len(uniq_letters)-k]
else:
    print("Сдвиг неверный, нельзя поместить пароль полностью")
    sys.exit()

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
        if symbol == ' ':
            cypher_mess += ' '
        else:
            cypher_mess += cypher[alphabet.index(symbol)]

    print("      Введенное предложение: ", mess)
    print("   Зашированное предложение: ", cypher_mess)