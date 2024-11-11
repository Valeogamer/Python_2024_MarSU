# Лабораторная работа №9: Запись и чтение файла

## Цель
Целью данной лабораторной работы является изучение операций с файлами в языке Python. Это включает в себя создание, открытие, запись в файлы, а также их чтение. Операции с файлами позволяют работать с внешними данными, такими как текстовые документы, конфигурационные файлы, логи и т.д.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Теоретическая часть
В Python для работы с файлами используется встроенная библиотека `open()`, которая позволяет открывать файлы для чтения, записи и других операций. Работа с файлами включает следующие этапы:

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Открытие файла
Открытие файла. Для того чтобы работать с файлом, необходимо его открыть с помощью функции `open()`. Эта функция принимает два основных параметра:

**Имя файла** (или путь к файлу).

**Режим работы с файлом**. Основные режимы:
- 'r' — открытие файла для чтения (по умолчанию).
- 'w' — открытие файла для записи (перезаписывает файл, если он существует, или создает новый).
- 'a' — открытие файла для добавления данных в конец файла.
- 'rb' и 'wb' — открытие файла в бинарном режиме для чтения или записи.
- 'x' — создание нового файла и открытие его для записи (если файл существует, вызовет ошибку).

```python
# Открытие файла для чтения
file = open('example.txt', 'r')

# Открытие файла для записи (перезапись файла)
file = open('example.txt', 'w')

# Открытие файла для добавления данных
file = open('example.txt', 'a')

# Открытие файла в бинарном режиме для чтения
file = open('example.bin', 'rb')

# Открытие файла в бинарном режиме для записи
file = open('example.bin', 'wb')

# Открытие файла для записи с условием, что файл должен быть новым
file = open('new_file.txt', 'x')
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Чтение файла
Чтение файла. Для чтения файла можно использовать несколько методов:
- read() — читает весь файл целиком.
- readline() — читает одну строку.
- readlines() — читает файл построчно и возвращает список строк.

```python
# Открытие файла для чтения
file = open('example.txt', 'r')

# Чтение всего файла целиком
content = file.read()
print(content)

# Чтение одной строки
line = file.readline()
print(line)

# Чтение всех строк файла в список
lines = file.readlines()
print(lines)

# Не забываем закрывать файл после чтения
file.close()
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Запись в файл.
Запись в файл. Для записи данных в файл используйте методы:
- write() — записывает строку в файл.
- writelines() — записывает список строк.

```python
# Открытие файла для записи (перезаписать содержимое)
file = open('example.txt', 'w')

# Запись строки в файл
file.write('Hello, world!\n')

# Запись списка строк в файл
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
file.writelines(lines)

# Закрытие файла после записи
file.close()
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Закрытие файла.
Закрытие файла. После выполнения операций с файлом, его необходимо закрыть с помощью метода `close()`, чтобы освободить ресурсы.
```python
# Открытие файла для записи
file = open('example.txt', 'w')

# Запись данных в файл
file.write('Some text')

# Закрытие файла после работы с ним
file.close()
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Конструкция with
Кроме того, часто используется конструкция with, которая автоматически закрывает файл после выполнения операций.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Пример записи в файл
```python
# Открытие файла для записи (перезапишет файл, если он существует)
with open('example.txt', 'w') as file:
    file.write("Привет, мир!\n")
    file.write("Это пример записи в файл.\n")
```
В данном примере:

Файл example.txt откроется для записи. Если файл не существует, он будет создан.
Мы записываем две строки в файл с помощью метода write().

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Пример чтения из файла
```python
# Открытие файла для чтения
with open('example.txt', 'r') as file:
    content = file.read()  # Чтение всего файла
    print(content)
```
Здесь:

Файл открывается для чтения.
Метод `read()` считывает весь файл целиком и выводит его содержимое на экран.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Пример построчного чтения из файла
```python
# Чтение файла построчно
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Метод strip() удаляет лишние символы новой строки
```
Здесь:

