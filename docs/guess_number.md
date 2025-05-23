# Документация

Игра "Угадай число" (C++)

## Описание

Это простая консольная игра, в которой программа случайным образом загадывает число от 1 до 100.
Задача пользователя — угадать это число, вводя свои варианты.

Программа даёт подсказки:
- Если число больше загаданного — "Меньше!"
- Если меньше — "Больше!"
- Если пользователь угадывает число — "Ты угадал!"

## Цель

Цель игры — угадать число за минимальное количество попыток.

## Используемые технологии

- Язык: C++
- Функции: `rand()`, `srand()`, `time()`
- Цикл: `do-while`
- Ввод/вывод: `cin`, `cout`
- Локализация: `setlocale()`
- Среда: Visual Studio 2022

## Пример вывода

Угадай число от 1 до 100:

Твой вариант: 50

Больше!

Твой вариант: 75

Меньше!

Твой вариант: 65

Ты угадал!
