print("------------------------")
print(" Маршрутное шифрование")
print("------------------------")

alphabet = "а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"
alphabet = alphabet.split()
mess = str(input("Введите предложение, которое нужно зашифровать: ")).lower()
# mess = 'нельзя недооценивать противника'
mess = mess.replace(' ', '')
mess = mess.replace('\t', '')
orig_mess = mess
mess = list(mess)
# n_block = int(input("Введите длину блока N: "))
# n_block = 4
password = str(input("Введите пароль: ")).lower()
# password = 'пароль'
password = password.replace(' ', '')
password = password.replace('\t', '')

n_block = len(password)

print("\nВведенное сообщение без пробелов: ", orig_mess)
print("Длина блока N:                    ", n_block)
print("Введенный пароль без пробелов:    ", password)

# дополняем строку буквами "а" до кратного числу N
while len(mess) % n_block != 0:
    mess.append('а')

# делим строку на блоки длины N
table = list()
tmp_lst = list()
for i in range(0, len(mess)):
    if i % n_block == 0 and i != 0:
        table.append(tmp_lst)
        tmp_lst = list()
    tmp_lst.append(mess[i])
    if i == len(mess) - 1:
        table.append(tmp_lst)

print("\nТаблица")
for t in table:
    print(t)

# сортируем пароль и формируем шифруем сообщение согласно столбцам таблицы по алфавиту пароля
sort_password = sorted(password)
print("_____" * n_block)
print(list(password))
cypher_mess = str()
for i in sort_password:
    col = password.index(i)
    for row in range(0, len(table)):
        cypher_mess += table[row][col].upper()

print("\nВведенное сообщение без пробелов: ", orig_mess)
print("Зашифрованное сообщение:          ", cypher_mess)
