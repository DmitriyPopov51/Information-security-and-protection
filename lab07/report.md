---
# Front matter
title: "Лабораторная работа 7"
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
<p>ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ №7
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

Освоить на практике дискретное логарифмирование в конечном поле.[1]

# Выполнение лабораторной работы

Требуется реализовать:

1. Алгоритм, реализующий p-метод Полларда для задач дискретного логарифмирования


## p-метод Полларда

Основные шаги:

Вход: Простое число p, числа a порядка r по модулю p, целое число b, 1< b < p отображение f, обладающее сжимающими свойствами и сохраняющее вычислимость логарифма
Выход: Показатель x, Для которого a^x Тождественно = b (mod p), если такой показатель существует
1. Выбрать произвольные числа u, v и положить c <- a^u * b^v (mod p), d <- c
2. Выполнять c <- f(c)(mod p), d <- f(f(d))(mod p), вычисляя при этом логарифмы для c и d как линейные функции от x по модулю r, до получения равенства c тождественно = d(mod p)
3. Приравняв логарифмы для c и d, вычислить логарифм x решением сравнения по модулю r. Результат: x или "Решения нет"

Чтобы реализовать программу был написал след. код на python:

1. Функция, реализующая p-метод Полларда [@fig:1].
2. Функция нахождения НОД [@fig:2].
3. Расширенный алгоритм Евклида для вычисления модульного обратного элемента [@fig:3].

![pollard](screenshots/img1.png){#fig:1 width=80%}

![gcd](screenshots/img2.png){#fig:2 width=80%}

![modinv](screenshots/img3.png){#fig:3 width=80%}

Выходные значения программы  [@fig:4].

![output](screenshots/img4.png){#fig:4 width=80%}


# Выводы

В результате выполнения работы я освоил на практике дискретное логарифмирование в конечном поле.


# Список литературы

1. Методические материалы курса
