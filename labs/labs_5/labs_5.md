# Лабораторная работа №5: Циклы

## Цель: Научиться использовать циклы.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Avocado.png" alt="Avocado" width="30" height="30" style="vertical-align: middle"/> Циклы в Python
Циклы являются фундаментальной конструкцией в программировании, позволяющей выполнять блок кода многократно до тех пор, пока не будет достигнуто определённое условие. В Python существуют два основных типа циклов:
1. `for`
2. `while`


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Avocado.png" alt="Avocado" width="30" height="30" style="vertical-align: middle"/> FOR
Цикл for используется для перебора элементов последовательности (списка, строки, кортежа, множества, словаря и других итерируемых объектов).

```python
    for элемент in последовательность:
        тело цикла
```
**Пример 1**
```python 
    # Пример
    fruits = ['яблоко', 'банан', 'вишня']  # Список (*ознакомимся в лабе структура данных)
    for fruit in fruits:
        print(fruit)
    
    # Вывод:
    яблоко
    банан
    вишня
```

**Пример 2**
```python 
    text = 'Hello'
    for symbol in text:
        print(symbol)
    
    # Вывод:
    H
    e
    l
    l
    o
```

**Пример 3**
```python 
    num = 5
    for n in range(num):
        print(n)
    
    # Вывод:
    0
    1
    2
    3
    4
```

**Пример 4**
```python 
    start = 10
    stop = 15
    for n in range(start, stop):
        print(n)
    # Вывод:
    10
    11
    12
    13
    14
```

**Пример 5**
```python 
    start = 20
    stop = 40
    step = 3
    for num in range(start, stop, step):
        print(num)
    # Вывод:
    20
    23
    26
    29
    32
    35
    38
```


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Avocado.png" alt="Avocado" width="30" height="30" style="vertical-align: middle"/> Функция range

Часто цикл for используется вместе с функцией `range()`, которая генерирует последовательность чисел.

Параметры функции `range`:
- `range(stop)` – генерирует числа от `0` до `stop - 1`.

```python
    # пройтись от 0 до 5, на каждом шаге значение хранить в переменной `num`
    for num in range(5):  # от 0 до 5, не включая 5.
        print(num)

    # Вывод
    0
    1
    2
    3
    4
```

- `range(start, stop)` – генерирует числа от `start` до `stop - 1`.

```python
    # пройтись от start до stop, на каждом шаге значение хранить в переменной `num`
    start = 5
    stop = 10
    for num in range(start, stop):  # от 5 до 10, не включая 10.
        print(num)

    # Вывод
    5
    6
    7
    8
    9
```

- `range(start, stop, step)` – генерирует числа от `start` до `stop - 1` с шагом `step`.

```python
    # пройтись от start до stop, на каждом шаге значение хранить в переменной `num`, с шагом 2
    start = 0
    stop = 10
    step = 2
    for num in range(start, stop, step):  # от 0 до 10, c шагом 2, не включая 10.
        print(num)

    # Вывод
    0
    2
    4
    6
    8
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Avocado.png" alt="Avocado" width="30" height="30" style="vertical-align: middle"/> while

Цикл `while` выполняет блок кода до тех пор, пока условие истинно.

```python
    while условие:
        тело цикла
```

```python
    count = 0  # счетчик чисел равен 0
    while count < 5: # пока счетчик меньше 0
        print(count)  # вывести значение счетчика
        count += 1  # прибавить +1 к счетчику
    
    # Вывод
    0
    1
    2
    3
    4
```

**Важные моменты:**
- Необходимо обеспечить, чтобы условие цикла со временем станет ложным, иначе цикл станет бесконечным.
- Использование управляющих операторов break и continue для управления потоком выполнения внутри цикла.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Avocado.png" alt="Avocado" width="30" height="30" style="vertical-align: middle"/> Управляющие операторы в циклах

#### `break` – немедленно прекращает выполнение цикла.

```python
    for num in range(10): # от 0 до 10
        if num == 5: # если достигли числа 5
            break  # выйти из цикла, то есть прекратить работу цикла если достигли числа 5
        print(num) # Вывод на экран
    
    # Вывод
    0
    1
    2
    3
    4
