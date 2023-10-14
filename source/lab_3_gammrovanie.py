print("---------------------------")
print(" Шифрование гаммированием")
print("---------------------------")


def crypt(mess, gamma, alphabet):
    # делаем гамму по длине больше, чем сообщение для шифрования
    while len(gamma) < len(mess):
        gamma += gamma
    # создаем списки из номеров букв из алфавита в сообщении и гамме
    mess_numb, gamma_numb, cypher_numb = [], [], []
    for symbol in mess:
        mess_numb.append(alphabet.index(symbol) + 1)
    for symbol in gamma:
        gamma_numb.append(alphabet.index(symbol) + 1)
    # шифруем сообщение по рекуррентной формуле
    cypher_mess = ''
    for i in range(0, len(mess_numb)):
        c = mess_numb[i] + gamma_numb[i] % len(alphabet)
        cypher_numb.append(c)
        cypher_mess += str(alphabet[c - 1])
    print(alphabet)
    print("      Введенное сообщение: ", mess.upper(), mess_numb)
    print("   Зашированное сообщение: ", cypher_mess.upper(), cypher_numb)


alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
mess = str(input("Введите предложение, которое нужно зашифровать: ")).lower().replace(' ', '')
# mess = 'приказ'.replace(' ', '')
gamma = str(input("Введите гамму: ")).lower()
# gamma = 'гамма'

crypt(mess=mess, gamma=gamma, alphabet=alphabet)
