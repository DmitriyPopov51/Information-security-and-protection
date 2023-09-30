---
# Front matter
title: "Лабораторная работа 2"
author: "Попов Дмитрий Павлович, НФИмд-01-23"

# Generic otions
lang: ru-RU
toc-title: "Содержание"

# Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

# Pdf output format
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
### Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Misc options
indent: true
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

<h1 align="center">
<p>РОССИЙСКИЙ УНИВЕРСИТЕТ ДРУЖБЫ НАРОДОВ 
<p>Факультет физико-математических и естественных наук  
<p>Кафедра математического моделирования и искусственного интеллекта
<p>ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ №2
<br></br>
<h2 align="right">
<p>дисциплина: Математические основы защиты информации и информационной безопасности
<p>Преподователь: Кулябов Дмитрий Сергеевич
<p>Студент: Попов Дмитрий Павлович
<p>Группа: НФИмд-01-23
<br></br>
<br></br>
<h1 align="center">
<p>МОСКВА
<p>2023 г.
</h1>

# Цель работы

Целью данной работы является приобретение практических навыков в шифрах перестановки.[1]

# Выполнение лабораторной работы

Требуется реализовать:

1. Маршрутное шифрование.
2. Шифрование с помощью решеток.
3. Таблица Виженера


## Маршрутное шифрование

Текст разбивается на равные блоки N длиной M. Если в конце не хватает букв, то они добавляются в конец.
Блоки записываются построчно в таблицу. Затем буквы выписываются по столбцам, которые упорядываются согласно паролю:
внизу таблицы приписывается слово из n неповторяющихся букв и столбы нумеруются по алфавитному порядку букв пароля

Чтобы реализовать программу был написал код на Python(@fig:001)(@fig:002):

![route1](screenshots/img1.png){#fig:001 width=80%}

![route2](screenshots/img2.png){#fig:002 width=80%}

Затем я запустил программу, ввел пароль и исходное сообщение. Получил таблицу шифрования, далее получил зашифрованное сообщение.
Вывод работы программы (@fig:003)

![route_out](screenshots/img3.png){#fig:003 width=80%}


## Шифрование с помощью решеток

Строится квадрат из k чисел. Затем к нему добавляются еще 3 квадрата, которые поворачиваются на 90 градусов и получается большой квадрат 2k размерностью.
Дальше из большого квадрата вырезаются клетки и прорези записываются буквы. Когда заполнятся все прорези решето поворачивается на 90 градусов.
И так продолжается пока не заполнится вся таблица. И буквы выписываются по алфивитному порядку пароля.

Чтобы реализовать программу был написал код на Python(@fig:004)(@fig:005)(@fig:006):

![grid1](screenshots/img4.png){#fig:004 width=80%}

![grid2](screenshots/img5.png){#fig:005 width=80%}

![grid3](screenshots/img6.png){#fig:006 width=80%}

Затем я запустил программу. Получил матрицы шифрования, далее получил зашифрованное сообщение.
Вывод работы программы (@fig:007)(@fig:008)(@fig:009)

![grid_out1](screenshots/img7.png){#fig:007 width=80%}

![grid_out2](screenshots/img8.png){#fig:008 width=80%}

![grid_out3](screenshots/img9.png){#fig:009 width=80%}


## Таблица Виженера

В таблице записаны буквы русского алфавита. При переходе от одной  строке к другой происходит циклический сдвиг на одну позицию.
Пароль записывается с повторениями над буквами сообщения.
В горизонтальном алфавите ищем букву нашего текста, а в вертикальном букву пароля и на их пересечении будет нужная нам буква.

Чтобы реализовать программу был написал код на Python(@fig:010)(@fig:011):

![viginere1](screenshots/img10.png){#fig:010 width=80%}

![viginere2](screenshots/img11.png){#fig:011 width=80%}

Затем я запустил программу, ввел пароль и исходное сообщение. Получил пароль над предложением, таблицу шифрования (алфавит), далее получил зашифрованное сообщение.
Вывод работы программы (@fig:012)(@fig:013)(@fig:014)

![viginere_out1](screenshots/img12.png){#fig:012 width=80%}

![viginere_out2](screenshots/img13.png){#fig:013 width=80%}

![viginere_out3](screenshots/img14.png){#fig:014 width=80%}


# Выводы

В результате выполнения работы я освоил на практике применение шифров перестановки.

# Список литературы

1. Методические материалы курса