```

#### `continue` – пропускает текущую итерацию и переходит к следующей.

```python
for num in range(5):
    if num == 2:
        continue
    print(num)

    # Вывод
    0
    1
    3
    4
```

#### `else` в циклах – блок else выполняется после завершения цикла, если он не был прерван оператором break.

```python
    for num in range(3):
        print(num)
    else:
        print("Цикл завершен без break")
    
    # Вывод
    0
    1
    2
    Цикл завершен без break
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Avocado.png" alt="Avocado" width="30" height="30" style="vertical-align: middle"/> Вложенные циклы

Циклы могут быть вложенными друг в друга, что позволяет выполнять более сложные операции, например, обход многомерных структур данных.

```python
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")
    
    # Вывод
    i=0, j=0
    i=0, j=1
    i=1, j=0
    i=1, j=1
    i=2, j=0
    i=2, j=1
```

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Hourglass%20Not%20Done.png" alt="Hourglass Not Done" width="35" height="35" /> Лабораторная работа 

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задача 1. Основы циклов `for` и `while`.

1. Напишите программу, которая выводит числа от `1` до `10` с помощью цикла `for`.

2. Используя цикл `while`, напишите программу, которая запрашивает у пользователя ввод чисел до тех пор, пока пользователь не введёт число `0`. Затем программа выводит сумму введённых чисел.

3. Напишите программу, которая перебирает числа от `1` до `20` и выводит только `чётные числа`, используя оператор `continue`.

4. Напишите программу, которая перебирает числа от `1` до `10` и прекращает выполнение цикла, когда число достигает `5`, используя оператор `break`.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задача 2. Вложенные циклы и обработка данных.

1. Напишите программу, которая выводит таблицу умножения от `1` до `9`, используя вложенные циклы `for`.

2. Напишите программу, которая принимает от пользователя строку и выводит каждый символ строки на отдельной строке, используя цикл `for`.

3. Реализуйте простую игру `"Угадай число"`, где программа загадывает число от `1` до `100`, а пользователь пытается его угадать. Используйте цикл `while` для организации процесса угадывания. Программа должна давать подсказки `"больше"` или `"меньше"` после каждой попытки.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задача 3. Применение циклов в решении задач.

1. Напишите программу, которая находит факториал заданного числа с помощью цикла `for` и `while`.

2. Реализуйте программу для проверки, является ли введённое пользователем число простым.

3. Создайте программу, которая отображает треугольник из символов `*`, где количество строк определяется пользователем. Например, для 5 строк:

```python
    # Пример вывод
    *
    **
    ***
    ****
    *****
```

4. Создайте программу, которая отображает треугольник из символов `*`, где количество строк определяется пользователем. Например, для 5 строк:

```python
    # Пример вывод
    *****
    ****
    ***
    **
    *
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задача 4. Применение циклов в решении задач.

1. Напишите программу, которая ищет первое число, делящееся на 7 и 5 одновременно в диапазоне от 1 до 1000. Прекратите поиск после нахождения первого такого числа, используя оператор break.

2. Вывести все четные числа в диапазоне от `0` до `101`.
   
3. Вывести все нечетные числа в диапазоне от `0` до `-101`.

4. Напишите программу, которая перебирает числа от `1` до `33` и выводит только те, которые делятся на `3`, используя оператор continue для пропуска остальных.

5. Создайте программу, которая проверяет, содержится ли заданное пользователем число в диапазоне от `1` до `100`. Если число найдено, выведите сообщение и завершите цикл с помощью `break`. Если цикл завершился без нахождения числа, выведите соответствующее сообщение, используя блок `else`.

6. Напишите программу, которая выводит все числа от `1` до `100`, которые не делятся на `4` и `6` одновременно. Используйте оператор `continue` для пропуска чисел, которые делятся на оба числа.

___

[Вернуться на главную страницу](https://valeogamer.github.io/Python_2024_MarSU/)