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

##### РОССИЙСКИЙ УНИВЕРСИТЕТ ДРУЖБЫ НАРОДОВ
##### Факультет физико-математических и естественных наук  
##### Кафедра математического моделирования и искусственного интеллекта 
##### ПРЕЗЕНТАЦИЯ ПО ЛАБОРАТОРНОЙ РАБОТЕ №2

дисциплина: Математические основы защиты информации и информационной безопасности

Преподователь: Кулябов Дмитрий Сергеевич

Cтудент: Попов Дмитрий Павлович

Группа: НФИмд-01-23

МОСКВА

2023 г.

# **Прагматика выполнения лабораторной работы**

- Требуется реализовать: 

1. Маршрутное шифрование.
2. Шифрование с помощью решеток.
3. Таблица Виженера

# **Цель работы**

Освоить на практике шифры перестановки.

# **Выполнение лабораторной работы**

# 1. Реализовал программу для маршрутного шифрования (1/2)
![route1](screenshots/img1.png){width=65%}

# 1. Реализовал программу для маршрутного шифрования (2/2)
![route2](screenshots/img2.png){width=80%}

# 2. Вывод работы первой программы
![route_out](screenshots/img3.png){width=80%}

# 3. Реализовал программу для шифрования с помощью решеток (1/3)
![grid1](screenshots/img4.png){width=60%}

# 3. Реализовал программу для шифрования с помощью решеток (2/3)
![grid2](screenshots/img5.png){width=60%}

# 3. Реализовал программу для шифрования с помощью решеток (3/3)
![grid3](screenshots/img6.png){width=60%}

# 4. Вывод работы второй программы (1/3)
![grid_out1](screenshots/img7.png){width=60%}

# 4. Вывод работы второй программы (2/3)
![grid_out2](screenshots/img8.png){width=60%}

# 4. Вывод работы второй программы (3/3)
![grid_out3](screenshots/img9.png){width=70%}

# 5. Реализовал программу для шифрования таблицей Виженера (1/2)
![viginere1](screenshots/img10.png){width=65%}

# 5. Реализовал программу для шифрования таблицей Виженера (2/2)
![viginere2](screenshots/img11.png){width=70%}

# 6. Вывод работы третьей программы (1/3)
![viginere_out1](screenshots/img12.png){width=80%}

# 6. Вывод работы третьей программы (2/3)
![viginere_out2](screenshots/img13.png){width=80%}

# 6. Вывод работы третьей программы (3/3)
![viginere_out3](screenshots/img14.png){width=80%}


# Вывод
В результате выполнения работы я освоил на практике применение шифров перестановки.