Мы используем цикл for для чтения файла построчно.
Каждая строка выводится с удалением символов новой строки.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Пример добавления данных в файл
```python
# Открытие файла для добавления данных в конец
with open('example.txt', 'a') as file:
    file.write("Добавляем еще одну строку.\n")
```
В этом примере:

Файл открывается в режиме 'a', который позволяет добавлять данные в конец файла, не перезаписывая его.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Открытие файла с использованием with
Когда мы используем with, Python автоматически закрывает файл после выхода из блока `with`. Пример:
```python
# Открытие файла для чтения
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Открытие файла для записи (перезапись содержимого)
with open('example.txt', 'w') as file:
    file.write('Hello, world!\n')

# Открытие файла для добавления данных в конец
with open('example.txt', 'a') as file:
    file.write('This is an appended line.\n')

# Открытие файла в бинарном режиме для чтения
with open('example.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)

# Открытие файла в бинарном режиме для записи
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03')

# Открытие файла для записи с условием, что файл должен быть новым
with open('new_file.txt', 'x') as file:
    file.write('This file was just created.\n')
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Чтение файла с использованием with
Для чтения файла мы можем использовать методы read(), readline() и readlines(). Вот примеры:
```python
# Открытие файла для чтения
with open('example.txt', 'r') as file:
    # Чтение всего файла целиком
    content = file.read()
    print(content)

    # Чтение одной строки
    line = file.readline()
    print(line)

    # Чтение всех строк файла в список
    lines = file.readlines()
    print(lines)
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Запись в файл с использованием with
Для записи данных в файл с использованием конструкции with:
```python
# Открытие файла для записи (перезапись содержимого)
with open('example.txt', 'w') as file:
    # Запись строки в файл
    file.write('Hello, world!\n')

    # Запись списка строк в файл
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)
```

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Raccoon.png" alt="Raccoon" width="30" height="30" style="vertical-align: middle"/> Закрытие файла с использованием with
С использованием конструкции with не нужно вызывать file.close(), так как файл будет автоматически закрыт при выходе из блока with. Вот пример:
```python
# Открытие файла для записи и автоматическое его закрытие
with open('example.txt', 'w') as file:
    file.write('Some text')

# Нет необходимости вызывать file.close() — файл будет закрыт автоматически
```

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Hourglass%20Not%20Done.png" alt="Hourglass Not Done" width="35" height="35" /> Лабораторная работа

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 1: Чтение и подсчет строк в файле
Прочитать файл и подсчитать количество строк, слов и символов в нем.

Условия:
- Сгенерируйте файл с данными.
- Прочитать файл и подсчитать:
- Общее количество строк.
- Общее количество слов.
- Общее количество символов.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 2: Запись списка в файл
Написать функцию которая записывает список строк в новый текстовый файл.

Условия:
- Вам нужно создать список строк (например, из списка студентов, продуктов или фильмов).
- Записать все строки в новый файл.
- Программа должна записывать данные в файл построчно.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 3: Модификация файла — добавление уникальных строк
Прочитать файл и добавить в него уникальные строки (которые отсутствуют в файле).

Условия:
- Создайте два файла file1.txt и file2.txt с произвольным текстом.
- Прочитать строки из обоих файлов.
- Добавить в первый файл строки, которые есть во втором файле, но отсутствуют в первом.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 4: Фильтрация и запись данных в новый файл
Прочитать файл, отфильтровать строки по условию и записать результат в новый файл.
(файл с числами создайте сами)

Условия:
- Создайте файл с числами, каждое число на новой строке.
- Прочитать данный файл.
- Необходимо оставить в файле только четные числа.
- Отфильтрованные числа записать в новый файл.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Fire.png" alt="Fire" width="25" height="25" /> Задание 5: Перевод текста в верхний регистр
Прочитать файл, преобразовать весь текст в верхний регистр и записать в новый файл.

Условия:
- Создайте файл с текстом
- Прочитать файл, преобразовать весь текст в верхний регистр.
- Записать преобразованный текст в новый файл.

Используйте метод `upper()` для преобразования текста в верхний регистр.