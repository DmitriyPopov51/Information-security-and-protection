print("-------------------")
print(" Таблица Виженера")
print("-------------------")

alphabet = "а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
alphabet = alphabet.split()
mess = str(input("Введите предложение, которое нужно зашифровать: ")).lower()
# mess = 'криптография серьезная наука'
mess = mess.replace(' ', '')
mess = mess.replace('\t', '')
orig_mess = mess
password = str(input("Введите пароль: ")).lower()
# password = 'математика'
password = password.replace(' ', '')
password = password.replace('\t', '')

print("Введенное сообщение без пробелов: ", orig_mess)
print("Введенный пароль без пробелов:    ", password)

# записываем пароль такой же длины, как и предложение
mess = list(mess)
passw = list()
for i in range(0, len(mess)):
    index = i % len(password)
    passw.append(password[index])

print("\nПароль над предложением:")
print(passw)
print(mess)

# создаем таблицу для шифрования
table = list()
table.append(alphabet)
for i in range(1, len(alphabet)):
    tmp_alph = alphabet[i:] + alphabet[:i]
    table.append(tmp_alph)

print("\nТаблица шифрования")
for t in table:
    print(t)

# шифруем сообщение по таблице
cypher_mess = str()
for i in range(0, len(passw)):
    row = alphabet.index(passw[i])
    col = alphabet.index(mess[i])
    cypher_mess += table[row][col].upper()

print("\nВведенное сообщение без пробелов: ", orig_mess)
print("Зашифрованное сообщение:          ", cypher_mess)

