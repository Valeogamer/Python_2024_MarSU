# Лабораторная работа №7: Функции

## Цель научиться использовать функции

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Что такое функция?

`Функция` — это именованный блок кода, который выполняет определённую задачу. Основная цель функций — это улучшение структуры кода, упрощение его понимания и повторное использование.

**Пример:**
Представьте, что вы хотите написать программу, которая будет складывать числа. Если вы просто напишете код для сложения каждый раз, когда вам это нужно, ваш код станет громоздким. Вместо этого вы можете создать функцию, которая делает это за вас.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Синтаксис функции

Вот как выглядит базовая структура функции в Python:

```python
def имя_функции(параметры):
    """Докстринг (необязательно)"""
    # Тело функции
    return значение  # (необязательно)
```

- **`def`**: ключевое слово, которое сообщает Python, что мы определяем новую функцию.
- **`имя_функции`**: имя функции. Обычно оно должно быть описательным и начинаться с буквы.
- **`параметры`**: значения, которые функция может принимать (например, числа, строки и т. д.). Эти значения передаются в скобках.
- **`return`**: оператор, который используется для возврата результата функции. Если `return` не указан, функция вернёт `None`.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Докстринги

Докстринг — это строка, которая описывает, что делает функция. Она помогает другим разработчикам (и вам самим) понять, как использовать функцию.

**Пример:**

```python
def sum(a, b):
    """Возвращает сумму двух чисел a и b.""" <- вот  это докстринг
    return a + b

result = sum(10, 11)
print(result) # выведет 21
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Параметры функции

Параметры — это переменные, которые вы определяете в скобках функции. Они служат для передачи данных в функцию.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Обязательные параметры

Эти параметры должны быть переданы при вызове функции.

```python
def mul(a, b): # обязательные параметры `a` и `b`
    return a * b

result = mul(5, 5)
print(result)  # 25
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Необязательные параметры с значениями по умолчанию

Если значение не передано, используется значение по умолчанию.

```python
def hello(name="Гость"): # name необязательный, по умолчанию Гость.
    print(f"Привет, {name}!")

hello()  # Выведет: Привет, Гость!
hello("Аня")  # Выведет: Привет, Аня!
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Возврат значений

Функции могут возвращать одно или несколько значений с помощью оператора `return`. Если `return` не используется, функция возвращает `None`.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Возврат одного значения

```python
def pow(n):
    return n ** 2

result = pow(4)
print(result)  # 16
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Возврат нескольких значений

Можно вернуть несколько значений в виде кортежа.

```python
def division(a, b):
    div = a / b  # деление 
    rem = a % b  # остаток 
    return div, rem

div, rem = division(10, 3)
print(div)  # Выведет: 3.3
print(rem)    # Выведет: 1
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Области видимости

Область видимости переменных определяет, где переменная доступна.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Локальные переменные

Локальные переменные определяются внутри функции и доступны только в ней.

```python
def func():
    local_var = "Я локальная" # локальная переменная
    print(local_var)

func()  # Выведет: Я локальная
print(local_var)  # Ошибка, переменная не доступна так как существует только внутри функции или не возвращена
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Глобальные переменные

Глобальные переменные определяются вне всех функций и доступны в любой части программы.

```python
global_var = "Я глобальная" # глобальная переменная доступна везде

def func():
    print(global_var) # глобальная переменная доступна и здесь, хотя как видим находится вне функции

func()  # Выведет: Я глобальная
print(global_var) 
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Аргументы функции

При вызове функции можно передавать аргументы разными способами.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Позиционные аргументы

Параметры передаются в том порядке, в котором они указаны.

```python
def sum(a, b):
    return a + b

print(sum(2, 3))  # Выведет: 5
res = sum(5, 10)
print(res) # Выведет 15
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Ключевые аргументы

Аргументы передаются с указанием имени параметра.

```python
def welcome(name, text="Привет"):
    print(f"{name}, {name}!")

welcome(name="Аня", text="Здравствуйте")  # Выведет: Здравствуйте, Аня!
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Аргументы переменной длины

Если вы не знаете, сколько аргументов будет передано, можно использовать `*args` и `**kwargs`.

- **`*args`**: позволяет передавать произвольное количество позиционных аргументов.
- **`**kwargs`**: позволяет передавать произвольное количество ключевых аргументов.

```python
def func(*args, **kwargs):
    print(args)    # Позиционные аргументы
    print(kwargs)  # Ключевые аргументы

