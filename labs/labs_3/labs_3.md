# Лабораторная работа №3: Ввод и вывод данных.

## Цель: Научиться вводить и выводить данные в Python.

### 📌 Ввод данных

В Python для ввода данных от пользователя используется функция `input()`. Эта функция позволяет пользователю ввести строку текста, которая затем может быть обработана программой.

**Синтаксис:**

```python
    input(prompt)
```

- `prompt` (необязательный параметр) — строка, которую программа выводит пользователю перед ожиданием ввода.

**Пример использования:**
```python
    # Запрашиваем у пользователя его имя и сохраняем его в переменную 'name'
    name = input("Введите ваше имя: ")
    # Выводим сообщение с использованием введенного имени
    print("Привет, " + name + "!")
```

- В этом примере, когда программа запрашивает ввод имени, пользователь вводит текст, который сохраняется в переменной `name`. Затем программа выводит сообщение, объединяя строку `"Привет, "` с введенным именем и восклицательным знаком.

Примечание: Все данные, введенные через `input()`, воспринимаются как строки (тип `str`). Если нужно преобразовать их в другой тип (например, в число), используйте функции преобразования типов.

**Пример преобразования строкового ввода в число:**
```python
    # Запрашиваем у пользователя его возраст
    age = input("Введите ваш возраст: ")
    # Преобразуем введенное значение в целое число
    age = int(age)
    # Выводим сообщение с возрастом
    print("Вам " + str(age) + " лет.")
```

- В этом примере `input()` возвращает строку, которая затем преобразуется в целое число с помощью `int()`. Функция `str()` используется для преобразования числа обратно в строку для вывода.

### 📌 Вывод данных
Для вывода данных на экран в Python используется функция `print()`. Она может принимать несколько аргументов и выводить их на экран, разделяя пробелами.

**Синтаксис:**
```python
    print(*objects, sep=' ', end='\n', file=sys.stdout)
```
- `objects` — объекты, которые будут выведены на экран.
- `sep` — строка, которая будет использоваться в качестве разделителя между объектами (по умолчанию пробел)
- `end` — строка, которая будет добавлена в конце строки (по умолчанию символ новой строки \n).
`file` — поток, куда будет записан вывод (по умолчанию стандартный поток вывода).

**Пример использвоания:**
```python
    # Выводим два слова, разделяя их пробелом (по умолчанию)
    print("Hello", "World")  # Выведет: Hello World

    # Выводим два слова, разделяя их дефисом
    print("Hello", "World", sep="-")  # Выведет: Hello-World

    # Выводим слово "Hello" без перевода строки в конце
    print("Hello", end="!")  # Выведет: Hello!

    # Продолжаем вывод на той же строке
    print("World")  # Выведет: World
```
- В этом примере `print()` используется для вывода строк с различными настройками разделителя и конца строки.

### 📌 Форматирование строк
Python предоставляет несколько способов форматирования строк, чтобы вывести данные в нужном формате.

**1. Оператор `%` (старый стиль):**
```python
    name = "Alice"
    age = 30
    # Форматируем строку с помощью оператора %
    print("Имя: %s, Возраст: %d" % (name, age))
```
- `%s` используется для `строк`
- `%d` для `целых чисел`

**2. Метод format():**
```python
    name = "Alice"
    age = 30
    # Форматируем строку с помощью метода format()
    print("Имя: {}, Возраст: {}".format(name, age))
```
- В фигурных скобках `{}` можно указать позиционные или именованные аргументы, которые будут заменены значениями, переданными методу `format()`.

**3. F-строки:**
```python
    name = "Alice"
    age = 30
    # Форматируем строку с помощью f-строк
    print(f"Имя: {name}, Возраст: {age}")
```
- `F-строки` позволяют встраивать переменные и выражения прямо в строку, делая код более читаемым и удобным.

## Лабораторная работа <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Man%20Technologist.png" alt="Man Technologist" width="45" height="45" />

### 📌 Задача 1: Введение и вывод текста.
Напишите программу, которая запрашивает у пользователя его `имя` и `возраст`, а затем `выводит сообщение` с этой информацией.

#### Шаги:
1. Используйте `input()` для получения имени и возраста пользователя.
2. Преобразуйте возраст в целое число с помощью `int()`.
3. Выведите сообщение с использованием форматирования строк.

### 📌 Задача 2: Калькулятор простых операций
Напишите программу, которая запрашивает у пользователя два числа и выполняет сложение, вычитание, умножение и деление.

#### Шаги:

1. Получите два числа от пользователя с помощью `input()`.
2. Преобразуйте введенные значения в числа с помощью `float()`.
3. Выполните арифметические операции и выведите результаты.

### 📌 Задача 3: Конвертер температуры
Напишите программу, которая конвертирует температуру из Цельсия в Фаренгейт по формуле:
$$\large
F = C * \frac{9}{5} + 32
$$

### Шаги:
1. Получите температуру в градусах Цельсия от пользователя.
2. Преобразуйте значение в вещественное число.
3. Примените формулу и выведите результат.



____

[Вернуться на главную страницу](https://valeogamer.github.io/Python_2024_MarSU/)