---
# Front matter
title: "Лабораторная работа 3"
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
<p>ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ №3
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

Целью данной работы является приобретение практических навыков в шифровании гаммированием.[1]

# Выполнение лабораторной работы

Требуется реализовать:

1. Шифрование гаммированием конечной гаммой


## Шифрование гаммированием конечной гаммой

Гаммирование — процедура наложения при помощи некоторой функции F на
исходный текст гаммы шифра, т.е. псевдослучайной последовательности (ПСП) с
выходов генератора G. Псевдослучайная последовательность по своим
статистическим свойствам неотличима от случайной последовательности, но
является детерминированной, т.е. известен алгоритм ее формирования. 

Входной текст преобразовывается в номера букв из алфавита, соответствующим буквам фразы, затем так же преобразовывается гамма. Далее используется операция побитового сложения по модулю, равному длине алфавита. Получаем итоговую последовательность чисел, которая переводится в буквы в соответствии с алфавитом и получаем конечную криптограмму.

Чтобы реализовать программу был написал код на Python(@fig:001)(@fig:002):

![gamma1](screenshots/img1.png){#fig:001 width=80%}

![gamma2](screenshots/img2.png){#fig:002 width=80%}

Затем я запустил программу, ввел гамму и исходное сообщение. Получил зашифрованное сообщение.
Вывод работы программы (@fig:003)

![gamma_out](screenshots/img3.png){#fig:003 width=80%}



# Выводы

В результате выполнения работы я освоил на практике применение шифрования с гаммированием конечной гаммой.

# Список литературы

1. Методические материалы курса