func(1, 2, 3, имя="Аня", возраст=30)
# Выведет:
# (1, 2, 3)
# {'имя': 'Аня', 'возраст': 30}
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Wolf.png" alt="Wolf" width="30" height="30" style="vertical-align: middle"/> Рекурсивные функции

Рекурсивная функция — это функция, которая вызывает саму себя. Это позволяет решать задачи, разбивая их на подзадачи.

**Пример: Факториал**

Факториал числа \( n \) (обозначается \( n! \)) — это произведение всех целых чисел от 1 до \( n \).

```python
def factorial(n):
    if n == 0:  # Базовый случай
        return 1
    else:
        return n * factorial(n - 1)  # Рекурсивный вызов

print(факториал(5))  # Выведет: 120
result = factorial(5)
print(result)
```

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Hourglass%20Not%20Done.png" alt="Hourglass Not Done" width="35" height="35" /> Лабораторная работа

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 1: Калькулятор

**Описание:** Создайте программу, которая реализует простой калькулятор. Функции должны выполнять сложение, вычитание, умножение и деление.

**Требования:**
- Реализуйте функции `add`, `subtract`, `multiply` и `divide`.
- В каждой функции должны быть параметры для двух чисел.
- Функция `divide` должна обрабатывать случай деления на ноль.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 2: Конвертер единиц

**Описание:** Напишите программу, которая конвертирует единицы измерения (метры, километры, миллиметры).

**Требования:**
- Создайте функцию convert_length, которая принимает три параметра: `значение`, `исходную единицу` и `целевую единицу(единица в которую конвертируем)`.
- Реализуйте конвертацию между метрами, километрами и миллиметрами.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 3: Факториал числа

**Описание:** Создайте программу для вычисления факториала числа.

**Требования:**
- Реализуйте функцию factorial, которая принимает одно целое неотрицательное число.
- Функция должна использовать рекурсию.
- Обработайте случай, когда передано отрицательное число.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 4: Генератор последовательности Фибоначчи

**Описание:** Создайте программу, которая генерирует последовательность Фибоначчи.

**Требования:**
- Реализуйте функцию fibonacci, которая принимает одно целое число (количество элементов в последовательности).
- Функция должна возвращать список из элементов последовательности Фибоначчи.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 5: Печать таблицы умножения

**Описание:** Напишите программу, которая выводит таблицу умножения для заданного числа.

**Требования:**
- Реализуйте функцию multiplication_table, которая принимает число и выводит таблицу умножения от 1 до 10.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 6: Калькулятор процентов

**Описание:** Напишите программу, которая вычисляет процент от заданного числа.

**Требования:**
- Пользователь вводит число и процент.
- Программа должна вычислить и вывести значение процента.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 7: Расчет простых процентов

**Описание:** Создайте программу, которая вычисляет простые проценты.

**Формула:** Простые проценты = Сумма * Процент * Время(в годах) / 100

**Требования:**
- Пользователь вводит сумму, процент и время.
- Программа выводит сумму процентов.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 8: Нахождение среднего арифметического

**Описание:** Напишите программу, которая находит среднее арифметическое списка чисел.

**Требования:**
- Пользователь вводит числа, разделенные запятыми.
- Программа вычисляет и выводит среднее арифметическое.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 9: Расчет объемов фигур

**Описание:** Напишите программу, которая рассчитывает объемы различных фигур (куб, параллелепипед, цилиндр).

**Требования:**
- Пользователь выбирает фигуру и вводит необходимые размеры.
- Выводите объем фигуры по формуле.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 10: Расчет финансового бюджета

Описание: Напишите программу, которая помогает пользователю вести бюджет.

Требования:
- Пользователь вводит доходы и расходы.
- Программа должна подсчитывать баланс (доходы - расходы).
- Позволяйте пользователю добавлять новые доходы и расходы.

___

[Вернуться на главную страницу](https://valeogamer.github.io/Python_2024_MarSU/)